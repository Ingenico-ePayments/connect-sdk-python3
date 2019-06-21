import unittest
import tests.integration.init_utils as init_utils
from tests.integration.init_utils import MERCHANT_ID
from ingenico.connect.sdk.merchant.services.convert_amount_params import ConvertAmountParams


class ConvertAmountTest(unittest.TestCase):
    """Test if the convert amount service can connect to the server"""

    def test_convert_amount(self):
        """Test if the convert amount service can connect to the server"""
        request = ConvertAmountParams()
        request.amount = 123
        request.source = "USD"
        request.target = "EUR"

        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).services().convert_amount(request)
        # actual convert amount may vary due to changing rates, so simply check if there is an amount
        self.assertIsNotNone(response.converted_amount)
        self.assertGreater(int(response.converted_amount), 0)


if __name__ == '__main__':
    unittest.main()
