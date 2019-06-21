# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_redirect_payment_method_specific_input import AbstractRedirectPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product840_specific_input_base import RedirectPaymentProduct840SpecificInputBase


class RedirectPaymentMethodSpecificInputBase(AbstractRedirectPaymentMethodSpecificInput):

    __payment_product840_specific_input = None

    @property
    def payment_product840_specific_input(self):
        """
        | Object containing specific input required for PayPal payments (Payment product ID 840)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product840_specific_input_base.RedirectPaymentProduct840SpecificInputBase`
        """
        return self.__payment_product840_specific_input

    @payment_product840_specific_input.setter
    def payment_product840_specific_input(self, value):
        self.__payment_product840_specific_input = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificInputBase, self).to_dictionary()
        if self.payment_product840_specific_input is not None:
            dictionary['paymentProduct840SpecificInput'] = self.payment_product840_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'paymentProduct840SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct840SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840SpecificInput']))
            value = RedirectPaymentProduct840SpecificInputBase()
            self.payment_product840_specific_input = value.from_dictionary(dictionary['paymentProduct840SpecificInput'])
        return self
