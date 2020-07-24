# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.mobile_payment_product_session302_specific_input import MobilePaymentProductSession302SpecificInput


class CreatePaymentProductSessionRequest(DataObject):

    __payment_product_session302_specific_input = None

    @property
    def payment_product_session302_specific_input(self):
        """
        | Object containing details for creating an Apple Pay session.
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.mobile_payment_product_session302_specific_input.MobilePaymentProductSession302SpecificInput`
        """
        return self.__payment_product_session302_specific_input

    @payment_product_session302_specific_input.setter
    def payment_product_session302_specific_input(self, value):
        self.__payment_product_session302_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreatePaymentProductSessionRequest, self).to_dictionary()
        if self.payment_product_session302_specific_input is not None:
            dictionary['paymentProductSession302SpecificInput'] = self.payment_product_session302_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentProductSessionRequest, self).from_dictionary(dictionary)
        if 'paymentProductSession302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProductSession302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductSession302SpecificInput']))
            value = MobilePaymentProductSession302SpecificInput()
            self.payment_product_session302_specific_input = value.from_dictionary(dictionary['paymentProductSession302SpecificInput'])
        return self
