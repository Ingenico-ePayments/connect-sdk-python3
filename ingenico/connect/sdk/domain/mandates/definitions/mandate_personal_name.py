# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MandatePersonalName(DataObject):

    __first_name = None
    __surname = None

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
        | Surname(s) or last name(s) of the customer
        
        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    def to_dictionary(self):
        dictionary = super(MandatePersonalName, self).to_dictionary()
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.surname is not None:
            dictionary['surname'] = self.surname
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandatePersonalName, self).from_dictionary(dictionary)
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        return self
