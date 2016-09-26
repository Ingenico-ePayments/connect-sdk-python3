from .logging_util import LoggingUtil


class LogMessage(object):
    """
    A utility class to build log messages.
    """
    __request_id = None
    __headers = None
    __body = None
    __content_type = None
    __header_list = None
    def __init__(self, request_id):
        if not request_id:
            raise ValueError("request_id is required")
        self.__request_id = request_id
        self.__headers = ""
        self.__header_list = []

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
        if len(self.__headers) > 0:
            self.__headers += ", "
        self.__headers += name + "=\""
        if value is not None and value.lower() != 'none':
            # if isinstance(value, bytes):
            #     value = base64.b64decode(value)  # decode byte-type headers for recording
            value = str(value)
            obfuscated_value = LoggingUtil.obfuscate_header(name, value)
            self.__headers += obfuscated_value
            self.__header_list.append((name, "\"" + obfuscated_value + "\""))
        else:
            self.__header_list.append((name, "\"\""))
        self.__headers += "\""

    def set_body(self, body, content_type, charset=False):
        if charset is False:
            self.__body = LoggingUtil.obfuscate_body(body)
            self.__content_type = content_type
        else:  # possible dead code
            self.__body = LoggingUtil.obfuscate_body(body, charset)
            self.__content_type = content_type

    def empty_if_none(self, value):
        if value is not None:
            return value
        return ""

    def get_message(self):
        raise NotImplementedError

    def get_header_list(self):
        return self.__header_list
