# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.complete_payment_card_payment_method_specific_input import CompletePaymentCardPaymentMethodSpecificInput


class CompletePaymentRequest(DataObject):

    __card_payment_method_specific_input = None

    @property
    def card_payment_method_specific_input(self):
        """
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.complete_payment_card_payment_method_specific_input.CompletePaymentCardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value):
        self.__card_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(CompletePaymentRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificInput', self.card_payment_method_specific_input)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CompletePaymentRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CompletePaymentCardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        return self
