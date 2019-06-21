# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PersonalNameBase(DataObject):

    __first_name = None
    __surname = None
    __surname_prefix = None

    @property
    def first_name(self):
        """
        | Given name(s) or first name(s) of the customer
        
        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def surname(self):
        """
        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def surname_prefix(self):
        """
        | Middle name - In between first name and surname - of the customer
        
        Type: str
        """
        return self.__surname_prefix

    @surname_prefix.setter
    def surname_prefix(self, value):
        self.__surname_prefix = value

    def to_dictionary(self):
        dictionary = super(PersonalNameBase, self).to_dictionary()
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.surname is not None:
            dictionary['surname'] = self.surname
        if self.surname_prefix is not None:
            dictionary['surnamePrefix'] = self.surname_prefix
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalNameBase, self).from_dictionary(dictionary)
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'surnamePrefix' in dictionary:
            self.surname_prefix = dictionary['surnamePrefix']
        return self
