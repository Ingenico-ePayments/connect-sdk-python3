#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney


class PaymentContext(DataObject):
    """
    Class PaymentContext
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentContext
    
    Attributes:
        amount_of_money:  :class:`AmountOfMoney`
        country_code:     str
        is_recurring:     bool
     """

    amount_of_money = None
    country_code = None
    is_recurring = None

    def to_dictionary(self):
        dictionary = super(PaymentContext, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountOfMoney', self.amount_of_money)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentContext, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        return self
