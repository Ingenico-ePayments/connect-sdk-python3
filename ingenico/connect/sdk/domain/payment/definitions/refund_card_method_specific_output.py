# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput


class RefundCardMethodSpecificOutput(RefundMethodSpecificOutput):

    __authorisation_code = None

    @property
    def authorisation_code(self):
        """
        | Card Authorization code as returned by the acquirer
        
        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value):
        self.__authorisation_code = value

    def to_dictionary(self):
        dictionary = super(RefundCardMethodSpecificOutput, self).to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundCardMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        return self
