import hmac
import hashlib
from base64 import b64encode

from .signature_validation_exception import SignatureValidationException


class SignatureValidator:
    """
    Validator for webhooks signatures.
    """

    def __init__(self, secret_key_store):
        if secret_key_store is None:
            raise ValueError("secret_key_store is required")
        self.__secret_key_store = secret_key_store

    def validate(self, body, request_headers):
        """
        Validates the given body using the given request headers.

        :raise: SignatureValidationException: If the body could not be validated successfully.
        """
        self.__validate_body(body, request_headers)

    def __validate_body(self, body, request_headers):
        signature = self.__get_header_value(request_headers, "X-GCS-Signature")
        key_id = self.__get_header_value(request_headers, "X-GCS-KeyId")
        secret_key = self.__secret_key_store.get_secret_key(key_id)
        unencoded_result = hmac.new(secret_key.encode("utf-8"), body, hashlib.sha256).digest()
        expected_signature = b64encode(unencoded_result)
        is_valid = hmac.compare_digest(signature.encode("utf-8"), expected_signature)
        if is_valid is False:
            raise SignatureValidationException("failed to validate signature: " + signature)

    @staticmethod
    def __get_header_value(request_headers, header_name):
        value = None
        for header in request_headers:
            if header_name.lower() == header.name.lower():
                if value is None:
                    value = header.value
                else:
                    raise SignatureValidationException("encountered multiple occurrences of header '" + header_name + "'")
        if value is None:
            raise SignatureValidationException("could not find header '" + header_name + "'")
        return value

    # Used for unit tests
    @property
    def secret_key_store(self):
        return self.__secret_key_store
