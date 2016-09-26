import base64
import unittest
from datetime import timedelta

from unittest.mock import Mock, MagicMock

from ingenico.connect.sdk.connection import Connection
from ingenico.connect.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.pooled_connection import PooledConnection
from ingenico.connect.sdk.request_header import RequestHeader
from tests.unit.test_factory import PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY


class ClientTest(unittest.TestCase):
    """Tests for the Client class that test if
    the function Client.with_client_meta_info correctly returns a client that is only modified if necessary.
    Also contains tests testing if connection settings are propagated properly to the connection object
    """

    def test_with_client_meta_info(self):
        """Tests if the function withClientMetaInfo alters a client when it needs to and does nothing if not required"""

        client1 = Factory.create_client_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        # client2 = client1.with_client_meta_info(None)
        client2 = client1.with_client_meta_info(None)
        client_meta_info = DefaultMarshaller.INSTANCE().marshal({"test": "test"})
        client3 = client1.with_client_meta_info(client_meta_info)
        client4 = client3.with_client_meta_info(client_meta_info)
        client5 = client3.with_client_meta_info(None)

        self.assertIsNone(client1._client_headers)
        self.assertIs(client1, client2)
        self.assertIsNot(client1, client3)
        self.assertClientHeaders(client3, client_meta_info)
        self.assertIs(client3, client4)
        self.assertIsNot(client3, client5)
        self.assertIsNone(client5._client_headers)

    def assertClientHeaders(self, client, client_meta_info):
        """Checks that the 'ClientMetaInfo' header with client_meta_info is stored properly in the client"""
        headers = client._client_headers
        header_value = base64.b64encode(client_meta_info.encode("utf-8"))
        expected = RequestHeader("X-GCS-ClientMetaInfo", header_value)
        found = False
        for header in headers:
            if str(expected) == str(header):
                found = True
        self.assertTrue(found, "header {0} was not found in {1}".format(expected, headers))

    def test_close_idle_connection_not_pooled(self):
        """Tests that the setting to close an idle connection in a client propagates to the connection
        for an unpooled connection
        """
        mock = MagicMock(spec=Connection(), autospec=True)
        function_mock = Mock(name="close_idle_connections_mock")
        mock.attach_mock(function_mock, "close_idle_connections")
        session = Factory.create_session_from_file(
            configuration_file_name=PROPERTIES_URI, connection=mock,
            api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY)
        client = Factory.create_client_from_session(session)

        client.close_idle_connections(timedelta(seconds=5))  # seconds

        function_mock.assert_not_called()

    def test_close_idle_connection_pooled(self):
        """Tests that the setting to close an idle connection in a client propagates to the connection
            for a pooled connection
            """
        pooled_mock = MagicMock(spec=PooledConnection(), autospec=True)
        function_mock = Mock(name="close_idle_connections_mock")
        pooled_mock.attach_mock(function_mock, "close_idle_connections")
        session = Factory.create_session_from_file(
            configuration_file_name=PROPERTIES_URI, connection=pooled_mock,
            api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY)
        client = Factory.create_client_from_session(session)

        client.close_idle_connections(timedelta(seconds=5))  #seconds

        function_mock.assert_called_once_with(timedelta(seconds=5))

    def test_close_expired_connections_not_pooled(self):
        """Tests that the setting to close an expired connection in a client propagates to the connection
        for an unpooled connection
        """
        mock = MagicMock(spec=Connection(), autospec=True)
        function_mock = Mock(name="close_expired_connections_mock")
        mock.attach_mock(function_mock, "close_expired_connections")
        session = Factory.create_session_from_file(
            configuration_file_name=PROPERTIES_URI,
            api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY, connection=mock)
        client = Factory.create_client_from_session(session)

        client.close_expired_connections()

        function_mock.assert_not_called()

    def test_close_expired_connections_pooled(self):
        """Tests that the setting to close an expired connection in a client propagates to the connection
        for a pooled connection
        """
        pooled_mock = MagicMock(spec=PooledConnection(), autospec=True)
        function_mock = Mock(name="close_expired_connections_mock")
        pooled_mock.attach_mock(function_mock, "close_expired_connections")
        session = Factory.create_session_from_file(
            configuration_file_name=PROPERTIES_URI, connection=pooled_mock,
            api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY)
        client = Factory.create_client_from_session(session)

        client.close_expired_connections()

        function_mock.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
