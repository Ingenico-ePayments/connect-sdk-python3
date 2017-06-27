# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class AbstractPayoutMethodSpecificInput(DataObject):

    def to_dictionary(self):
        dictionary = super(AbstractPayoutMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractPayoutMethodSpecificInput, self).from_dictionary(dictionary)
        return self
