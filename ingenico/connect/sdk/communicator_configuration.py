from .endpoint_configuration import EndpointConfiguration
from ingenico.connect.sdk.defaultimpl.authorization_type import \
    AuthorizationType


# pylint: disable=too-many-instance-attributes
# Necessary to load information from config
class CommunicatorConfiguration(EndpointConfiguration):
    """
    Configuration for the communicator.

    :param properties: a ConfigParser.ConfigParser object containing configuration data
    :param connect_timeout: connection timeout for the network communication in seconds
    :param socket_timeout: socket timeout for the network communication in seconds
    :param max_connections: The maximum number of connections in the connection pool
    """
    __api_key_id = None
    __secret_api_key = None

    def __init__(self, properties=None, api_endpoint=False, api_key_id=False,
                 secret_api_key=False, authorization_type=False,
                 connect_timeout=False, socket_timeout=False,
                 max_connections=False, proxy_configuration=False,
                 integrator=False, shopping_cart_extension=False):
        if properties:
            super(CommunicatorConfiguration, self).__init__(properties,
                                                            "connect.api")
            if properties.sections() and properties.options("ConnectSDK"):
                authorization = properties.get("ConnectSDK",
                                               "connect.api.authorizationType")
                self.__authorization_type = AuthorizationType.get_authorization(
                    authorization)
        if api_endpoint:
            self.api_endpoint = api_endpoint
        if api_key_id:
            self.api_key_id = api_key_id
        if secret_api_key:
            self.secret_api_key = secret_api_key
        if authorization_type:
            self.authorization_type = authorization_type
        if connect_timeout:
            self.connect_timeout = connect_timeout
        if socket_timeout:
            self.socket_timeout = socket_timeout
        if max_connections:
            self.max_connections = max_connections
        if proxy_configuration:
            self.proxy_configuration = proxy_configuration
        if integrator:
            self.integrator = integrator
        if shopping_cart_extension:
            self.shopping_cart_extension = shopping_cart_extension

    @property
    def api_endpoint(self):
        """
        The Ingenico ePayments platform API endpoint URI.
        """
        return super(CommunicatorConfiguration, self)._endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        super(CommunicatorConfiguration, self)._set_endpoint(api_endpoint)

    @property
    def api_key_id(self):
        """
        An identifier for the secret API key. The api_key_id can be
        retrieved from the Configuration Center. This identifier is visible in
        the HTTP request and is also used to identify the correct account.
        """
        return self.__api_key_id

    @api_key_id.setter
    def api_key_id(self, api_key_id):
        self.__api_key_id = api_key_id

    @property
    def secret_api_key(self):
        """
        A shared secret. The shared secret can be retrieved from the
        Configuration Center. An api_key_id and secret_api_key always go
        hand-in-hand, the difference is that secret_api_key is never visible in
        the HTTP request. This secret is used as input for the HMAC algorithm.
        """
        return self.__secret_api_key

    @secret_api_key.setter
    def secret_api_key(self, secret_api_key):
        self.__secret_api_key = secret_api_key

    @property
    def authorization_type(self):
        return self.__authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        self.__authorization_type = authorization_type
