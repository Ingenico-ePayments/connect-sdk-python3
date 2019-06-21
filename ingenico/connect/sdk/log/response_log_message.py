from ingenico.connect.sdk.log.log_message import \
    LogMessage


class ResponseLogMessage(LogMessage):
    """
    A utility class to build request log messages.
    """

    def __init__(self, request_id, status_code, duration=-1):
        super(ResponseLogMessage, self).__init__(request_id)
        self.__status_code = status_code
        if duration is False:
            self.__duration = -1
        else:
            self.__duration = duration

    def get_duration(self):
        return self.__duration

    def get_status_code(self):
        return self.__status_code

    def get_message(self):
        if self.__duration < 0:
            return "Incoming response (requestId='" + \
                   self.request_id + "'):\n" + \
                   "  status_code:  " + str(
                       self.__status_code) + "\n  headers:      " + \
                   self.headers + "\n  content-type: " + \
                   self.empty_if_none(
                       self.content_type) + "\n  body:         " + \
                   self.empty_if_none(self.body)

        else:
            return "Incoming response (requestId='" + \
                   self.request_id + "', " + str(self.__duration) + " ms):\n" + \
                   "  status_code:  " + \
                   str(self.__status_code) + "\n  headers:      " + \
                   self.headers + "\n  content-type: " + \
                   self.empty_if_none(
                       self.content_type) + "\n  body:         " + \
                   self.empty_if_none(self.body)
