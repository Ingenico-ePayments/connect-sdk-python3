# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProductFieldDisplayElement(DataObject):

    __id = None
    __type = None
    __value = None

    @property
    def id(self):
        """
        | The ID of the display element.
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def type(self):
        """
        | The type of the display element. Indicates how the value should be presented. Possible values are:
        
        * string - as plain text
        * currency - as an amount in cents displayed with a decimal separator and the currency of the payment
        * percentage - as a number with a percentage sign
        * integer - as an integer
        * uri - as a link
        
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def value(self):
        """
        | the value of the display element.
        
        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldDisplayElement, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'type', self.type)
        self._add_to_dictionary(dictionary, 'value', self.value)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldDisplayElement, self).from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'type' in dictionary:
            self.type = dictionary['type']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
