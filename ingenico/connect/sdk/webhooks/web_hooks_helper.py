from .api_version_mismatch_exception import ApiVersionMismatchException
from .signature_validator import SignatureValidator
from ingenico.connect.sdk.client import Client
from ingenico.connect.sdk.domain.webhooks.web_hooks_event import WebhooksEvent


class WebhooksHelper:
    """
    Ingenico ePayments platform webhooks helper.
    """

    def __init__(self, marshaller, secret_key_store):
        if marshaller is None:
            raise ValueError("marshaller is requried")
        self.__marshaller = marshaller
        self.__signature_validator = SignatureValidator(secret_key_store)

    def unmarshal(self, body, request_headers):
        """
        Unmarshals the given body, while also validating it using the given request headers.

        :raise: SignatureValidationException: If the body could not be validated successfully.
        :raise: ApiVersionMismatchException: If the resulting event has an API
         version that this version of the SDK does not support.
        :return: The body unmarshalled as a WebhooksEvent.
        """
        self._validate(body, request_headers)
        event = self.__marshaller.unmarshal(body.decode("utf-8"), WebhooksEvent)
        self.__validate_api_version(event)
        return event

    def _validate(self, body, request_headers):
        """
        Validates the given body using the given request headers.

        :raise: SignatureValidationException: If the body could not be validated successfully.
        """
        self.__signature_validator.validate(body, request_headers)

    @staticmethod
    def are_equal_signatures(signature, expected_signature):
        """
        Deprecated; use hmac.compare_digest instead
        """
        # don't use a simple equals call, as that may leak timing information (it fails fast)
        length = len(signature)
        expected_length = len(expected_signature)

        # always check at least 256 characters, to also not leak timing
        # information about the length of the expected signature
        limit = max(max(length, expected_length), 256)

        result = True

        # the loop below uses result &= false instead of result = false and
        # result &= true instead of nothing because those might leak timing
        # information
        for i in range(0, limit):
            if i < length and i < expected_length:
                # both within string boundaries
                result = result and (signature[i] == expected_signature[i])
            elif i >= length and i >= expected_length:
                # past both string boundaries
                result = result and True
            else:
                # i >= length || i >= expected_length but not both
                result = result and False

        return result

    @staticmethod
    def __validate_api_version(event):
        if not Client.API_VERSION() == event.api_version:
            raise ApiVersionMismatchException(event.api_version, Client.API_VERSION())

    # Used for unit tests
    @property
    def marshaller(self):
        return self.__marshaller

    @property
    def secret_key_store(self):
        return self.__signature_validator.secret_key_store
