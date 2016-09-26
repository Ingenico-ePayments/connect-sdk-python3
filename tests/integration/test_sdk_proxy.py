import unittest

from ingenico.connect.sdk.merchant.services.convert_amount_params import ConvertAmountParams
from ingenico.connect.sdk.merchant.services.services_client import ServicesClient
from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID


class SDKProxyTest(unittest.TestCase):
    def test_sdk_proxy(self):
        request = ConvertAmountParams()
        request.amount = 123
        request.source = "USD"
        request.target = "EUR"

        with init_utils.create_client_with_proxy() as client:
            services = client.merchant(MERCHANT_ID).services()
            services.convertAmount(request)

            self.assertIsInstance(services, ServicesClient)

if __name__ == '__main__':
    unittest.main()
