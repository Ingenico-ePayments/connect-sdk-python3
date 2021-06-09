# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct4101SpecificInput(DataObject):
    """
    | Contains specific input required for UPI payments.
    """

    __integration_type = None
    __vpa = None

    @property
    def integration_type(self):
        """
        | The integration type to be used in the UPI payment
        
        Type: str
        """
        return self.__integration_type

    @integration_type.setter
    def integration_type(self, value):
        self.__integration_type = value

    @property
    def vpa(self):
        """
        | The virtual payment address.
        
        Type: str
        """
        return self.__vpa

    @vpa.setter
    def vpa(self, value):
        self.__vpa = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct4101SpecificInput, self).to_dictionary()
        if self.integration_type is not None:
            dictionary['integrationType'] = self.integration_type
        if self.vpa is not None:
            dictionary['vpa'] = self.vpa
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct4101SpecificInput, self).from_dictionary(dictionary)
        if 'integrationType' in dictionary:
            self.integration_type = dictionary['integrationType']
        if 'vpa' in dictionary:
            self.vpa = dictionary['vpa']
        return self
