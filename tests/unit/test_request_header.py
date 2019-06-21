import unittest

from ingenico.connect.sdk.request_header import RequestHeader, get_header, get_header_value


class RequestHeaderTest(unittest.TestCase):

    def test_get_header_value_none(self):
        """Tests get_header_value using None as headers"""
        self.assertIsNone(get_header_value(None, "Content-Length"))

    def test_get_header_value_list(self):
        """Tests get_header_value using a list of RequestHeader objects"""
        headers = [RequestHeader("Content-Type", "application/json")]
        self.assertEqual("application/json", get_header_value(headers, "Content-Type"))
        self.assertEqual("application/json", get_header_value(headers, "content-type"))
        self.assertIsNone(get_header_value(headers, "Content-Length"))

    def test_get_header_value_dict(self):
        """Tests get_header_value using a dictionary"""
        headers = {"Content-Type": "application/json"}
        self.assertEqual("application/json", get_header_value(headers, "Content-Type"))
        self.assertEqual("application/json", get_header_value(headers, "content-type"))
        self.assertIsNone(get_header_value(headers, "Content-Length"))

    def test_get_header_none(self):
        """Tests get_header using None as headers"""
        self.assertIsNone(get_header(None, "Content-Length"))

    def test_get_header_list(self):
        """Tests get_header using a list of RequestHeader objects"""
        headers = [RequestHeader("Content-Type", "application/json")]
        self.assertEqual("Content-Type:application/json", str(get_header(headers, "Content-Type")))
        self.assertEqual("Content-Type:application/json", str(get_header(headers, "content-type")))
        self.assertIsNone(get_header_value(headers, "Content-Length"))

    def test_get_header_dict(self):
        """Tests get_header using a dictionary"""
        headers = {"Content-Type": "application/json"}
        self.assertEqual("Content-Type:application/json", str(get_header(headers, "Content-Type")))
        self.assertEqual("Content-Type:application/json", str(get_header(headers, "content-type")))
        self.assertIsNone(get_header(headers, "Content-Length"))


if __name__ == '__main__':
    unittest.main()
