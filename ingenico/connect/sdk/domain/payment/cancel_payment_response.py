# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.cancel_payment_card_payment_method_specific_output import CancelPaymentCardPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.cancel_payment_mobile_payment_method_specific_output import CancelPaymentMobilePaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment


class CancelPaymentResponse(DataObject):
    """
    | Response to the cancelation of a payment
    """

    __card_payment_method_specific_output = None
    __mobile_payment_method_specific_output = None
    __payment = None

    @property
    def card_payment_method_specific_output(self):
        """
        | Object that holds specific information on cancelled card payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cancel_payment_card_payment_method_specific_output.CancelPaymentCardPaymentMethodSpecificOutput`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value):
        self.__card_payment_method_specific_output = value

    @property
    def mobile_payment_method_specific_output(self):
        """
        | Object that holds specific information on cancelled mobile payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cancel_payment_mobile_payment_method_specific_output.CancelPaymentMobilePaymentMethodSpecificOutput`
        """
        return self.__mobile_payment_method_specific_output

    @mobile_payment_method_specific_output.setter
    def mobile_payment_method_specific_output(self, value):
        self.__mobile_payment_method_specific_output = value

    @property
    def payment(self):
        """
        | Object that holds the payment related properties
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment.Payment`
        """
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    def to_dictionary(self):
        dictionary = super(CancelPaymentResponse, self).to_dictionary()
        if self.card_payment_method_specific_output is not None:
            dictionary['cardPaymentMethodSpecificOutput'] = self.card_payment_method_specific_output.to_dictionary()
        if self.mobile_payment_method_specific_output is not None:
            dictionary['mobilePaymentMethodSpecificOutput'] = self.mobile_payment_method_specific_output.to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CancelPaymentResponse, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = CancelPaymentCardPaymentMethodSpecificOutput()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'mobilePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificOutput']))
            value = CancelPaymentMobilePaymentMethodSpecificOutput()
            self.mobile_payment_method_specific_output = value.from_dictionary(dictionary['mobilePaymentMethodSpecificOutput'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self
