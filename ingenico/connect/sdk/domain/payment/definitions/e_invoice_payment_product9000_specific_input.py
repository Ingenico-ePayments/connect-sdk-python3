# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban


class EInvoicePaymentProduct9000SpecificInput(DataObject):

    __bank_account_iban = None
    __installment_id = None

    @property
    def bank_account_iban(self):
        """
        | Object containing the bank account details of the customer.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.bank_account_iban.BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value):
        self.__bank_account_iban = value

    @property
    def installment_id(self):
        """
        | The ID of the installment plan selected by the customer. Installment plans can be retrieved with Get payment product <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/get.html>.
        
        Type: str
        """
        return self.__installment_id

    @installment_id.setter
    def installment_id(self, value):
        self.__installment_id = value

    def to_dictionary(self):
        dictionary = super(EInvoicePaymentProduct9000SpecificInput, self).to_dictionary()
        if self.bank_account_iban is not None:
            dictionary['bankAccountIban'] = self.bank_account_iban.to_dictionary()
        if self.installment_id is not None:
            dictionary['installmentId'] = self.installment_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(EInvoicePaymentProduct9000SpecificInput, self).from_dictionary(dictionary)
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'installmentId' in dictionary:
            self.installment_id = dictionary['installmentId']
        return self
