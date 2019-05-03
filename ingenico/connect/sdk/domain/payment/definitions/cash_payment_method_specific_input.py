# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_cash_payment_method_specific_input import AbstractCashPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1503_specific_input import CashPaymentProduct1503SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1504_specific_input import CashPaymentProduct1504SpecificInput


class CashPaymentMethodSpecificInput(AbstractCashPaymentMethodSpecificInput):

    __payment_product1503_specific_input = None
    __payment_product1504_specific_input = None

    @property
    def payment_product1503_specific_input(self):
        """
        | Object that holds the specific data for Boleto Bancario in Brazil (payment product 1503)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1503_specific_input.CashPaymentProduct1503SpecificInput`
        
        Deprecated; No replacement
        """
        return self.__payment_product1503_specific_input

    @payment_product1503_specific_input.setter
    def payment_product1503_specific_input(self, value):
        self.__payment_product1503_specific_input = value

    @property
    def payment_product1504_specific_input(self):
        """
        | Object that holds the specific data for Konbini in Japan (payment product 1504)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1504_specific_input.CashPaymentProduct1504SpecificInput`
        """
        return self.__payment_product1504_specific_input

    @payment_product1504_specific_input.setter
    def payment_product1504_specific_input(self, value):
        self.__payment_product1504_specific_input = value

    def to_dictionary(self):
        dictionary = super(CashPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProduct1503SpecificInput', self.payment_product1503_specific_input)
        self._add_to_dictionary(dictionary, 'paymentProduct1504SpecificInput', self.payment_product1504_specific_input)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CashPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'paymentProduct1503SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1503SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1503SpecificInput']))
            value = CashPaymentProduct1503SpecificInput()
            self.payment_product1503_specific_input = value.from_dictionary(dictionary['paymentProduct1503SpecificInput'])
        if 'paymentProduct1504SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1504SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1504SpecificInput']))
            value = CashPaymentProduct1504SpecificInput()
            self.payment_product1504_specific_input = value.from_dictionary(dictionary['paymentProduct1504SpecificInput'])
        return self
