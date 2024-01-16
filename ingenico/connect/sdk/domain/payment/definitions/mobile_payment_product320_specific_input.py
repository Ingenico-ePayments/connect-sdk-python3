# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.g_pay_three_d_secure import GPayThreeDSecure


class MobilePaymentProduct320SpecificInput(DataObject):

    __cardholder_name = None
    __three_d_secure = None

    @property
    def cardholder_name(self):
        """
        | The card holder's name on the card.
        | The encrypted payment data can be found in property paymentMethodData.tokenizationData.info.billingAddress.name of the PaymentData <https://developers.google.com/android/reference/com/google/android/gms/wallet/PaymentData>.toJson() result.
        
        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value

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
        dictionary = super(MobilePaymentProduct320SpecificInput, self).to_dictionary()
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentProduct320SpecificInput, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = GPayThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
