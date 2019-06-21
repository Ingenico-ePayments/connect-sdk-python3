# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_card_payment_method_specific_input import AbstractCardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.three_d_secure_base import ThreeDSecureBase


class CardPaymentMethodSpecificInputBase(AbstractCardPaymentMethodSpecificInput):

    __three_d_secure = None

    @property
    def three_d_secure(self):
        """
        | Object containing specific data regarding 3-D Secure
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.three_d_secure_base.ThreeDSecureBase`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value):
        self.__three_d_secure = value

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInputBase, self).to_dictionary()
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = ThreeDSecureBase()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
