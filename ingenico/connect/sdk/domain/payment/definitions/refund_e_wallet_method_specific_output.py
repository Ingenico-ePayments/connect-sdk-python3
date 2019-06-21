# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_payment_product840_specific_output import RefundPaymentProduct840SpecificOutput


class RefundEWalletMethodSpecificOutput(RefundMethodSpecificOutput):

    __payment_product840_specific_output = None

    @property
    def payment_product840_specific_output(self):
        """
        | PayPal (payment product 840) specific details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.refund_payment_product840_specific_output.RefundPaymentProduct840SpecificOutput`
        """
        return self.__payment_product840_specific_output

    @payment_product840_specific_output.setter
    def payment_product840_specific_output(self, value):
        self.__payment_product840_specific_output = value

    def to_dictionary(self):
        dictionary = super(RefundEWalletMethodSpecificOutput, self).to_dictionary()
        if self.payment_product840_specific_output is not None:
            dictionary['paymentProduct840SpecificOutput'] = self.payment_product840_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundEWalletMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'paymentProduct840SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct840SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840SpecificOutput']))
            value = RefundPaymentProduct840SpecificOutput()
            self.payment_product840_specific_output = value.from_dictionary(dictionary['paymentProduct840SpecificOutput'])
        return self
