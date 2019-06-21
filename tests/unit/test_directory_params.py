import unittest

from ingenico.connect.sdk.merchant.products.directory_params import DirectoryParams
from tests.unit.comparable_param import ComparableParam


class DirectoryParamsTest(unittest.TestCase):
    """Tests if instances of the DirectoryParams class for products
    can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the DirectoryParams object correctly functions when values are not set"""
        params = DirectoryParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the DirectoryParams object can correctly store and convert its data to RequestParameters"""
        params = DirectoryParams()
        expected = []
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the GetParams object"""
        params = DirectoryParams()
        expected = []
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.country_code = None
        params.currency_code = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)


if __name__ == '__main__':
    unittest.main()
