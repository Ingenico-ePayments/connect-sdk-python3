# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MobilePaymentProduct320SpecificInputHostedCheckout(DataObject):

    __merchant_name = None
    __merchant_origin = None

    @property
    def merchant_name(self):
        """
        | Used as an input for the Google Pay payment sheet. Provide your company name in a human readable form.
        
        Type: str
        """
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self.__merchant_name = value

    @property
    def merchant_origin(self):
        """
        | Used as an input for the Google Pay payment sheet. Provide the url of your webshop. For international (non-ASCII) domains, please use Punycode <https://en.wikipedia.org/wiki/Punycode>.
        
        Type: str
        """
        return self.__merchant_origin

    @merchant_origin.setter
    def merchant_origin(self, value):
        self.__merchant_origin = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentProduct320SpecificInputHostedCheckout, self).to_dictionary()
        if self.merchant_name is not None:
            dictionary['merchantName'] = self.merchant_name
        if self.merchant_origin is not None:
            dictionary['merchantOrigin'] = self.merchant_origin
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentProduct320SpecificInputHostedCheckout, self).from_dictionary(dictionary)
        if 'merchantName' in dictionary:
            self.merchant_name = dictionary['merchantName']
        if 'merchantOrigin' in dictionary:
            self.merchant_origin = dictionary['merchantOrigin']
        return self
