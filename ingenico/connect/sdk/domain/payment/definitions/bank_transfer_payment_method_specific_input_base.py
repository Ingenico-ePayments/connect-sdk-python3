# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_bank_transfer_payment_method_specific_input import AbstractBankTransferPaymentMethodSpecificInput


class BankTransferPaymentMethodSpecificInputBase(AbstractBankTransferPaymentMethodSpecificInput):

    def to_dictionary(self):
        dictionary = super(BankTransferPaymentMethodSpecificInputBase, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankTransferPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        return self
