import unittest

from ingenico.connect.sdk.merchant.products.directory_params import DirectoryParams
from ingenico.connect.sdk.merchant.products.find_products_params import FindProductsParams
from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID


class PaymentProductTest(unittest.TestCase):
    """Test if products function"""
    def test_payment_products(self):
        """Test if products function"""
        params = FindProductsParams()
        params.country_code = "NL"
        params.currency_code = "EUR"

        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).products().find(params)
        self.assertGreater(len(response.payment_products), 0)

    """Test if product directories function"""
    def test_payment_product_directories(self):
        """Test if product directories function"""
        params = DirectoryParams()
        params.country_code = "NL"
        params.currency_code = "EUR"

        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).products().directory(809, params)
        self.assertGreater(len(response.entries), 0)


if __name__ == '__main__':
    unittest.main()
