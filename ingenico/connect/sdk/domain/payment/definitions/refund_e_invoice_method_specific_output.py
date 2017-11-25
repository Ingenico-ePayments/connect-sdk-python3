# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput


class RefundEInvoiceMethodSpecificOutput(RefundMethodSpecificOutput):

    def to_dictionary(self):
        dictionary = super(RefundEInvoiceMethodSpecificOutput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundEInvoiceMethodSpecificOutput, self).from_dictionary(dictionary)
        return self
