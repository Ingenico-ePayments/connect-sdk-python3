# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_direct_debit_payment_method_specific_input import ApprovePaymentDirectDebitPaymentMethodSpecificInput


class ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput(ApprovePaymentDirectDebitPaymentMethodSpecificInput):

    def to_dictionary(self):
        dictionary = super(ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        return self
