# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney


class PaymentContext(DataObject):
    """
    | Values that can optionally be set to refine an IIN Lookup
    """

    __amount_of_money = None
    __country_code = None
    __is_recurring = None

    @property
    def amount_of_money(self):
        """
        | The payment amount
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def country_code(self):
        """
        | The country the payment takes place in
        
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def is_recurring(self):
        """
        | True if the payment is recurring
        
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    def to_dictionary(self):
        dictionary = super(PaymentContext, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
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
