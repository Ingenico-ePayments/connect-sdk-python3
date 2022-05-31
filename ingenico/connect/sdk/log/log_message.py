from .body_obfuscator import BodyObfuscator
from .header_obfuscator import HeaderObfuscator


class LogMessage(object):
    """
    A utility class to build log messages.
    """
    __request_id = None
    __headers = None
    __body = None
    __content_type = None
    __header_list = None
    __body_obfuscator = None
    __header_obfuscator = None

    def __init__(self, request_id,
                 body_obfuscator=BodyObfuscator.default_body_obfuscator(),
                 header_obfuscator=HeaderObfuscator.default_header_obfuscator()):
        if not request_id:
            raise ValueError("request_id is required")
        if not body_obfuscator:
            raise ValueError("body_obfuscator is required")
        if not header_obfuscator:
            raise ValueError("header_obfuscator is required")
        self.__request_id = request_id
        self.__headers = ""
        self.__header_list = []
        self.__body_obfuscator = body_obfuscator
        self.__header_obfuscator = header_obfuscator

    @property
    def request_id(self):
        return self.__request_id

    @property
    def headers(self):
        return str(self.__headers)

    @property
    def body(self):
        return self.__body

    @property
    def content_type(self):
        return self.__content_type

    def add_header(self, name, value):
        if self.__headers:
            self.__headers += ", "
        self.__headers += name + "=\""
        if value is not None and value.lower() != 'none':
            # if isinstance(value, bytes):
            #     value = base64.b64decode(value)  # decode byte-type headers for recording
            value = str(value)
            obfuscated_value = self.__header_obfuscator.obfuscate_header(name, value)
            self.__headers += obfuscated_value
            self.__header_list.append((name, "\"" + obfuscated_value + "\""))
        else:
            self.__header_list.append((name, "\"\""))
        self.__headers += "\""

    def set_body(self, body, content_type, charset=None):
        self.__content_type = content_type
        if self.__is_binary(content_type):
            self.__body = "<binary content>"
        else:
            self.__body = self.__body_obfuscator.obfuscate_body(body, charset)

    def set_binary_body(self, content_type):
        if not self.__is_binary(content_type):
            raise ValueError("Not a binary content type: " + content_type)
        self.__content_type = content_type
        self.__body = "<binary content>"

    def __is_binary(self, content_type):
        if content_type is None:
            return False
        content_type = content_type.lower()
        return not (content_type.startswith("text/") or "json" in content_type or "xml" in content_type)

    def empty_if_none(self, value):
        if value is not None:
            return value
        return ""

    def get_message(self):
        raise NotImplementedError

    def get_header_list(self):
        return self.__header_list
