# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.domain.definitions.redirect_data_base import RedirectDataBase


class RedirectData(RedirectDataBase):

    def to_dictionary(self):
        dictionary = super(RedirectData, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectData, self).from_dictionary(dictionary)
        return self
