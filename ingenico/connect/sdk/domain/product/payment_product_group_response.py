# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.product.definitions.payment_product_group import PaymentProductGroup


class PaymentProductGroupResponse(PaymentProductGroup):

    def to_dictionary(self):
        dictionary = super(PaymentProductGroupResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductGroupResponse, self).from_dictionary(dictionary)
        return self
