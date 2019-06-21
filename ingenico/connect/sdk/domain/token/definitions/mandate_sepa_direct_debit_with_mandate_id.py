# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.token.definitions.mandate_sepa_direct_debit_without_creditor import MandateSepaDirectDebitWithoutCreditor


class MandateSepaDirectDebitWithMandateId(MandateSepaDirectDebitWithoutCreditor):

    __mandate_id = None

    @property
    def mandate_id(self):
        """
        | Unique mandate identifier
        
        Type: str
        """
        return self.__mandate_id

    @mandate_id.setter
    def mandate_id(self, value):
        self.__mandate_id = value

    def to_dictionary(self):
        dictionary = super(MandateSepaDirectDebitWithMandateId, self).to_dictionary()
        if self.mandate_id is not None:
            dictionary['mandateId'] = self.mandate_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateSepaDirectDebitWithMandateId, self).from_dictionary(dictionary)
        if 'mandateId' in dictionary:
            self.mandate_id = dictionary['mandateId']
        return self
