# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.fraud_results import FraudResults
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment_product771_specific_output import PaymentProduct771SpecificOutput


class SepaDirectDebitPaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):

    __fraud_results = None
    __payment_product771_specific_output = None

    @property
    def fraud_results(self):
        """
        | Object containing the results of the fraud screening
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.fraud_results.FraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value):
        self.__fraud_results = value

    @property
    def payment_product771_specific_output(self):
        """
        | Output that is SEPA Direct Debit specific (i.e. the used mandate)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment_product771_specific_output.PaymentProduct771SpecificOutput`
        """
        return self.__payment_product771_specific_output

    @payment_product771_specific_output.setter
    def payment_product771_specific_output(self, value):
        self.__payment_product771_specific_output = value

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentMethodSpecificOutput, self).to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.payment_product771_specific_output is not None:
            dictionary['paymentProduct771SpecificOutput'] = self.payment_product771_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = FraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'paymentProduct771SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct771SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct771SpecificOutput']))
            value = PaymentProduct771SpecificOutput()
            self.payment_product771_specific_output = value.from_dictionary(dictionary['paymentProduct771SpecificOutput'])
        return self
