from .api_exception import ApiException


class AuthorizationException(ApiException):
    """
    Represents an error response from the GlobalCollect platform when
    authorization failed.
    """

    def __init__(self, status_code, response_body, error_id, errors,
                 message="the GlobalCollect platform returned an authorization error response"):
        super(AuthorizationException, self).__init__(status_code, response_body,
                                                     error_id, errors, message)
