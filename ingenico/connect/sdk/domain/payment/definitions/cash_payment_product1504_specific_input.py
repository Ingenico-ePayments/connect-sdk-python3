#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CashPaymentProduct1504SpecificInput(DataObject):
    """
    Class CashPaymentProduct1504SpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CashPaymentProduct1504SpecificInput
    """

    __return_url = None

    @property
    def return_url(self):
        """
        str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    def to_dictionary(self):
        dictionary = super(CashPaymentProduct1504SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'returnUrl', self.return_url)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CashPaymentProduct1504SpecificInput, self).from_dictionary(dictionary)
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        return self
