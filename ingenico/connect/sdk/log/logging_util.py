from .body_obfuscator import BodyObfuscator
from .header_obfuscator import HeaderObfuscator


class LoggingUtil:
    """
    A utility class to support logging.
    """

    def __init__(self):
        pass

    @staticmethod
    def obfuscate_body(body, charset=None):
        """
        Obfuscates the body from the given stream as necessary.

        Deprecated; Use BodyObfuscator instead

        :param body: The body to obfuscate, as string or bytes
        :param charset: The charset to use to read the body input stream.
        """
        return BodyObfuscator.default_body_obfuscator().obfuscate_body(body, charset)

    @staticmethod
    def obfuscate_header(name, value):
        """
        Obfuscates the value for the given header as necessary.

        Deprecated; Use HeaderObfuscator instead
        """
        return HeaderObfuscator.default_header_obfuscator().obfuscate_header(name, value)
