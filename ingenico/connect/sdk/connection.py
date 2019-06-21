from ingenico.connect.sdk.log.logging_capable import LoggingCapable


# noinspection PyAbstractClass
class Connection(LoggingCapable):
    """
    Represents a connection to the Ingenico ePayments platform server.
    """

    def get(self, url, request_headers):
        """
        Send a GET request to the Ingenico ePayments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :return: The response from the Ingenico ePayments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError

    def delete(self, url, request_headers):
        """
        Send a DELETE request to the Ingenico ePayments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :return: The response from the Ingenico ePayments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError

    def post(self, url, request_headers, body):
        """
        Send a POST request to the Ingenico ePayments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :param body: The optional body to send.
        :return: The response from the Ingenico ePayments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError

    def put(self, url, request_headers, body):
        """
        Send a PUT request to the Ingenico ePayments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional list of request headers.
        :param body: The optional body to send.
        :return: The response from the Ingenico ePayments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise: CommunicationException when an exception occurred communicating
         with the Ingenico ePayments platform
        """
        raise NotImplementedError
