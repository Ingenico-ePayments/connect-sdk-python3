#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class AmountBreakdown(DataObject):
    """
    Class AmountBreakdown
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AmountBreakdown
    """

    __amount = None
    __type = None

    @property
    def amount(self):
        """
        int
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def type(self):
        """
        str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(AmountBreakdown, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amount', self.amount)
        self._add_to_dictionary(dictionary, 'type', self.type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AmountBreakdown, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
