# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.g_pay_three_d_secure import GPayThreeDSecure


class MobilePaymentProduct320SpecificInputHostedCheckout(DataObject):

    __merchant_name = None
    __merchant_origin = None
    __three_d_secure = None

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

    @property
    def three_d_secure(self):
        """
        | Object containing specific data regarding 3-D Secure
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.g_pay_three_d_secure.GPayThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value):
        self.__three_d_secure = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentProduct320SpecificInputHostedCheckout, self).to_dictionary()
        if self.merchant_name is not None:
            dictionary['merchantName'] = self.merchant_name
        if self.merchant_origin is not None:
            dictionary['merchantOrigin'] = self.merchant_origin
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentProduct320SpecificInputHostedCheckout, self).from_dictionary(dictionary)
        if 'merchantName' in dictionary:
            self.merchant_name = dictionary['merchantName']
        if 'merchantOrigin' in dictionary:
            self.merchant_origin = dictionary['merchantOrigin']
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = GPayThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
