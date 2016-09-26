#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CashPaymentProduct1503SpecificInput(DataObject):
    """
    Class CashPaymentProduct1503SpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CashPaymentProduct1503SpecificInput
    
    Attributes:
        return_url:  str
     """

    return_url = None

    def to_dictionary(self):
        dictionary = super(CashPaymentProduct1503SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'returnUrl', self.return_url)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CashPaymentProduct1503SpecificInput, self).from_dictionary(dictionary)
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        return self
