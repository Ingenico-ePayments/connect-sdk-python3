import unittest
import urllib.parse

from ingenico.connect.sdk.defaultimpl.authorization_type import AuthorizationType
from ingenico.connect.sdk.defaultimpl.default_authenticator import DefaultAuthenticator
from ingenico.connect.sdk.request_header import RequestHeader


class DefaultAuthenticatorTest(unittest.TestCase):
    """Tests that the DefaultAuthenticator is capable of converting a set of request headers to a POST request
    and that it is capable of providing the correct signature"""

    def test_canonicalized_header_value(self):
        """Tests that the to_canonicalize_header function correctly removes control characters and excessive whitespace
        """
        authenticator = DefaultAuthenticator(AuthorizationType.get_authorization("v1HMAC"), "apiKeyId", "secretApiKey")

        self.assertEqual("aap noot", authenticator.to_canonicalize_header_value("aap\nnoot  "))
        self.assertEqual("aap noot", authenticator.to_canonicalize_header_value(" aap\r\n  noot"))

    def test_to_data_to_sign(self):
        """Tests that the to_data_to_sign function correctly constructs a POST request for multiple headers"""
        authenticator = DefaultAuthenticator(AuthorizationType.get_authorization("v1HMAC"), "apiKeyId", "secretApiKey")
        http_headers = [RequestHeader("X-GCS-ServerMetaInfo",
                                      "{\"platformIdentifier\":\"Windows 7/6.1 Java/1.7 (Oracle Corporation; "
                                      "Java HotSpot(TM) 64-Bit Server VM; 1.7.0_45)\",\"sdkIdentifier\":\"1.0\"}"),
                        RequestHeader("Content-Type", "application/json"),
                        RequestHeader("X-GCS-ClientMetaInfo", "{\"aap\",\"noot\"}"),
                        RequestHeader("User-Agent", "Apache-HttpClient/4.3.4 (java 1.5)"),
                        RequestHeader("Date", "Mon, 07 Jul 2014 12:12:40 GMT")]
        expected_start = "POST\n" \
                         "application/json\n"
        expected_end = "x-gcs-clientmetainfo:{\"aap\",\"noot\"}\n" \
                       "x-gcs-servermetainfo:{\"platformIdentifier\":\"Windows 7/6.1 Java/1.7 " \
                       "(Oracle Corporation; Java HotSpot(TM) 64-Bit Server VM; 1.7.0_45)\"," \
                       "\"sdkIdentifier\":\"1.0\"}\n" \
                       "/v1/9991/services%20bla/convert/amount?aap=noot&mies=geen%20noot\n"

        data_to_sign = authenticator.to_data_to_sign("POST",
            urllib.parse.urlparse("http://localhost:8080/v1/9991/services%20bla/convert/amount?aap=noot&mies=geen%20noot"),
            http_headers)

        actual_start = data_to_sign[:22]
        actual_end = data_to_sign[52:]
        self.assertEqual(expected_start, actual_start)
        self.assertEqual(expected_end, actual_end)

    def test_create_authentication_signature(self):
        """Tests if the default authenticator creates the correct signature"""
        authenticator = DefaultAuthenticator(AuthorizationType.get_authorization("v1HMAC"), "apiKeyId", "secretApiKey")
        data_to_sign = "DELETE\n" \
                       "application/json\n" \
                       "Fri, 06 Jun 2014 13:39:43 GMT\n" \
                       "x-gcs-clientmetainfo:processed header value\n" \
                       "x-gcs-customerheader:processed header value\n" \
                       "x-gcs-servermetainfo:processed header value\n" \
                       "/v1/9991/tokens/123456789\n"

        authentication_signature = authenticator.create_authentication_signature(data_to_sign)

        self.assertEqual("VfnXpPBQQoHZivTcAg0JvOWkhnzlPnaCPKpTQn/uMJM=", authentication_signature)

    def test_create_authentication_signature_2(self):
        """Tests if the default authenticator creates the correct signature"""
        authenticator = DefaultAuthenticator(AuthorizationType.get_authorization("v1HMAC"), "apiKeyId", "6Kj5HT0MQKC6D8eb7W3lTg71kVKVDSt1")
        data_to_sign = "GET\n" \
                       "\n" \
                       "Fri, 06 Jun 2014 13:39:43 GMT\n" \
                       "/v1/9991/tokens/123456789\n"

        authentication_signature = authenticator.create_authentication_signature(data_to_sign)

        self.assertEqual("9ond5EIN05dBXJGCLRK5om9pxHsyrh/12pZJ7bvmwNM=", authentication_signature)


if __name__ == '__main__':
    unittest.main()
