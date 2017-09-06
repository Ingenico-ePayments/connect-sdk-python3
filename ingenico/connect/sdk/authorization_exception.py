from .api_exception import ApiException


class AuthorizationException(ApiException):
    """
    Represents an error response from the Ingenico ePayments platform when
    authorization failed.
    """

    def __init__(self, status_code, response_body, error_id, errors,
                 message="the Ingenico ePayments platform returned an authorization error response"):
        super(AuthorizationException, self).__init__(status_code, response_body,
                                                     error_id, errors, message)
