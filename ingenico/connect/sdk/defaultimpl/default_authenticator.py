import hashlib
import hmac
from base64 import b64encode
from operator import attrgetter
from re import sub

from ingenico.connect.sdk.authenticator import Authenticator
from ingenico.connect.sdk.request_header import RequestHeader


class DefaultAuthenticator(Authenticator):
    """
    Default Authenticator implementation.
    """

    def __init__(self, authorization_type, api_id_key, secret_api_key):
        """
        :param authorization_type: Based on this value both the Ingenico ePayments
         platform and the merchant know which security implementation is used.
         A version number is used for backward compatibility in the future.
        :param api_id_key: An identifier for the secret API key. The api_key_id
         can be retrieved from the Configuration Center. This identifier is
         visible in the HTTP request and is also used to identify the correct
         account.
        :param secret_api_key: A shared secret. The shared secret can be
         retrieved from the Configuration Center. An api_key_id and
         secret_api_key always go hand-in-hand, the difference is that
         secret_api_key is never visible in the HTTP request. This secret is
         used as input for the HMAC algorithm.
        """
        Authenticator.__init__(self)
        if authorization_type is None:
            raise ValueError("authorization_type is required")
        if secret_api_key is None or not secret_api_key.strip():
            raise ValueError("secret_api_key is required")
        if api_id_key is None or not api_id_key.strip():
            raise ValueError("api_id_key is required")
        self.__authorization_type = authorization_type
        self.__api_id_key = api_id_key
        self.__secret_api_key = secret_api_key

    def create_simple_authentication_signature(self, http_method, resource_uri,
                                               http_headers):
        """Returns a v1HMAC authentication signature header"""
        if http_method is None or not http_method.strip():
            raise ValueError("http_method is required")
        if resource_uri is None:
            raise ValueError("resource_uri is required")
        data_to_sign = self.to_data_to_sign(http_method, resource_uri,
                                            http_headers)
        return "GCS " + self.__authorization_type + ":" + self.__api_id_key + \
               ":" + self.create_authentication_signature(data_to_sign)

    def to_data_to_sign(self, http_method, resource_uri, http_headers):
        content_type = None
        date = None
        canonicalized_headers = ""
        canonicalized_resource = self.__to_canonicalized_resource(resource_uri)
        xgcs_http_headers = []
        if http_headers is not None:
            for http_header in http_headers:
                if "Content-Type".lower() == http_header.name.lower():
                    content_type = http_header.value
                elif "Date".lower() == http_header.name.lower():
                    date = http_header.value
                else:
                    name = self.__to_canonicalize_header_name(http_header.name)
                    if name.startswith("x-gcs"):
                        value = self.to_canonicalize_header_value(
                            http_header.value)
                        xgcs_http_header = RequestHeader(name, value)
                        xgcs_http_headers.append(xgcs_http_header)
        xgcs_http_headers.sort(key=attrgetter('name'))
        for xgcs_http_header in xgcs_http_headers:
            canonicalized_headers += xgcs_http_header.name + ":" + xgcs_http_header.value + "\n"
        string = http_method.upper() + "\n"
        if content_type is not None:
            string += content_type + "\n"
        else:
            string += "\n"
        string += date + "\n"
        string += str(canonicalized_headers)
        string += canonicalized_resource + "\n"
        return str(string)

    def __to_canonicalized_resource(self, resource_uri):
        """
        Returns the encoded URI path without the HTTP method and including all
        decoded query parameters.
        """
        string = ""
        string += resource_uri.path
        if resource_uri.query:
            string += "?" + resource_uri.query
        return str(string)

    def __to_canonicalize_header_name(self, original_name):
        if original_name is None:
            return None
        else:
            return original_name.lower()

    def to_canonicalize_header_value(self, original_value):
        # For now V1HMAC is the only supported AuthorizationType so always use
        # the same logic.
        if original_value is None:
            return ""
        return sub(r"\r?\n(?:(?![\r\n])\s)*", " ", original_value).strip()

    def create_authentication_signature(self, data_to_sign):
        sig = hmac.new(self.__secret_api_key.encode("utf-8"), data_to_sign.encode("utf-8"),
                       hashlib.sha256)
        return b64encode(sig.digest()).decode("utf-8").rstrip('\n')
