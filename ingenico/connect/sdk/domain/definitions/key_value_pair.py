# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class KeyValuePair(DataObject):

    __key = None
    __value = None

    @property
    def key(self):
        """
        | Name of the key or property
        
        Type: str
        """
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

    @property
    def value(self):
        """
        | Value of the key or property
        
        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(KeyValuePair, self).to_dictionary()
        if self.key is not None:
            dictionary['key'] = self.key
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary):
        super(KeyValuePair, self).from_dictionary(dictionary)
        if 'key' in dictionary:
            self.key = dictionary['key']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
