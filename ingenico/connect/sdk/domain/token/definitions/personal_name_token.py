# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.personal_name_base import PersonalNameBase


class PersonalNameToken(PersonalNameBase):

    def to_dictionary(self):
        dictionary = super(PersonalNameToken, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalNameToken, self).from_dictionary(dictionary)
        return self
