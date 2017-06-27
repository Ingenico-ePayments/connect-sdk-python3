# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment


class PaymentResponse(Payment):

    def to_dictionary(self):
        dictionary = super(PaymentResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentResponse, self).from_dictionary(dictionary)
        return self
