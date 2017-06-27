# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.product.definitions.payment_product import PaymentProduct


class PaymentProductResponse(PaymentProduct):

    def to_dictionary(self):
        dictionary = super(PaymentProductResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductResponse, self).from_dictionary(dictionary)
        return self
