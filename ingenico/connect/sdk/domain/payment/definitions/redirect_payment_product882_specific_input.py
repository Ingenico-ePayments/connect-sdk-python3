# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct882SpecificInput(DataObject):
    """
    | Please find below specific input fields for payment product 882 (Net Banking)
    """

    __issuer_id = None

    @property
    def issuer_id(self):
        """
        | ID of the issuing bank of the customer. A list of available issuerIDs can be obtained by using the retrieve payment product directory API.
        
        Type: str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value):
        self.__issuer_id = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct882SpecificInput, self).to_dictionary()
        if self.issuer_id is not None:
            dictionary['issuerId'] = self.issuer_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct882SpecificInput, self).from_dictionary(dictionary)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        return self
