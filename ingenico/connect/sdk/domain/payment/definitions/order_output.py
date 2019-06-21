# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.payment.definitions.payment_references import PaymentReferences


class OrderOutput(DataObject):

    __amount_of_money = None
    __references = None

    @property
    def amount_of_money(self):
        """
        | Object containing amount and ISO currency code attributes
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def references(self):
        """
        | Object that holds all reference properties that are linked to this transaction
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value):
        self.__references = value

    def to_dictionary(self):
        dictionary = super(OrderOutput, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderOutput, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        return self
