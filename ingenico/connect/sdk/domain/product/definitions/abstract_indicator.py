# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class AbstractIndicator(DataObject):

    __name = None
    __value = None

    @property
    def name(self):
        """
        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def value(self):
        """
        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(AbstractIndicator, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractIndicator, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
