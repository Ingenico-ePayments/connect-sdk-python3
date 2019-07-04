# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class LoanRecipient(DataObject):

    __account_number = None
    __date_of_birth = None
    __partial_pan = None
    __surname = None
    __zip = None

    @property
    def account_number(self):
        """
        | Should be filled with the last 10 digits of the bank account number of the recipient of the loan.
        
        Type: str
        """
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def date_of_birth(self):
        """
        | The date of birth of the customer of the recipient of the loan.
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @property
    def partial_pan(self):
        """
        | Should be filled with the first 6 and last 4 digits of the PAN number of the recipient of the loan.
        
        Type: str
        """
        return self.__partial_pan

    @partial_pan.setter
    def partial_pan(self, value):
        self.__partial_pan = value

    @property
    def surname(self):
        """
        | Surname of the recipient of the loan.
        
        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def zip(self):
        """
        | Zip code of the recipient of the loan
        
        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    def to_dictionary(self):
        dictionary = super(LoanRecipient, self).to_dictionary()
        if self.account_number is not None:
            dictionary['accountNumber'] = self.account_number
        if self.date_of_birth is not None:
            dictionary['dateOfBirth'] = self.date_of_birth
        if self.partial_pan is not None:
            dictionary['partialPan'] = self.partial_pan
        if self.surname is not None:
            dictionary['surname'] = self.surname
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary):
        super(LoanRecipient, self).from_dictionary(dictionary)
        if 'accountNumber' in dictionary:
            self.account_number = dictionary['accountNumber']
        if 'dateOfBirth' in dictionary:
            self.date_of_birth = dictionary['dateOfBirth']
        if 'partialPan' in dictionary:
            self.partial_pan = dictionary['partialPan']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
