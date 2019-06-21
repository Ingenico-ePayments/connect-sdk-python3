# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class EInvoicePaymentProduct9000SpecificOutput(DataObject):

    __installment_id = None

    @property
    def installment_id(self):
        """
        | The ID of the installment plan used for the payment.
        
        Type: str
        """
        return self.__installment_id

    @installment_id.setter
    def installment_id(self, value):
        self.__installment_id = value

    def to_dictionary(self):
        dictionary = super(EInvoicePaymentProduct9000SpecificOutput, self).to_dictionary()
        if self.installment_id is not None:
            dictionary['installmentId'] = self.installment_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(EInvoicePaymentProduct9000SpecificOutput, self).from_dictionary(dictionary)
        if 'installmentId' in dictionary:
            self.installment_id = dictionary['installmentId']
        return self
