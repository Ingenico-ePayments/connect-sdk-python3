# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.token.definitions.mandate_approval import MandateApproval


class ApproveTokenRequest(MandateApproval):

    def to_dictionary(self):
        dictionary = super(ApproveTokenRequest, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApproveTokenRequest, self).from_dictionary(dictionary)
        return self
