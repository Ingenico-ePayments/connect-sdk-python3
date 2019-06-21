import hmac
from base64 import b64encode
import hashlib

from .api_version_mismatch_exception import ApiVersionMismatchException
from ingenico.connect.sdk.client import Client
from ingenico.connect.sdk.domain.webhooks.web_hooks_event import WebhooksEvent
from .signature_validation_exception import SignatureValidationException


class WebhooksHelper:
    """
    Ingenico ePayments platform webhooks helper.
    """

    def __init__(self, marshaller, secret_key_store):
        if marshaller is None:
            raise ValueError("marshaller is requried")
        if secret_key_store is None:
            raise ValueError("secret_key_store is required")
        self.__marshaller = marshaller
        self.__secret_key_store = secret_key_store

    # body as InputStream

    def unmarshal(self, body, request_headers):
        """
        Unmarshals the given body, while also validating it using the given request headers.
        @:raises SignatureValidationException: If the body could not be validated successfully.
        @:raises ApiVersionMismatchException: If the resulting event has an API
        version that this version of the SDK does not support.
        :return: The body unmarshalled as a WebhooksEvent.
        """
        self._validate(body, request_headers)
        event = self.__marshaller.unmarshal(body.decode("utf-8"), WebhooksEvent)
        self.__validate_api_version(event)
        return event

    def _validate(self, param, request_headers):
        """
        Validates the given body using the given request headers.
        :raises SignatureValidationException: If the body could not be validated
        successfully.
        """
        # if isinstance(param, str):
        #     self._validate(param.encode('UTF-8'), request_headers)
        # else:
        # try:
        self.__validate_body(param, request_headers)
        # except Exception as e:
        #     raise SignatureValidationException(e)

    # validation utility methods

    def __validate_body(self, body, request_headers):
        signature = self.__get_header_value(request_headers, "X-GCS-Signature")
        key_id = self.__get_header_value(request_headers, "X-GCS-KeyId")
        secret_key = self.__secret_key_store.get_secret_key(key_id)
        unencoded_result = hmac.new(secret_key.encode("utf-8"), body, hashlib.sha256)
        expected_signature = b64encode(unencoded_result.digest()).decode(
            "utf-8").rstrip('\n')
        is_valid = self.are_equal_signatures(signature, expected_signature)
        if is_valid is False:
            raise SignatureValidationException("failed to validate signature: "
                                               + signature + "'Expected: " + expected_signature + str(
                                                   len(signature)) + str(len(expected_signature)))

    @staticmethod
    def are_equal_signatures(signature, expected_signature):
        # don't use a simple equals call, as that may leak timing information
        # (it fails fast)
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

    # general utility methods

    def __validate_api_version(self, event):
        if not Client.API_VERSION() == event.api_version:
            raise ApiVersionMismatchException(event.api_version,
                                              Client.API_VERSION())

    def __get_header_value(self, request_headers, header_name):
        value = None
        for header in request_headers:
            if header_name.lower() == header.name.lower():
                if value is None:
                    value = header.value
                else:
                    raise SignatureValidationException(
                        "encountered multiple occurrences of header '"
                        + header_name + "'")
        if value is None:
            raise SignatureValidationException(
                "could not find header '" + header_name + "'")
        return value

    # Used for unit tests
    @property
    def marshaller(self):
        return self.__marshaller

    @property
    def secret_key_store(self):
        return self.__secret_key_store
