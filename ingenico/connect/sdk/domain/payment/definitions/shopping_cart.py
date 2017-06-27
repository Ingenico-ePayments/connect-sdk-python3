# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.amount_breakdown import AmountBreakdown


class ShoppingCart(DataObject):

    __amount_breakdown = None

    @property
    def amount_breakdown(self):
        """
        | Determines the type of the amount.
        
        Type: list[:class:`ingenico.connect.sdk.domain.payment.definitions.amount_breakdown.AmountBreakdown`]
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
