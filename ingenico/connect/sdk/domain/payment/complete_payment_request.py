# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.complete_payment_card_payment_method_specific_input import CompletePaymentCardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.merchant import Merchant
from ingenico.connect.sdk.domain.payment.definitions.order import Order


class CompletePaymentRequest(DataObject):

    __card_payment_method_specific_input = None
    __merchant = None
    __order = None

    @property
    def card_payment_method_specific_input(self):
        """
        | Object containing the specific input details for card payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.complete_payment_card_payment_method_specific_input.CompletePaymentCardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value):
        self.__card_payment_method_specific_input = value

    @property
    def merchant(self):
        """
        | Object containing information on you, the merchant
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.merchant.Merchant`
        """
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value

    @property
    def order(self):
        """
        | Order object containing order related data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    def to_dictionary(self):
        dictionary = super(CompletePaymentRequest, self).to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.merchant is not None:
            dictionary['merchant'] = self.merchant.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CompletePaymentRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CompletePaymentCardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'merchant' in dictionary:
            if not isinstance(dictionary['merchant'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchant']))
            value = Merchant()
            self.merchant = value.from_dictionary(dictionary['merchant'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        return self
