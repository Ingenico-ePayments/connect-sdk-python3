from urllib.parse import urlparse


class ProxyConfiguration:
    """
    HTTP proxy configuration.

    Can be initialised directly from a host and port or can be constructed from a uri using fromuri
    """

    def __init__(self, host, port, scheme="http", username=None, password=None):
        if not host:
            raise ValueError("host is required")
        if not port:
            raise ValueError("port is required")
        if port <= 0 or port > 65535:
            raise ValueError("""port "{}" is invalid""".format(port))
        self.__scheme = scheme
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password

    @staticmethod
    def from_uri(uri, username=None, password=None):
        """
        Constructs a ProxyConfiguration from a URI; if username and/or password
        are given they will be used instead of corresponding data in the URI
        """
        parsed = urlparse(uri)
        scheme = parsed.scheme
        host = parsed.hostname + parsed.path
        port = parsed.port
        if username is None:
            username = parsed.username
        if password is None:
            password = parsed.password
        if port is None:
            if scheme == "http":
                port = 80
            elif scheme == "https":
                port = 443
            else:
                raise ValueError("unsupported scheme: " + scheme)
        return ProxyConfiguration(scheme=scheme, host=host, port=port,
                                  username=username, password=password)

    @property
    def scheme(self):
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme):
        self.__scheme = scheme

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.__host = host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        """
        Return a proxy string in the form scheme://username:password@host:port
        or scheme://host:port if authentication is absent

        Supports HTTP Basic Auth
        """
        if self.username is None or self.password is None:
            return r"{0}://{1}:{2}".format(self.scheme, self.host, self.port)
        else:
            return r"{0}://{3}:{4}@{1}:{2}".format(self.scheme, self.host,
                                                   self.port, self.username,
                                                   self.password)
