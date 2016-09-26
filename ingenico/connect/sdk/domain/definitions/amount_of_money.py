#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class AmountOfMoney(DataObject):
    """
    Class AmountOfMoney
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AmountOfMoney
    
    Attributes:
        amount:         int
        currency_code:  str
     """

    amount = None
    currency_code = None

    def to_dictionary(self):
        dictionary = super(AmountOfMoney, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amount', self.amount)
        self._add_to_dictionary(dictionary, 'currencyCode', self.currency_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AmountOfMoney, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'currencyCode' in dictionary:
            self.currency_code = dictionary['currencyCode']
        return self
