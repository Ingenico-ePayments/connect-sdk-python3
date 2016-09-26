import unittest
import tests.integration.init_utils as init_utils
from ingenico.connect.sdk.request_header import RequestHeader
from tests.integration.init_utils import MERCHANT_ID
from ingenico.connect.sdk.merchant.products.directory_params import DirectoryParams
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.meta_data_provider import MetaDataProvider


class MultiLineHeaderTest(unittest.TestCase):
    """Test if the products service can function with a multiline header"""
    def test_multiline_header(self):
        """Test if the products service can function with a multiline header"""
        multi_line_header = " some value  \r\n \n with        a liberal amount     of \r\n  spaces    "
        configuration = init_utils.create_communicator_configuration()
        meta_data_provider = MetaDataProvider(integrator="Ingenico",
                                              additional_request_headers=(RequestHeader("X-GCS-MultiLineHeader", multi_line_header), ))
        params = DirectoryParams()
        params.country_code = "NL"
        params.currency_code = "EUR"
        session = Factory.create_session_from_configuration(configuration, meta_data_provider=meta_data_provider)

        with Factory.create_client_from_session(session) as client:
            response = client.merchant(MERCHANT_ID).products().directory(809, params)

        self.assertGreater(len(response.entries), 0)


if __name__ == '__main__':
    unittest.main()
