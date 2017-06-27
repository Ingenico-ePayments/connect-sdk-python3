# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.services.definitions.bank_details import BankDetails


class BankDetailsRequest(BankDetails):

    def to_dictionary(self):
        dictionary = super(BankDetailsRequest, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankDetailsRequest, self).from_dictionary(dictionary)
        return self
