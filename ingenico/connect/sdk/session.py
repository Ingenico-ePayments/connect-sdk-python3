from urllib.parse import urlparse


class Session(object):
    """
    Contains the components needed to communicate with the Ingenico ePayments platform.

    :param api_endpoint: the address of the target server as a string or ParseResult object
    """
    def __init__(self, api_endpoint, connection, authenticator,
                 meta_data_provider):
        if api_endpoint is None:
            raise ValueError("api_endpoint is required")
        if isinstance(api_endpoint, str):
            api_endpoint = urlparse(api_endpoint)
        if api_endpoint.path:
            raise ValueError("api_endpoint should not contain a path")
        if api_endpoint.username is not None or api_endpoint.query or api_endpoint.fragment:
            raise ValueError(
                "api_endpoint should not contain user info, query or fragment")
        if connection is None:
            raise ValueError("connection is required")
        if authenticator is None:
            raise ValueError("authenticator is required")
        if meta_data_provider is None:
            raise ValueError("meta_data_provider is required")
        self.__api_endpoint = api_endpoint
        self.__connection = connection
        self.__authenticator = authenticator
        self.__meta_data_provider = meta_data_provider

    @property
    def api_endpoint(self):
        """
        :return: The Ingenico ePayments platform API endpoint URI. This URI's path
         will be None or empty.
        """
        return self.__api_endpoint

    @property
    def connection(self):
        """
        :return: The Connection object associated with this session. Never None.
        """
        return self.__connection

    @property
    def authenticator(self):
        """
        :return: The Authenticator object associated with this session. Never None.
        """
        return self.__authenticator

    @property
    def meta_data_provider(self):
        """
        :return: The MetaDataProvider object associated with this session. Never None.
        """
        return self.__meta_data_provider
