# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RangeValidator(DataObject):

    __max_value = None
    __min_value = None

    @property
    def max_value(self):
        """
        | Upper value of the range that is still valid
        
        Type: int
        """
        return self.__max_value

    @max_value.setter
    def max_value(self, value):
        self.__max_value = value

    @property
    def min_value(self):
        """
        | Lower value of the range that is still valid
        
        Type: int
        """
        return self.__min_value

    @min_value.setter
    def min_value(self, value):
        self.__min_value = value

    def to_dictionary(self):
        dictionary = super(RangeValidator, self).to_dictionary()
        if self.max_value is not None:
            dictionary['maxValue'] = self.max_value
        if self.min_value is not None:
            dictionary['minValue'] = self.min_value
        return dictionary

    def from_dictionary(self, dictionary):
        super(RangeValidator, self).from_dictionary(dictionary)
        if 'maxValue' in dictionary:
            self.max_value = dictionary['maxValue']
        if 'minValue' in dictionary:
            self.min_value = dictionary['minValue']
        return self
