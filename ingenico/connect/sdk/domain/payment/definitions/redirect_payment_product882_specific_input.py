#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct882SpecificInput(DataObject):
    """
    Class RedirectPaymentProduct882SpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RedirectPaymentProduct882SpecificInput
    """

    __issuer_id = None

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
        dictionary = super(RedirectPaymentProduct882SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'issuerId', self.issuer_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct882SpecificInput, self).from_dictionary(dictionary)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        return self
