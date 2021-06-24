# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct4101SpecificInput(DataObject):
    """
    | Please find below specific input fields for payment product 4101 (UPI)
    """

    __integration_type = None
    __merchant_name = None
    __transaction_note = None
    __vpa = None

    @property
    def integration_type(self):
        """
        | The value of this property must be either or 'vpa', 'QRCode', or 'urlIntent'.
        
        Type: str
        """
        return self.__integration_type

    @integration_type.setter
    def integration_type(self, value):
        self.__integration_type = value

    @property
    def merchant_name(self):
        """
        | The merchant name as shown to the customer in some payment applications.
        
        Type: str
        """
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self.__merchant_name = value

    @property
    def transaction_note(self):
        """
        | Some additional transaction information as shown to the customer in some payment applications.
        
        Type: str
        """
        return self.__transaction_note

    @transaction_note.setter
    def transaction_note(self, value):
        self.__transaction_note = value

    @property
    def vpa(self):
        """
        | The Virtual Payment Address (VPA) of the customer.
        
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
        if self.merchant_name is not None:
            dictionary['merchantName'] = self.merchant_name
        if self.transaction_note is not None:
            dictionary['transactionNote'] = self.transaction_note
        if self.vpa is not None:
            dictionary['vpa'] = self.vpa
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct4101SpecificInput, self).from_dictionary(dictionary)
        if 'integrationType' in dictionary:
            self.integration_type = dictionary['integrationType']
        if 'merchantName' in dictionary:
            self.merchant_name = dictionary['merchantName']
        if 'transactionNote' in dictionary:
            self.transaction_note = dictionary['transactionNote']
        if 'vpa' in dictionary:
            self.vpa = dictionary['vpa']
        return self
