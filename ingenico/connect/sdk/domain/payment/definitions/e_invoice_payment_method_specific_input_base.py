# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class EInvoicePaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):

    __requires_approval = None

    @property
    def requires_approval(self):
        """
        * true = the payment requires approval before the funds will be captured using the Capture payment <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/approve.html> API
        * false = the payment does not require approval, and the funds will be captured automatically
        
        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value):
        self.__requires_approval = value

    def to_dictionary(self):
        dictionary = super(EInvoicePaymentMethodSpecificInputBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'requiresApproval', self.requires_approval)
        return dictionary

    def from_dictionary(self, dictionary):
        super(EInvoicePaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        return self
