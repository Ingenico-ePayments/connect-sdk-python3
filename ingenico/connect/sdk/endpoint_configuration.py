from configparser import NoOptionError
from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from ingenico.connect.sdk.domain.metadata.shopping_cart_extension import \
    ShoppingCartExtension

from .proxy_configuration import ProxyConfiguration


class EndpointConfiguration(object):
    """
    Base class for endpoint configurations.
    """
    # The default number of maximum connections.
    DEFAULT_MAX_CONNECTIONS = 10

    def __init__(self, properties=None, prefix=None):
        if properties and properties.sections() and properties.options("ConnectSDK"):
            self.__endpoint = self.__get_endpoint(properties, prefix)
            self.__connect_timeout = int(
                properties.get("ConnectSDK",
                               prefix + ".connectTimeout"))
            self.__socket_timeout = int(
                properties.get("ConnectSDK",
                               prefix + ".socketTimeout"))
            self.__max_connections = \
                self.__get_property(properties, prefix + ".maxConnections",
                                    self.DEFAULT_MAX_CONNECTIONS)
            try:
                proxy_uri = properties.get("ConnectSDK",
                                           prefix + ".proxy.uri")
            except NoOptionError:
                proxy_uri = None
            try:
                proxy_user = properties.get("ConnectSDK",
                                            prefix + ".proxy.username")
            except NoOptionError:
                proxy_user = None
            try:
                proxy_pass = properties.get("ConnectSDK",
                                            prefix + ".proxy.password")
            except NoOptionError:
                proxy_pass = None
            if proxy_uri is not None:
                self.__proxy_configuration = ProxyConfiguration.from_uri(
                    proxy_uri,
                    proxy_user,
                    proxy_pass)
            else:
                self.__proxy_configuration = None
            try:
                self.__integrator = properties.get("ConnectSDK",
                                                   prefix + ".integrator")
            except NoOptionError:
                self.__integrator = None
            try:
                self.__shopping_cart_extension = \
                    self.__get_shopping_cart_extension(properties, prefix)
            except NoOptionError:
                self.__shopping_cart_extension = None

    def __get_property(self, properties, key, default_value):
        try:
            property_value = properties.get("ConnectSDK", key)
        except NoOptionError:
            property_value = None
        if property_value is not None:
            return int(property_value)
        else:
            return default_value

    def __get_endpoint(self, properties, prefix):
        host = properties.get("ConnectSDK", prefix + ".endpoint.host")
        try:
            scheme = properties.get("ConnectSDK",
                                    prefix + ".endpoint.scheme")
        except NoOptionError:
            scheme = None
        try:
            port = properties.get("ConnectSDK",
                                  prefix + ".endpoint.port")
        except NoOptionError:
            port = None
        if scheme:
            if port:
                return self.__create_uri(scheme, host, int(port))
            else:
                return self.__create_uri(scheme, host, -1)
        elif port:
            return self.__create_uri("https", host, int(port))
        else:
            return self.__create_uri("https", host, -1)

    def __create_uri(self, scheme, host, port):
        if port != -1:
            uri = scheme + "://" + host + ":" + str(port)
        else:
            uri = scheme + "://" + host
        try:
            URLValidator(uri)
            return urlparse(uri)
        except ValidationError as e:
            raise ValueError("Unable to construct endpoint URI", e)

    def __get_shopping_cart_extension(self, properties, prefix):
        try:
            creator = properties.get("ConnectSDK",
                                     prefix + ".shoppingCartExtension.creator")
        except NoOptionError:
            creator = None
        try:
            name = properties.get("ConnectSDK",
                                  prefix + ".shoppingCartExtension.name")
        except NoOptionError:
            name = None
        try:
            version = properties.get("ConnectSDK",
                                     prefix + ".shoppingCartExtension.version")
        except NoOptionError:
            version = None
        try:
            extension_id = properties.get("ConnectSDK",
                                          prefix + ".shoppingCartExtension.extensionId")
        except NoOptionError:
            extension_id = None
        if creator is None and name is None and version is None and extension_id is None:
            return None
        else:
            return ShoppingCartExtension(creator, name, version, extension_id)

    @property
    def _endpoint(self):
        return self.__endpoint

    def _set_endpoint(self, endpoint):
        if isinstance(endpoint, str):
            endpoint = urlparse(str(endpoint))
        if endpoint is not None and endpoint.path:
            raise ValueError("apiEndpoint should not contain a path")
        if endpoint is not None and (
                endpoint.username is not None or
                endpoint.query or endpoint.fragment):
            raise ValueError(
                "apiEndpoint should not contain user info, query or fragment")
        self.__endpoint = endpoint

    @property
    def connect_timeout(self):
        """Connection timeout for the underlying network communication in seconds"""
        return self.__connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        self.__connect_timeout = connect_timeout

    @property
    def socket_timeout(self):
        """Socket timeout for the underlying network communication in seconds"""
        return self.__socket_timeout

    @socket_timeout.setter
    def socket_timeout(self, socket_timeout):
        self.__socket_timeout = socket_timeout

    @property
    def max_connections(self):
        return self.__max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        self.__max_connections = max_connections

    @property
    def proxy_configuration(self):
        return self.__proxy_configuration

    @proxy_configuration.setter
    def proxy_configuration(self, proxy_configuration):
        self.__proxy_configuration = proxy_configuration

    @property
    def integrator(self):
        return self.__integrator

    @integrator.setter
    def integrator(self, integrator):
        self.__integrator = integrator

    @property
    def shopping_cart_extension(self):
        return self.__shopping_cart_extension

    @shopping_cart_extension.setter
    def shopping_cart_extension(self, shopping_cart_extension):
        self.__shopping_cart_extension = shopping_cart_extension
