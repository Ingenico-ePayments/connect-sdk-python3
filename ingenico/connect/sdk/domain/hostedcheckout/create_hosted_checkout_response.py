#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CreateHostedCheckoutResponse(DataObject):
    """
    Class CreateHostedCheckoutResponse
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreateHostedCheckoutResponse
    
    Attributes:
        returnmac:             str
        hosted_checkout_id:    str
        partial_redirect_url:  str
     """

    returnmac = None
    hosted_checkout_id = None
    partial_redirect_url = None

    def to_dictionary(self):
        dictionary = super(CreateHostedCheckoutResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'RETURNMAC', self.returnmac)
        self._add_to_dictionary(dictionary, 'hostedCheckoutId', self.hosted_checkout_id)
        self._add_to_dictionary(dictionary, 'partialRedirectUrl', self.partial_redirect_url)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedCheckoutResponse, self).from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'hostedCheckoutId' in dictionary:
            self.hosted_checkout_id = dictionary['hostedCheckoutId']
        if 'partialRedirectUrl' in dictionary:
            self.partial_redirect_url = dictionary['partialRedirectUrl']
        return self
