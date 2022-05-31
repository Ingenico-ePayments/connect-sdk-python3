import os
import unittest

from ingenico.connect.sdk.log.body_obfuscator import BodyObfuscator
from tests import file_utils


class BodyObfuscatorTest(unittest.TestCase):
    """Tests if the body obfuscator is capable of obfuscating bodies of requests"""

    def test_obfuscate_body_none_as_body(self):
        """Test that the obfuscate_body function can deal with a body = none and produce a result of none"""
        body = None

        obfuscated_body = BodyObfuscator.default_body_obfuscator().obfuscate_body(body)
        self.assertIsNone(obfuscated_body)

    def test_obfuscate_body_empty(self):
        """Tests if the logging util is capable of obfuscating an empty body"""
        body = ""

        obfuscated_body = BodyObfuscator.default_body_obfuscator().obfuscate_body(body)
        self.assertEqual("", obfuscated_body)

    def test_obfuscate_body_card(self):
        """Tests that the obfuscate_body correctly obfuscates a json containing payment card card data"""
        self.obfuscate_body_match("bodyWithCardOriginal.json",
                                  "bodyWithCardObfuscated.json")

    def test_obfuscate_body_card_custom_rule(self):
        """Tests that the obfuscate_body correctly obfuscates a json containing payment card card data with a custom rule"""
        def obfuscate_custom(value):
            start = 6
            end = len(value) - 4
            value_between = '*' * (end - start)
            return value[:start] + value_between + value[end:]

        body_obfuscator = BodyObfuscator(additional_rules={
            "card": obfuscate_custom
        })
        self.obfuscate_body_match("bodyWithCardOriginal.json",
                                  "bodyWithCardObfuscated.json",
                                  body_obfuscator=body_obfuscator)

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

    def test_obfuscate_body_object(self):
        """Tests that the obfuscate_body correctly obfuscates a json containing an object that does not need to be obfuscated"""
        self.obfuscate_body_match("bodyWithObjectOriginal.json",
                                  "bodyWithObjectObfuscated.json")

    def obfuscate_body_match(self, original_resource, obfuscated_resource, body_obfuscator=BodyObfuscator.default_body_obfuscator()):
        """Tests that the LoggingUtil obfuscates the json in original_resource to the json in obfuscated_resource

        original_resource is the path to a json file that contains one or more data entries to be obfuscated
        obfuscated_resource is the path to a json file containing the expected obfuscated json result of the obfuscation
        """
        body = _read_resource(original_resource)
        expected = _read_resource(obfuscated_resource)

        obfuscated_body = body_obfuscator.obfuscate_body(body)

        self.assertEqual(expected, obfuscated_body)

    def obfuscate_body_no_match(self, resource):
        """Tests that the LoggingUtil does not obfuscate the json given in the resource file

        resource is the path to a json file that contains no data that should be obfuscated
        """
        self.obfuscate_body_match(resource, resource)


# reads a file names file_name stored under resources/log
def _read_resource(file_name): return file_utils.read_file(
    os.path.join("log", file_name))


if __name__ == '__main__':
    unittest.main()
