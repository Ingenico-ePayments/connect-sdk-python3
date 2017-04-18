#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.amount_breakdown import AmountBreakdown


class ShoppingCart(DataObject):
    """
    Class ShoppingCart
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ShoppingCart
    """

    __amount_breakdown = None

    @property
    def amount_breakdown(self):
        """
        list[:class:`AmountBreakdown`]
        """
        return self.__amount_breakdown

    @amount_breakdown.setter
    def amount_breakdown(self, value):
        self.__amount_breakdown = value

    def to_dictionary(self):
        dictionary = super(ShoppingCart, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountBreakdown', self.amount_breakdown)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShoppingCart, self).from_dictionary(dictionary)
        if 'amountBreakdown' in dictionary:
            if not isinstance(dictionary['amountBreakdown'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['amountBreakdown']))
            self.amount_breakdown = []
            for amountBreakdown_element in dictionary['amountBreakdown']:
                amountBreakdown_value = AmountBreakdown()
                self.amount_breakdown.append(amountBreakdown_value.from_dictionary(amountBreakdown_element))
        return self
