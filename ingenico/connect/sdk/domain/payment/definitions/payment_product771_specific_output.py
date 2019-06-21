# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct771SpecificOutput(DataObject):

    __mandate_reference = None

    @property
    def mandate_reference(self):
        """
        | Unique reference to a Mandate
        
        Type: str
        """
        return self.__mandate_reference

    @mandate_reference.setter
    def mandate_reference(self, value):
        self.__mandate_reference = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct771SpecificOutput, self).to_dictionary()
        if self.mandate_reference is not None:
            dictionary['mandateReference'] = self.mandate_reference
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct771SpecificOutput, self).from_dictionary(dictionary)
        if 'mandateReference' in dictionary:
            self.mandate_reference = dictionary['mandateReference']
        return self
