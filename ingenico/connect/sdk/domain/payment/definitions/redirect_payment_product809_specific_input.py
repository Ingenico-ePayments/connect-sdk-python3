#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct809SpecificInput(DataObject):
    """
    Class RedirectPaymentProduct809SpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RedirectPaymentProduct809SpecificInput
    """

    __expiration_period = None
    __issuer_id = None

    @property
    def expiration_period(self):
        """
        str
        """
        return self.__expiration_period

    @expiration_period.setter
    def expiration_period(self, value):
        self.__expiration_period = value

    @property
    def issuer_id(self):
        """
        str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value):
        self.__issuer_id = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct809SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'expirationPeriod', self.expiration_period)
        self._add_to_dictionary(dictionary, 'issuerId', self.issuer_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct809SpecificInput, self).from_dictionary(dictionary)
        if 'expirationPeriod' in dictionary:
            self.expiration_period = dictionary['expirationPeriod']
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        return self
