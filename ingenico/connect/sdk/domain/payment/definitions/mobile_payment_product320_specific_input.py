# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MobilePaymentProduct320SpecificInput(DataObject):
    """
    | Please find below specific input fields for payment product 320 (Android Pay)
    """

    __key_id = None

    @property
    def key_id(self):
        """
        | The identifier of the public key that is used to create the vendor's encrypted payment data
        
        Type: str
        """
        return self.__key_id

    @key_id.setter
    def key_id(self, value):
        self.__key_id = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentProduct320SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'keyId', self.key_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentProduct320SpecificInput, self).from_dictionary(dictionary)
        if 'keyId' in dictionary:
            self.key_id = dictionary['keyId']
        return self
