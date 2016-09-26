import unittest

from ingenico.connect.sdk.merchant.tokens.delete_token_params import DeleteTokenParams
from tests.unit.comparable_param import ComparableParam


class DeleteTokenParamsTest(unittest.TestCase):
    """Tests if instances of the DeleteTokenParams class for products
    can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the DeleteTokenParams object correctly functions when values are not set"""
        params = DeleteTokenParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the DeleteTokenParams object can correctly store and convert its data to RequestParameters"""
        params = DeleteTokenParams()
        expected = []
        params.mandate_cancel_date = "20160610"
        expected.append(ComparableParam("mandateCancelDate", "20160610"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the DeleteTokenParams object"""
        params = DeleteTokenParams()
        expected = []
        params.mandate_cancel_date = "20160610"
        params.mandate_cancel_date = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)

if __name__ == '__main__':
    unittest.main()
