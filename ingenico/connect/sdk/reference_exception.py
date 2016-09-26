from .api_exception import ApiException


class ReferenceException(ApiException):
    """
    Represents an error response from the GlobalCollect platform when a
    non-existing or removed object is trying to be accessed.
    """

    def __init__(self, status_code, response_body, error_id, errors,
                 message="the GlobalCollect platform returned a "
                         "reference error response"):
        super(ReferenceException, self).__init__(status_code, response_body,
                                                 error_id, errors, message)
