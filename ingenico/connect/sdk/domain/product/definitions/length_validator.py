# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class LengthValidator(DataObject):

    __max_length = None
    __min_length = None

    @property
    def max_length(self):
        """
        | The maximum allowed length
        
        Type: int
        """
        return self.__max_length

    @max_length.setter
    def max_length(self, value):
        self.__max_length = value

    @property
    def min_length(self):
        """
        | The minimum allowed length
        
        Type: int
        """
        return self.__min_length

    @min_length.setter
    def min_length(self, value):
        self.__min_length = value

    def to_dictionary(self):
        dictionary = super(LengthValidator, self).to_dictionary()
        if self.max_length is not None:
            dictionary['maxLength'] = self.max_length
        if self.min_length is not None:
            dictionary['minLength'] = self.min_length
        return dictionary

    def from_dictionary(self, dictionary):
        super(LengthValidator, self).from_dictionary(dictionary)
        if 'maxLength' in dictionary:
            self.max_length = dictionary['maxLength']
        if 'minLength' in dictionary:
            self.min_length = dictionary['minLength']
        return self
