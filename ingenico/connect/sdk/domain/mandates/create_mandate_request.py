# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.mandates.definitions.create_mandate_with_return_url import CreateMandateWithReturnUrl


class CreateMandateRequest(CreateMandateWithReturnUrl):

    def to_dictionary(self):
        dictionary = super(CreateMandateRequest, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateMandateRequest, self).from_dictionary(dictionary)
        return self
