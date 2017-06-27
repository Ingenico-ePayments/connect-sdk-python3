# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase


class ContactDetailsToken(ContactDetailsBase):

    def to_dictionary(self):
        dictionary = super(ContactDetailsToken, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetailsToken, self).from_dictionary(dictionary)
        return self
