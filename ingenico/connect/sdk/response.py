class Response(object):
    """
    Thrown when a response was received from the GlobalCollect platform which indicates an error.
    """
    def __init__(self, status_code, body, headers):
        self.__status_code = status_code
        self.__body = body
        if headers is not None:
            self.__headers = headers
        else:
            self.__headers = {}

    @property
    def status_code(self):
        """
        :return: The HTTP status code that was returned by the GlobalCollect
         platform.
        """
        return self.__status_code

    @property
    def body(self):
        """
        :return: The raw response body that was returned by the GlobalCollect
         platform.
        """
        return self.__body

    @property
    def headers(self):
        """
        :return: The headers that were returned by the GlobalCollect platform.
         Never None.
        """
        return self.__headers

    def get_header(self, header_name):
        """
        :return: The header with the given name, or None if there was no such
         header.
        """
        for name, value in self.__headers.items():
            if name.lower() == header_name.lower():
                return {name.lower: value}
        return None

    def get_header_value(self, header_name):
        """
        :return: The value header with the given name, or None if there was no
         such header.
        """
        for name, value in self.__headers.items():
            if name.lower() == header_name.lower():
                return value

    def __str__(self):
        string = Response.__name__ + "[status_code=" + str(
            self.__status_code)
        if self.__body is not None and len(self.__body) > 0:
            string += ",body='" + self.__body + "'"
        if self.__headers:
            string += ",headers=" + str(self.__headers)
        return str(string + "]")
