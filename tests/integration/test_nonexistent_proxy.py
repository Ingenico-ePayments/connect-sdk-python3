import unittest
import configparser
import tests.integration.init_utils as init_utils
from ingenico.connect.sdk.communication_exception import CommunicationException
from ingenico.connect.sdk.communicator_configuration import CommunicatorConfiguration
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.proxy_configuration import ProxyConfiguration
from tests.integration.init_utils import MERCHANT_ID


class ProxyTest(unittest.TestCase):
    def test_connect_nonexistent_proxy(self):
        """Try connecting to a nonexistent proxy and assert it fails to connect to it"""
        parser = configparser.ConfigParser()
        parser.read(init_utils.PROPERTIES_URL_PROXY)
        communicator_config = CommunicatorConfiguration(parser, connect_timeout=1, socket_timeout=1,
                                                        api_key_id=init_utils.API_KEY_ID,
                                                        secret_api_key=init_utils.SECRET_API_KEY,
                                                        proxy_configuration=ProxyConfiguration(
                                                            host="localhost", port=65535,
                                                            username="arg", password="blarg")
                                                        )
        with Factory.create_client_from_configuration(communicator_config) as client:
            with self.assertRaises(CommunicationException):
                client.merchant(MERCHANT_ID).services().testconnection()


if __name__ == '__main__':
    unittest.main()
