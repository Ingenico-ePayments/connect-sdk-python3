from .signature_validation_exception import SignatureValidationException


class SecretKeyNotAvailableException(SignatureValidationException):
    """
    Represents an error that causes a secret key to not be available.
    """

    def __init__(self, param1, param2, cause=False):
        if cause is False:
            if isinstance(param2, str):
                super(SecretKeyNotAvailableException, self).__init__(param1)
                self.__key_id = param2
            else:
                super(SecretKeyNotAvailableException, self).__init__(param2)
                self.__key_id = param1
        else:
            super(SecretKeyNotAvailableException, self).__init__(param1, cause)
            self.__key_id = param2

    @property
    def key_id(self):
        return self.__key_id
