import os
import unittest

from ingenico.connect.sdk.log.header_obfuscator import HeaderObfuscator
from ingenico.connect.sdk.log.obfuscation_rule import obfuscate_all
from tests import file_utils


class HeaderObfuscatorTest(unittest.TestCase):
    """Tests if the header obfuscator is capable of obfuscating headers of requests"""

    def test_obfuscate_header(self):
        """Tests that any default headers get obfuscated, while others do not"""
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

    def test_obfuscate_custom_header(self):
        """Tests that any default and custom headers get obfuscated"""
        header_obfuscator = HeaderObfuscator(additional_rules={
            "content-type": obfuscate_all()
        })

        self.obfuscate_header_match("Authorization", "Basic QWxhZGRpbjpPcGVuU2VzYW1l", "********",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("authorization", "Basic QWxhZGRpbjpPcGVuU2VzYW1l", "********",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("AUTHORIZATION", "Basic QWxhZGRpbjpPcGVuU2VzYW1l", "********",
                                    header_obfuscator=header_obfuscator)

        self.obfuscate_header_match("X-GCS-Authentication-Token", "foobar", "********",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("x-gcs-authentication-token", "foobar", "********",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("X-GCS-AUTHENTICATION-TOKEN", "foobar", "********",
                                    header_obfuscator=header_obfuscator)

        self.obfuscate_header_match("X-GCS-Callerpassword", "foobar", "********",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("x-gcs-callerpassword", "foobar", "********",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("X-GCS-CALLERPASSWORD", "foobar", "********",
                                    header_obfuscator=header_obfuscator)

        self.obfuscate_header_match("Content-Type", "application/json", "****************",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("content-type", "application/json", "****************",
                                    header_obfuscator=header_obfuscator)
        self.obfuscate_header_match("CONTENT-TYPE", "application/json", "****************",
                                    header_obfuscator=header_obfuscator)

    def obfuscate_header_match(self, name, original_value,
                               expected_obfuscated_value,
                               header_obfuscator=HeaderObfuscator.default_header_obfuscator()):
        """Tests that the obfuscator obfuscates the original_value to produce the expected_obfuscated_value"""
        obfuscated_value = header_obfuscator.obfuscate_header(name, original_value)
        self.assertEqual(expected_obfuscated_value, obfuscated_value)

    def obfuscate_header_no_match(self, name, original_value):
        """Tests that the obfuscator leaves the parameter header intact and does not obfuscate anything"""
        obfuscated_value = HeaderObfuscator.default_header_obfuscator().obfuscate_header(name, original_value)
        self.assertEqual(original_value, obfuscated_value)


# reads a file names file_name stored under resources/log
def _read_resource(file_name): return file_utils.read_file(
    os.path.join("log", file_name))


if __name__ == '__main__':
    unittest.main()
