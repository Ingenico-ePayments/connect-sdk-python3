import os
import unittest
import warnings
from urllib.parse import urlparse

from ingenico.connect.sdk.defaultimpl.authorization_type import AuthorizationType
from ingenico.connect.sdk.defaultimpl.default_authenticator import DefaultAuthenticator
from ingenico.connect.sdk.defaultimpl.default_connection import DefaultConnection
from ingenico.connect.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from ingenico.connect.sdk.factory import Factory
from tests.unit.test_default_connection import DefaultConnectionTest
from ingenico.connect.sdk.meta_data_provider import MetaDataProvider

PROPERTIES_URI = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.ini"))
API_KEY_ID = "someKey"
SECRET_API_KEY = "someSecret"


class FactoryTest(unittest.TestCase):
    """Tests that the factory is capable of correctly creating communicators and communicator configurations"""

    def test_create_configuration(self):
        """Tests that the factory is correctly able to create a communicator configuration"""
        configuration = Factory.create_configuration(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        self.assertEqual(urlparse("https://eu.sandbox.api-ingenico.com"), configuration.api_endpoint)
        self.assertEqual(AuthorizationType.get_authorization("v1HMAC"), configuration.authorization_type)
        self.assertEqual(-1, configuration.connect_timeout)
        self.assertEqual(-1, configuration.socket_timeout)
        self.assertEqual(100, configuration.max_connections)
        self.assertEqual(API_KEY_ID, configuration.api_key_id)
        self.assertEqual(SECRET_API_KEY, configuration.secret_api_key)
        self.assertIsNone(configuration.proxy_configuration)

    # noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
    def test_create_communicator(self):
        """Tests that the factory is correctly able to create a communicator"""
        communicator = Factory.create_communicator_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

        self.assertIs(communicator.marshaller, DefaultMarshaller.INSTANCE())

        session = communicator._Communicator__session
        connection = session.connection
        self.assertIsInstance(connection, DefaultConnection)
        DefaultConnectionTest.assertConnection(self, connection, None, None, 100, None)

        authenticator = session.authenticator
        self.assertIsInstance(authenticator, DefaultAuthenticator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertEqual(AuthorizationType.V1HMAC, authenticator._DefaultAuthenticator__authorization_type)
            self.assertEqual(API_KEY_ID, authenticator._DefaultAuthenticator__api_id_key)
            self.assertEqual(SECRET_API_KEY, authenticator._DefaultAuthenticator__secret_api_key)

        meta_data_provider = session.meta_data_provider
        self.assertIsInstance(meta_data_provider, MetaDataProvider)
        request_headers = meta_data_provider.meta_data_headers
        self.assertEqual(1, len(request_headers))
        self.assertEqual("X-GCS-ServerMetaInfo", request_headers[0].name)


if __name__ == '__main__':
    unittest.main()
