# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_cash_payment_method_specific_input import AbstractCashPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1503_specific_input import CashPaymentProduct1503SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1504_specific_input import CashPaymentProduct1504SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1521_specific_input import CashPaymentProduct1521SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1522_specific_input import CashPaymentProduct1522SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1523_specific_input import CashPaymentProduct1523SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1524_specific_input import CashPaymentProduct1524SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1526_specific_input import CashPaymentProduct1526SpecificInput


class CashPaymentMethodSpecificInput(AbstractCashPaymentMethodSpecificInput):

    __payment_product1503_specific_input = None
    __payment_product1504_specific_input = None
    __payment_product1521_specific_input = None
    __payment_product1522_specific_input = None
    __payment_product1523_specific_input = None
    __payment_product1524_specific_input = None
    __payment_product1526_specific_input = None

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

    @property
    def payment_product1521_specific_input(self):
        """
        | Object that holds the specific data for e-Pay (payment product 1521).
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1521_specific_input.CashPaymentProduct1521SpecificInput`
        """
        return self.__payment_product1521_specific_input

    @payment_product1521_specific_input.setter
    def payment_product1521_specific_input(self, value):
        self.__payment_product1521_specific_input = value

    @property
    def payment_product1522_specific_input(self):
        """
        | Object that holds the specific data for Tesco - Paysbuy Cash (payment product 1522).
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1522_specific_input.CashPaymentProduct1522SpecificInput`
        """
        return self.__payment_product1522_specific_input

    @payment_product1522_specific_input.setter
    def payment_product1522_specific_input(self, value):
        self.__payment_product1522_specific_input = value

    @property
    def payment_product1523_specific_input(self):
        """
        | Object that holds the specific data for ATM Transfers Indonesia(payment product 1523).
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1523_specific_input.CashPaymentProduct1523SpecificInput`
        """
        return self.__payment_product1523_specific_input

    @payment_product1523_specific_input.setter
    def payment_product1523_specific_input(self, value):
        self.__payment_product1523_specific_input = value

    @property
    def payment_product1524_specific_input(self):
        """
        | Object that holds the specific data for DragonPay (payment product 1524).
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1524_specific_input.CashPaymentProduct1524SpecificInput`
        """
        return self.__payment_product1524_specific_input

    @payment_product1524_specific_input.setter
    def payment_product1524_specific_input(self, value):
        self.__payment_product1524_specific_input = value

    @property
    def payment_product1526_specific_input(self):
        """
        | Object that holds the specific data for 7-11 MOLPay Cash (payment product 1526).
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1526_specific_input.CashPaymentProduct1526SpecificInput`
        """
        return self.__payment_product1526_specific_input

    @payment_product1526_specific_input.setter
    def payment_product1526_specific_input(self, value):
        self.__payment_product1526_specific_input = value

    def to_dictionary(self):
        dictionary = super(CashPaymentMethodSpecificInput, self).to_dictionary()
        if self.payment_product1503_specific_input is not None:
            dictionary['paymentProduct1503SpecificInput'] = self.payment_product1503_specific_input.to_dictionary()
        if self.payment_product1504_specific_input is not None:
            dictionary['paymentProduct1504SpecificInput'] = self.payment_product1504_specific_input.to_dictionary()
        if self.payment_product1521_specific_input is not None:
            dictionary['paymentProduct1521SpecificInput'] = self.payment_product1521_specific_input.to_dictionary()
        if self.payment_product1522_specific_input is not None:
            dictionary['paymentProduct1522SpecificInput'] = self.payment_product1522_specific_input.to_dictionary()
        if self.payment_product1523_specific_input is not None:
            dictionary['paymentProduct1523SpecificInput'] = self.payment_product1523_specific_input.to_dictionary()
        if self.payment_product1524_specific_input is not None:
            dictionary['paymentProduct1524SpecificInput'] = self.payment_product1524_specific_input.to_dictionary()
        if self.payment_product1526_specific_input is not None:
            dictionary['paymentProduct1526SpecificInput'] = self.payment_product1526_specific_input.to_dictionary()
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
        if 'paymentProduct1521SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1521SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1521SpecificInput']))
            value = CashPaymentProduct1521SpecificInput()
            self.payment_product1521_specific_input = value.from_dictionary(dictionary['paymentProduct1521SpecificInput'])
        if 'paymentProduct1522SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1522SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1522SpecificInput']))
            value = CashPaymentProduct1522SpecificInput()
            self.payment_product1522_specific_input = value.from_dictionary(dictionary['paymentProduct1522SpecificInput'])
        if 'paymentProduct1523SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1523SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1523SpecificInput']))
            value = CashPaymentProduct1523SpecificInput()
            self.payment_product1523_specific_input = value.from_dictionary(dictionary['paymentProduct1523SpecificInput'])
        if 'paymentProduct1524SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1524SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1524SpecificInput']))
            value = CashPaymentProduct1524SpecificInput()
            self.payment_product1524_specific_input = value.from_dictionary(dictionary['paymentProduct1524SpecificInput'])
        if 'paymentProduct1526SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1526SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1526SpecificInput']))
            value = CashPaymentProduct1526SpecificInput()
            self.payment_product1526_specific_input = value.from_dictionary(dictionary['paymentProduct1526SpecificInput'])
        return self
