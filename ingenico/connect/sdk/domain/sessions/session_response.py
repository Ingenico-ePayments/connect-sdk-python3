#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class SessionResponse(DataObject):
    """
    Class SessionResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_SessionResponse
    """

    __client_session_id = None
    __customer_id = None
    __invalid_tokens = None
    __region = None

    @property
    def client_session_id(self):
        """
        str
        """
        return self.__client_session_id

    @client_session_id.setter
    def client_session_id(self, value):
        self.__client_session_id = value

    @property
    def customer_id(self):
        """
        str
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value

    @property
    def invalid_tokens(self):
        """
        list[str]
        """
        return self.__invalid_tokens

    @invalid_tokens.setter
    def invalid_tokens(self, value):
        self.__invalid_tokens = value

    @property
    def region(self):
        """
        str
        """
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value

    def to_dictionary(self):
        dictionary = super(SessionResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'clientSessionId', self.client_session_id)
        self._add_to_dictionary(dictionary, 'customerId', self.customer_id)
        self._add_to_dictionary(dictionary, 'invalidTokens', self.invalid_tokens)
        self._add_to_dictionary(dictionary, 'region', self.region)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SessionResponse, self).from_dictionary(dictionary)
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
