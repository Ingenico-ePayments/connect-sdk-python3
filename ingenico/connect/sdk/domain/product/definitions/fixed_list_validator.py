# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class FixedListValidator(DataObject):

    __allowed_values = None

    @property
    def allowed_values(self):
        """
        | List of the allowed values that the field will be validated against
        
        Type: list[str]
        """
        return self.__allowed_values

    @allowed_values.setter
    def allowed_values(self, value):
        self.__allowed_values = value

    def to_dictionary(self):
        dictionary = super(FixedListValidator, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'allowedValues', self.allowed_values)
        return dictionary

    def from_dictionary(self, dictionary):
        super(FixedListValidator, self).from_dictionary(dictionary)
        if 'allowedValues' in dictionary:
            if not isinstance(dictionary['allowedValues'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['allowedValues']))
            self.allowed_values = []
            for allowedValues_element in dictionary['allowedValues']:
                self.allowed_values.append(allowedValues_element)
        return self
