# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.create_payment_result import CreatePaymentResult


class CreatePaymentResponse(CreatePaymentResult):

    def to_dictionary(self):
        dictionary = super(CreatePaymentResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentResponse, self).from_dictionary(dictionary)
        return self
