# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payout.definitions.payout_result import PayoutResult


class PayoutResponse(PayoutResult):

    def to_dictionary(self):
        dictionary = super(PayoutResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutResponse, self).from_dictionary(dictionary)
        return self
