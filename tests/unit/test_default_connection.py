import unittest
import warnings

from ingenico.connect.sdk.communicator_configuration import CommunicatorConfiguration
from ingenico.connect.sdk.log.response_log_message import ResponseLogMessage
from ingenico.connect.sdk.log.sys_out_communicator_logger import SysOutCommunicatorLogger
from ingenico.connect.sdk.defaultimpl.default_connection import DefaultConnection
from ingenico.connect.sdk.proxy_configuration import ProxyConfiguration

CONNECT_TIMEOUT = 10
SOCKET_TIMEOUT = 20
MAX_CONNECTIONS = 100


# noinspection PyTypeChecker
class DefaultConnectionTest(unittest.TestCase):
    """Tests that a DefaultConnection can be constructed with a multitude of settings"""

    def test_log_unicode_2(self):
        """Tests if requests can be logged correctly"""
        logger = SysOutCommunicatorLogger()
        message = ResponseLogMessage(request_id="aaa",
                                     status_code=2345,
                                     duration=45.32)
        body = u"Schr\xf6der"
        content = "JSON"
        message.set_body(body, content)
        logger.log_response(message)

    def test_log_unicode(self):
        """Tests if requests can be logged correctly"""
        logger = SysOutCommunicatorLogger()
        message = ResponseLogMessage(request_id="aaa",
                                     status_code=2345,
                                     duration=45.32)
        body = u"Schr\u0e23\u0e16der"
        content = "JSON"
        message.set_body(body, content)
        logger.log_response(message)

    def test_construct_without_proxy(self):
        """Tests construction of a DefaultConnection without using a proxy"""
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)

        self.assertTimeouts(self, connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertMaxConnections(self, connection, CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS, None)
            self.assertNoProxy(self, connection)

    def test_construct_with_proxy_without_authentication(self):
        """Tests construction of a DefaultConnection with an unauthenticated proxy"""
        proxy_config = ProxyConfiguration.from_uri("http://test-proxy")

        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT, proxy_configuration=proxy_config)

        self.assertTimeouts(self, connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertMaxConnections(self, connection,
                                      CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS, proxy_config)
            self.assertProxy(self, connection, proxy_config)

    def test_construct_with_proxy_with_authentication(self):
        """Tests construction of a DefaultConnection with an authenticated proxy"""
        proxy_config = ProxyConfiguration.from_uri("http://test-proxy", "test-username", "test-password")

        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT, proxy_configuration=proxy_config)

        self.assertTimeouts(self, connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertMaxConnections(self, connection,
                                      CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS, proxy_config)
            self.assertProxy(self, connection, proxy_config)

    def test_construct_with_max_connections_without_proxy(self):
        """Tests construction of a DefaultConnection with a different amount of max connections and no proxy"""
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT, MAX_CONNECTIONS)

        self.assertTimeouts(self, connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertMaxConnections(self, connection, MAX_CONNECTIONS, None)
            self.assertNoProxy(self, connection)

    def test_construct_with_max_connections_with_proxy(self):
        """Tests construction of a DefaultConnection
        with a different amount of max connections and an unauthenticated proxy
        """
        proxy_config = ProxyConfiguration.from_uri("http://test-proxy")

        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT,
                                       MAX_CONNECTIONS, proxy_configuration=proxy_config)

        self.assertTimeouts(self, connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertMaxConnections(self, connection, MAX_CONNECTIONS, proxy_config)
            self.assertProxy(self, connection, proxy_config)

    @staticmethod
    def assertNoProxy(test_instance, default_connection):
        """Asserts that the default_connection does not have any proxy settings contained within"""
        test_instance.assertFalse(default_connection._DefaultConnection__requests_session.proxies)

    @staticmethod
    def assertProxy(test_instance, connection, proxy_configuration):
        """Asserts that the proxy data inside the connection is consistent with the data in proxy_configuration"""
        test_instance.assertIn(str(proxy_configuration),
                               list(connection._DefaultConnection__requests_session.proxies.values()))

    @staticmethod
    def assertConnection(test_instance, default_connection, connect_timeout, socket_timeout,
                         max_connections, proxy_configuration=None):
        """Asserts that the default_connection parameter has properties conform
        the connect_timeout, the socket_timeout, max_connections and the proxy_configuration
        """
        DefaultConnectionTest.assertTimeouts(test_instance, default_connection, connect_timeout, socket_timeout)
        DefaultConnectionTest.assertMaxConnections(test_instance, default_connection, max_connections,
                                                   proxy_configuration)
        if proxy_configuration is not None:
            DefaultConnectionTest.assertProxy(test_instance, default_connection, proxy_configuration)
        else:
            DefaultConnectionTest.assertNoProxy(test_instance, default_connection)

    @staticmethod
    def assertTimeouts(test_instance, connection, connection_timeout, socket_timeout):
        """Asserts that the settings in the request config of the connection have the proper timeout settings"""
        test_instance.assertEqual(connection_timeout, connection.connect_timeout)
        test_instance.assertEqual(socket_timeout, connection.socket_timeout)

    @staticmethod
    def assertMaxConnections(test_instance, connection, max_connections, proxy_configuration):
        """Asserts that the connection has the correct setting for max_connections and proxy_configuration"""
        requests_session = connection._DefaultConnection__requests_session
        try:
            http_poolsize = requests_session.get_adapter("http://")._pool_maxsize
            https_poolsize = requests_session.get_adapter("https://")._pool_maxsize
            test_instance.assertEqual(http_poolsize,
                                      https_poolsize)  # requests stores its poolsize as a per-host variable
        except Exception as e:
            if isinstance(e, AssertionError):
                raise e
            else:
                print("Could not access max_connections attribute in libary for validation")

        # proxy settings are deeply embedded in requests, we don't check them here


if __name__ == '__main__':
    unittest.main()
