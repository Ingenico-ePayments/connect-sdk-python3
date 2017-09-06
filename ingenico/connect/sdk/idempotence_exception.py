from .api_exception import ApiException


class IdempotenceException(ApiException):
    """
    Represents an error response from the Ingenico ePayments platform when an
    idempotent request failed because the first request has not finished yet.
    """

    def __init__(self, idempotence_key, idempotence_request_timestamp,
                 status_code, response_body, error_id, errors,
                 message="the Ingenico ePayments platform returned a duplicate request error response"):
        super(IdempotenceException, self).__init__(status_code, response_body,
                                                   error_id, errors, message)
        self.__idempotence_key = idempotence_key
        self.__idempotence_request_timestamp = idempotence_request_timestamp

    @property
    def idempotence_key(self):
        """
        :return: The key that was used for the idempotent request.
        """
        return self.__idempotence_key

    @property
    def idempotence_request_timestamp(self):
        """
        :return: The request timestamp of the first idempotent request with the
         same key.
        """
        return self.__idempotence_request_timestamp
