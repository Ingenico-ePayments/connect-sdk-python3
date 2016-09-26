class ResponseException(RuntimeError):
    """
    Thrown when a response was received from the GlobalCollect platform which
    indicates an error.
    """

    def __init__(self, response):
        super(ResponseException, self).__init__(
            "the GlobalCollect platform returned an error response")
        self.__response = response

    @property
    def response(self):
        """
        :return: The response that was returned by the GlobalCollect platform.
        """
        return self.__response

    @property
    def status_code(self):
        """
        :return: The HTTP status code that was returned by the GlobalCollect
         platform.
        """
        return self.__response.status_code

    @property
    def body(self):
        """
        :return: The raw response body that was returned by the GlobalCollect
         platform.
        """
        return self.__response.body

    @property
    def headers(self):
        """
        :return: The headers that were returned by the GlobalCollect platform.
         Never None.
        """
        return self.__response.headers

    def get_header(self, header_name):
        """
        :return: The header with the given name, or None if there was no such
         header.
        """
        return self.__response.get_header(header_name)

    def get_header_value(self, header_name):
        """
        :return: The value header with the given name, or None if there was no
         such header.
        """
        return self.__response.get_header_value(header_name)

    def __str__(self):
        string = super(ResponseException, self).__str__()
        status_code = self.__response.status_code
        if status_code > 0:
            string += "; status_code=" + str(status_code)
        response_body = self.__response.body
        if response_body is not None and len(response_body) > 0:
            string += "; response_body='" + response_body + "'"
        return str(string)
