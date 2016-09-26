from .api_exception import ApiException


class GlobalCollectException(ApiException):
    """
    Represents an error response from the GlobalCollect platform when something
    went wrong at the GlobalCollect platform or further downstream.
    """

    def __init__(self, status_code, response_body, error_id, errors,
                 message="the GlobalCollect platform returned an error response"):
        super(GlobalCollectException, self).__init__(status_code, response_body,
                                                     error_id, errors, message)
