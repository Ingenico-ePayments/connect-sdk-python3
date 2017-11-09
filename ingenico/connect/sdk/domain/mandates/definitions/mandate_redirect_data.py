# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.redirect_data_base import RedirectDataBase


class MandateRedirectData(RedirectDataBase):

    def to_dictionary(self):
        dictionary = super(MandateRedirectData, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateRedirectData, self).from_dictionary(dictionary)
        return self
