# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.token.definitions.creditor import Creditor
from ingenico.connect.sdk.domain.token.definitions.mandate_sepa_direct_debit_with_mandate_id import MandateSepaDirectDebitWithMandateId


class MandateSepaDirectDebit(MandateSepaDirectDebitWithMandateId):

    __creditor = None

    @property
    def creditor(self):
        """
        | Object containing information on the creditor
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.creditor.Creditor`
        """
        return self.__creditor

    @creditor.setter
    def creditor(self, value):
        self.__creditor = value

    def to_dictionary(self):
        dictionary = super(MandateSepaDirectDebit, self).to_dictionary()
        if self.creditor is not None:
            dictionary['creditor'] = self.creditor.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateSepaDirectDebit, self).from_dictionary(dictionary)
        if 'creditor' in dictionary:
            if not isinstance(dictionary['creditor'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['creditor']))
            value = Creditor()
            self.creditor = value.from_dictionary(dictionary['creditor'])
        return self
