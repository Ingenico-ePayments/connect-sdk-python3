class ApiException(RuntimeError):
    """
    Represents an error response from the GlobalCollect platform which contains
    an ID and a list of errors.
    """

    def __init__(self, status_code, response_body, error_id, errors,
                 message="the GlobalCollect platform returned an error"
                         " response"):
        super(ApiException, self).__init__(message)
        self.__status_code = status_code
        self.__response_body = response_body
        self.__error_id = error_id
        if errors is None:
            self.__errors = ()
        else:
            self.__errors = errors

    @property
    def status_code(self):
        """
        :return: The HTTP status code that was returned by the GlobalCollect
         platform.
        """
        return self.__status_code

    @property
    def response_body(self):
        """
        :return: The raw response body that was returned by the GlobalCollect
         platform.
        """
        return self.__response_body

    @property
    def error_id(self):
        """
        :return: The error ID received from the GlobalCollect platform if
         available.
        """
        return self.__error_id

    @property
    def errors(self):
        """
        :return: The error list received from the GlobalCollect platform if
         available. Never None.
        """
        return self.__errors

    def __str__(self):
        string = super(ApiException, self).__str__()
        if self.__status_code > 0:
            string += "; status_code=" + str(self.__status_code)
        if self.__response_body is not None and len(self.__response_body) > 0:
            string += "; response_body='" + self.__response_body + "'"
        return str(string)
