# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban


class RedirectPaymentProduct816SpecificInput(DataObject):
    """
    | Please find below specific input fields for payment product 816 (giropay)
    """

    __bank_account_iban = None

    @property
    def bank_account_iban(self):
        """
        | Object containing the bank account details of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.bank_account_iban.BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value):
        self.__bank_account_iban = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct816SpecificInput, self).to_dictionary()
        if self.bank_account_iban is not None:
            dictionary['bankAccountIban'] = self.bank_account_iban.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct816SpecificInput, self).from_dictionary(dictionary)
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        return self
