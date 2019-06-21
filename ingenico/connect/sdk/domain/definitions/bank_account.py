# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class BankAccount(DataObject):

    __account_holder_name = None

    @property
    def account_holder_name(self):
        """
        | Name in which the account is held.
        
        Type: str
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value

    def to_dictionary(self):
        dictionary = super(BankAccount, self).to_dictionary()
        if self.account_holder_name is not None:
            dictionary['accountHolderName'] = self.account_holder_name
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccount, self).from_dictionary(dictionary)
        if 'accountHolderName' in dictionary:
            self.account_holder_name = dictionary['accountHolderName']
        return self
