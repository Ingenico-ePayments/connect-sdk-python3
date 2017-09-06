from ingenico.connect.sdk.log.logging_capable import LoggingCapable


# noinspection PyAbstractClass
class Connection(LoggingCapable):
    """
    Represents a connection to the Ingenico ePayments platform server.
    """

    def get(self, uri, request_headers):
        """
        Send a GET request to the Ingenico ePayments platform and return the response.

        :param uri: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :return: :class:`ingenico.connect.sdk.response.Response`
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError

    def delete(self, uri, request_headers):
        """
        Send a DELETE request to the Ingenico ePayments platform and return the response.

        :param uri: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :return: :class:`ingenico.connect.sdk.response.Response`
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError

    def post(self, uri, request_headers, body):
        """
        Send a POST request to the Ingenico ePayments platform and return the response.

        :param uri: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :param body: The optional body to send.
        :return: :class:`ingenico.connect.sdk.response.Response`
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError

    def put(self, uri, request_headers, body):
        """
        Send a PUT request to the Ingenico ePayments platform and return the response.

        :param uri: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :param body: The optional body to send.
        :return: :class:`ingenico.connect.sdk.response.Response`
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError
