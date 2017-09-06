# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_payment_method_specific_input import ApprovePaymentPaymentMethodSpecificInput


class ApprovePaymentDirectDebitPaymentMethodSpecificInput(ApprovePaymentPaymentMethodSpecificInput):

    def to_dictionary(self):
        dictionary = super(ApprovePaymentDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePaymentDirectDebitPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        return self
