import os
import unittest

from ingenico.connect.sdk.log.logging_util import LoggingUtil
from tests import file_utils


class LoggingUtilTest(unittest.TestCase):
    """Tests if the log util is capable of obfuscating headers and bodies of requests"""

    def test_obfuscate_body_none_as_body(self):
        """Test that the obfuscate_body function can deal with a body = none and produce a result of none"""
        body = None

        obfuscated_body = LoggingUtil.obfuscate_body(body)
        self.assertIsNone(obfuscated_body)

    def test_obfuscate_body_empty(self):
        """Tests if the logging util is capable of obfuscating an empty body"""
        body = ""

        obfuscated_body = LoggingUtil.obfuscate_body(body)
        self.assertEqual("", obfuscated_body)

    def test_obfuscate_body_card(self):
        """Tests that the obfuscate_body correctly obfuscates a json containing payment card card data"""
        self.obfuscate_body_match("bodyWithCardOriginal.json",
                                  "bodyWithCardObfuscated.json")

    def test_obfuscate_body_iban(self):
        """Tests that the obfuscate_body correctly obfuscates a json containing an iban number"""
        self.obfuscate_body_match("bodyWithIbanOriginal.json",
                                  "bodyWithIbanObfuscated.json")

    def test_obfuscate_body_bin(self):
        """Tests that the obfuscate_body correctly obfuscates a json containing bin data"""
        self.obfuscate_body_match("bodyWithBinOriginal.json",
                                  "bodyWithBinObfuscated.json")

    def test_obfuscate_body_nothing(self):
        """Tests that the obfuscate_body function does not touch data that does not need to be obfuscated"""
        self.obfuscate_body_no_match("bodyNoObfuscation.json")

    def obfuscate_body_match(self, original_resource, obfuscated_resource):
        """Tests that the LoggingUtil obfuscates the json in original_resource to the json in obfuscated_resource

        original_resource is the path to a json file that contains one or more data entries to be obfuscated
        obfuscated_resource is the path to a json file containing the expected obfuscated json result of the obfuscation
        """
        body = _read_resource(original_resource)
        expected = _read_resource(obfuscated_resource)

        obfuscated_body = LoggingUtil.obfuscate_body(body)

        self.assertEqual(expected, obfuscated_body)

    def obfuscate_body_no_match(self, resource):
        """Tests that the LoggingUtil does not obfuscate the json given in the resource file

        resource is the path to a json file that contains no data that should be obfuscated
        """
        self.obfuscate_body_match(resource, resource)

    def test_obfuscate_header(self):
        """Tests that any authorization headers get obfuscated, while others do not"""
        self.obfuscate_header_match("Authorization",
                                    "Basic QWxhZGRpbjpPcGVuU2VzYW1l",
                                    "********")
        self.obfuscate_header_match("authorization",
                                    "Basic QWxhZGRpbjpPcGVuU2VzYW1l",
                                    "********")
        self.obfuscate_header_match("AUTHORIZATION",
                                    "Basic QWxhZGRpbjpPcGVuU2VzYW1l",
                                    "********")

        self.obfuscate_header_match("X-GCS-Authentication-Token", "foobar",
                                    "********")
        self.obfuscate_header_match("x-gcs-authentication-token", "foobar",
                                    "********")
        self.obfuscate_header_match("X-GCS-AUTHENTICATION-TOKEN", "foobar",
                                    "********")

        self.obfuscate_header_match("X-GCS-Callerpassword", "foobar",
                                    "********")
        self.obfuscate_header_match("x-gcs-callerpassword", "foobar",
                                    "********")
        self.obfuscate_header_match("X-GCS-CALLERPASSWORD", "foobar",
                                    "********")

        self.obfuscate_header_no_match("Content-Type", "application/json")
        self.obfuscate_header_no_match("content-type", "application/json")
        self.obfuscate_header_no_match("CONTENT-TYPE", "application/json")

    def obfuscate_header_match(self, name, original_value,
                               expected_obfuscated_value):
        """Tests that the obfuscator obfuscates the original_value to produce the expected_obfuscated_value"""
        obfuscated_value = LoggingUtil.obfuscate_header(name, original_value)
        self.assertEqual(expected_obfuscated_value, obfuscated_value)

    def obfuscate_header_no_match(self, name, original_value):
        """Tests that the obfuscator leaves the parameter header intact and does not obfuscate anything"""
        obfuscated_value = LoggingUtil.obfuscate_header(name, original_value)
        self.assertEqual(original_value, obfuscated_value)


# reads a file names file_name stored under resources/log
def _read_resource(file_name): return file_utils.read_file(
    os.path.join("log", file_name))


if __name__ == '__main__':
    unittest.main()
