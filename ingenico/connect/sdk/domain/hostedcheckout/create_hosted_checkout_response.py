#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CreateHostedCheckoutResponse(DataObject):
    """
    Class CreateHostedCheckoutResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreateHostedCheckoutResponse
    """

    __returnmac = None
    __hosted_checkout_id = None
    __invalid_tokens = None
    __partial_redirect_url = None

    @property
    def returnmac(self):
        """
        str
        """
        return self.__returnmac

    @returnmac.setter
    def returnmac(self, value):
        self.__returnmac = value

    @property
    def hosted_checkout_id(self):
        """
        str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value):
        self.__hosted_checkout_id = value

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
    def partial_redirect_url(self):
        """
        str
        """
        return self.__partial_redirect_url

    @partial_redirect_url.setter
    def partial_redirect_url(self, value):
        self.__partial_redirect_url = value

    def to_dictionary(self):
        dictionary = super(CreateHostedCheckoutResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'RETURNMAC', self.returnmac)
        self._add_to_dictionary(dictionary, 'hostedCheckoutId', self.hosted_checkout_id)
        self._add_to_dictionary(dictionary, 'invalidTokens', self.invalid_tokens)
        self._add_to_dictionary(dictionary, 'partialRedirectUrl', self.partial_redirect_url)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedCheckoutResponse, self).from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'hostedCheckoutId' in dictionary:
            self.hosted_checkout_id = dictionary['hostedCheckoutId']
        if 'invalidTokens' in dictionary:
            if not isinstance(dictionary['invalidTokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['invalidTokens']))
            self.invalid_tokens = []
            for invalidTokens_element in dictionary['invalidTokens']:
                self.invalid_tokens.append(invalidTokens_element)
        if 'partialRedirectUrl' in dictionary:
            self.partial_redirect_url = dictionary['partialRedirectUrl']
        return self
