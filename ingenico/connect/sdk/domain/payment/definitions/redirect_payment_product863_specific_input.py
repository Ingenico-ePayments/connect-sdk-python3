# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct863SpecificInput(DataObject):

    __integration_type = None
    __open_id = None

    @property
    def integration_type(self):
        """
        | The type of integration with WeChat. Possible values:
        
        * desktopQRCode - used on desktops, the customer opens the WeChat app by scanning a QR code.
        * urlIntent - used in mobile apps or on mobile web pages, the customer opens the WeChat app using a URL intent.
        * nativeInApp - used in mobile apps that use the WeChat Pay SDK.
        * javaScriptAPI - used for WeChat official accounts. Requires the QQ browser to function.
        * miniProgram - used for Mini Programs.
        
        Type: str
        """
        return self.__integration_type

    @integration_type.setter
    def integration_type(self, value):
        self.__integration_type = value

    @property
    def open_id(self):
        """
        | An openId of a customer.
        
        Type: str
        """
        return self.__open_id

    @open_id.setter
    def open_id(self, value):
        self.__open_id = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct863SpecificInput, self).to_dictionary()
        if self.integration_type is not None:
            dictionary['integrationType'] = self.integration_type
        if self.open_id is not None:
            dictionary['openId'] = self.open_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct863SpecificInput, self).from_dictionary(dictionary)
        if 'integrationType' in dictionary:
            self.integration_type = dictionary['integrationType']
        if 'openId' in dictionary:
            self.open_id = dictionary['openId']
        return self
