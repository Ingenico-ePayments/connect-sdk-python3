# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct4101SpecificInput(DataObject):
    """
    | Please find below specific input fields for payment product 4101 (UPI)
    """

    __display_name = None
    __integration_type = None
    __virtual_payment_address = None

    @property
    def display_name(self):
        """
        | The merchant name as shown to the customer in some payment applications.
        
        Type: str
        """
        return self.__display_name

    @display_name.setter
    def display_name(self, value):
        self.__display_name = value

    @property
    def integration_type(self):
        """
        | The value of this property must be 'vpa', 'desktopQRCode', or 'urlIntent'.
        
        Type: str
        """
        return self.__integration_type

    @integration_type.setter
    def integration_type(self, value):
        self.__integration_type = value

    @property
    def virtual_payment_address(self):
        """
        | The Virtual Payment Address (VPA) of the customer. The '+' character is not allowed in this property for transactions that are processed by TechProcess Payment Platform.
        
        Type: str
        """
        return self.__virtual_payment_address

    @virtual_payment_address.setter
    def virtual_payment_address(self, value):
        self.__virtual_payment_address = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct4101SpecificInput, self).to_dictionary()
        if self.display_name is not None:
            dictionary['displayName'] = self.display_name
        if self.integration_type is not None:
            dictionary['integrationType'] = self.integration_type
        if self.virtual_payment_address is not None:
            dictionary['virtualPaymentAddress'] = self.virtual_payment_address
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct4101SpecificInput, self).from_dictionary(dictionary)
        if 'displayName' in dictionary:
            self.display_name = dictionary['displayName']
        if 'integrationType' in dictionary:
            self.integration_type = dictionary['integrationType']
        if 'virtualPaymentAddress' in dictionary:
            self.virtual_payment_address = dictionary['virtualPaymentAddress']
        return self
