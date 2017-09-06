from .api_exception import ApiException


class ValidationException(ApiException):
    """
    Represents an error response from the Ingenico ePayments platform when validation
    of requests failed.
    """
    def __init__(self, status_code, response_body, error_id, errors,
                 message="the Ingenico ePayments platform returned an incorrect "
                         "request error response"):
        super(ValidationException, self).__init__(status_code, response_body,
                                                  error_id, errors, message)
