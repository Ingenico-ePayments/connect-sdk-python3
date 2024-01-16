# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_e_invoice_payment_method_specific_input import AbstractEInvoicePaymentMethodSpecificInput


class EInvoicePaymentMethodSpecificInputBase(AbstractEInvoicePaymentMethodSpecificInput):

    def to_dictionary(self):
        dictionary = super(EInvoicePaymentMethodSpecificInputBase, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(EInvoicePaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        return self
