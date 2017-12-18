# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class SessionResponse(DataObject):

    __asset_url = None
    __client_api_url = None
    __client_session_id = None
    __customer_id = None
    __invalid_tokens = None
    __region = None

    @property
    def asset_url(self):
        """
        | The base url for assets.
        
        Type: str
        """
        return self.__asset_url

    @asset_url.setter
    def asset_url(self, value):
        self.__asset_url = value

    @property
    def client_api_url(self):
        """
        | The base url for client requests.
        
        Type: str
        """
        return self.__client_api_url

    @client_api_url.setter
    def client_api_url(self, value):
        self.__client_api_url = value

    @property
    def client_session_id(self):
        """
        | The identifier of the session that has been created.
        
        Type: str
        """
        return self.__client_session_id

    @client_session_id.setter
    def client_session_id(self, value):
        self.__client_session_id = value

    @property
    def customer_id(self):
        """
        | The session is build up around the consumer in the form of the customerId. All of the Client APIs use this customerId in the URI to identify the consumer.
        
        Type: str
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def invalid_tokens(self):
        """
        | Tokens that are submitted in the request are validated. In case any of the tokens can't be used anymore they are returned in this array. You should most likely remove those tokens from your system.
        
        Type: list[str]
        """
        return self.__invalid_tokens

    @invalid_tokens.setter
    def invalid_tokens(self, value):
        self.__invalid_tokens = value

    @property
    def region(self):
        """
        | Possible values:
        
        * EU - datacenter located in Amsterdam
        * US - datacenter located in Miami
        * AMS - datacenter located in Amsterdam
        * PAR - datacenter located in Paris
        
        | When a session is created it is created in a specific datacenter. Any subsequent calls using the Client API need to be datacenter specific. The region is identified by EU or AMS (datacenter located in Amsterdam), US (datacenter located in Miami) or PAR (datacenter located in Paris). This value needs to be passed to the a Client SDK to make sure that the client software connects to the right datacenter.
        
        Type: str
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value

    def to_dictionary(self):
        dictionary = super(SessionResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'assetUrl', self.asset_url)
        self._add_to_dictionary(dictionary, 'clientApiUrl', self.client_api_url)
        self._add_to_dictionary(dictionary, 'clientSessionId', self.client_session_id)
        self._add_to_dictionary(dictionary, 'customerId', self.customer_id)
        self._add_to_dictionary(dictionary, 'invalidTokens', self.invalid_tokens)
        self._add_to_dictionary(dictionary, 'region', self.region)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SessionResponse, self).from_dictionary(dictionary)
        if 'assetUrl' in dictionary:
            self.asset_url = dictionary['assetUrl']
        if 'clientApiUrl' in dictionary:
            self.client_api_url = dictionary['clientApiUrl']
        if 'clientSessionId' in dictionary:
            self.client_session_id = dictionary['clientSessionId']
        if 'customerId' in dictionary:
            self.customer_id = dictionary['customerId']
        if 'invalidTokens' in dictionary:
            if not isinstance(dictionary['invalidTokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['invalidTokens']))
            self.invalid_tokens = []
            for invalidTokens_element in dictionary['invalidTokens']:
                self.invalid_tokens.append(invalidTokens_element)
        if 'region' in dictionary:
            self.region = dictionary['region']
        return self
