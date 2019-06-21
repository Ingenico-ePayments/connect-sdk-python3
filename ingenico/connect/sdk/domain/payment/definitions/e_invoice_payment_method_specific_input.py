# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_e_invoice_payment_method_specific_input import AbstractEInvoicePaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_product9000_specific_input import EInvoicePaymentProduct9000SpecificInput


class EInvoicePaymentMethodSpecificInput(AbstractEInvoicePaymentMethodSpecificInput):

    __accepted_terms_and_conditions = None
    __payment_product9000_specific_input = None

    @property
    def accepted_terms_and_conditions(self):
        """
        | Indicates that the customer has read and accepted the terms and conditions of the product before proceeding with the payment. This must be done before the payment can continue. An URL to the terms and conditions can be retrieved with Get payment product <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/get.html>.
        
        Type: bool
        """
        return self.__accepted_terms_and_conditions

    @accepted_terms_and_conditions.setter
    def accepted_terms_and_conditions(self, value):
        self.__accepted_terms_and_conditions = value

    @property
    def payment_product9000_specific_input(self):
        """
        | Object that holds the specific data for AfterPay Installments (payment product 9000).
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_product9000_specific_input.EInvoicePaymentProduct9000SpecificInput`
        """
        return self.__payment_product9000_specific_input

    @payment_product9000_specific_input.setter
    def payment_product9000_specific_input(self, value):
        self.__payment_product9000_specific_input = value

    def to_dictionary(self):
        dictionary = super(EInvoicePaymentMethodSpecificInput, self).to_dictionary()
        if self.accepted_terms_and_conditions is not None:
            dictionary['acceptedTermsAndConditions'] = self.accepted_terms_and_conditions
        if self.payment_product9000_specific_input is not None:
            dictionary['paymentProduct9000SpecificInput'] = self.payment_product9000_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(EInvoicePaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'acceptedTermsAndConditions' in dictionary:
            self.accepted_terms_and_conditions = dictionary['acceptedTermsAndConditions']
        if 'paymentProduct9000SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct9000SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct9000SpecificInput']))
            value = EInvoicePaymentProduct9000SpecificInput()
            self.payment_product9000_specific_input = value.from_dictionary(dictionary['paymentProduct9000SpecificInput'])
        return self
