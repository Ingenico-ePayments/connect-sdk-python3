# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.bank_account import BankAccount


class BankAccountIban(BankAccount):

    __iban = None

    @property
    def iban(self):
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits.
        
        Type: str
        """
        return self.__iban

    @iban.setter
    def iban(self, value):
        self.__iban = value

    def to_dictionary(self):
        dictionary = super(BankAccountIban, self).to_dictionary()
        if self.iban is not None:
            dictionary['iban'] = self.iban
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccountIban, self).from_dictionary(dictionary)
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        return self
