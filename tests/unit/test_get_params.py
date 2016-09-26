import unittest

from ingenico.connect.sdk.merchant.productgroups.get_productgroup_params import GetProductgroupParams
from ingenico.connect.sdk.merchant.products.get_product_params import GetProductParams
from tests.unit.comparable_param import ComparableParam


class GetProductParamsTest(unittest.TestCase):
    """Tests if instances of the GetProductParams class for products
    can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the GetProductParams object correctly functions when values are not set"""
        params = GetProductParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the GetProductParams object can correctly store and convert its data to RequestParameters"""
        params = GetProductParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the GetProductParams object"""
        params = GetProductParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)


class GetProductGroupParamsTest(unittest.TestCase):
    """Tests if instances of the GetProductgroupParams class for product groups
    can be correctly converted to RequestParameter objects
    """

    def test_empty_request_parameters(self):
        """Tests that the GetProductgroupParams object correctly functions when values are not set"""
        params = GetProductgroupParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the GetProductgroupParams object can correctly store and convert its data to RequestParameters"""
        params = GetProductgroupParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the GetProductgroupParams object"""
        params = GetProductgroupParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)

if __name__ == '__main__':
    unittest.main()
