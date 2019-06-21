# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_product9000_specific_output import EInvoicePaymentProduct9000SpecificOutput


class EInvoicePaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):
    """
    | E-invoice payment specific response data
    """

    __payment_product9000_specific_output = None

    @property
    def payment_product9000_specific_output(self):
        """
        | AfterPay Installments (payment product 9000) specific details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_product9000_specific_output.EInvoicePaymentProduct9000SpecificOutput`
        """
        return self.__payment_product9000_specific_output

    @payment_product9000_specific_output.setter
    def payment_product9000_specific_output(self, value):
        self.__payment_product9000_specific_output = value

    def to_dictionary(self):
        dictionary = super(EInvoicePaymentMethodSpecificOutput, self).to_dictionary()
        if self.payment_product9000_specific_output is not None:
            dictionary['paymentProduct9000SpecificOutput'] = self.payment_product9000_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(EInvoicePaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'paymentProduct9000SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct9000SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct9000SpecificOutput']))
            value = EInvoicePaymentProduct9000SpecificOutput()
            self.payment_product9000_specific_output = value.from_dictionary(dictionary['paymentProduct9000SpecificOutput'])
        return self
