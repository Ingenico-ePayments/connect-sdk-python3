# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.refund.definitions.refund_result import RefundResult


class RefundResponse(RefundResult):

    def to_dictionary(self):
        dictionary = super(RefundResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundResponse, self).from_dictionary(dictionary)
        return self
