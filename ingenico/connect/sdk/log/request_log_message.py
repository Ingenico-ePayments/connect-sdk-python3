from .body_obfuscator import BodyObfuscator
from .header_obfuscator import HeaderObfuscator
from .log_message import LogMessage


class RequestLogMessage(LogMessage):
    """
    A utility class to build request log messages.
    """

    def __init__(self, request_id, method, uri,
                 body_obfuscator=BodyObfuscator.default_body_obfuscator(),
                 header_obfuscator=HeaderObfuscator.default_header_obfuscator()):
        super(RequestLogMessage, self).__init__(request_id, body_obfuscator, header_obfuscator)
        self.method = method
        self.uri = uri

    def get_message(self):
        string = "Outgoing request (requestId='" + \
                 str(self.request_id) + "'):\n" + \
                 "  method:       " + \
                 self.empty_if_none("'" + self.method + "'") + "\n  uri:          " + \
                 self.empty_if_none("'" + self.uri + "'") + "\n  headers:      " + \
                 self.headers
        body = self.body
        if body is None:
            return string
        else:
            return string + "\n  content-type: '" + self.empty_if_none(self.content_type) + "'" + \
                   "\n  body:         '" + body + "'"
