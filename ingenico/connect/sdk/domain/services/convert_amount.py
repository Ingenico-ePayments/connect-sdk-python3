# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ConvertAmount(DataObject):

    __converted_amount = None

    @property
    def converted_amount(self):
        """
        | Converted amount in cents and having 2 decimal
        
        Type: int
        """
        return self.__converted_amount

    @converted_amount.setter
    def converted_amount(self, value):
        self.__converted_amount = value

    def to_dictionary(self):
        dictionary = super(ConvertAmount, self).to_dictionary()
        if self.converted_amount is not None:
            dictionary['convertedAmount'] = self.converted_amount
        return dictionary

    def from_dictionary(self, dictionary):
        super(ConvertAmount, self).from_dictionary(dictionary)
        if 'convertedAmount' in dictionary:
            self.converted_amount = dictionary['convertedAmount']
        return self
