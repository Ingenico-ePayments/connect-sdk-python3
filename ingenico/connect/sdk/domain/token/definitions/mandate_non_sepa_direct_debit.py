# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit_payment_product705_specific_data import TokenNonSepaDirectDebitPaymentProduct705SpecificData
from ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit_payment_product730_specific_data import TokenNonSepaDirectDebitPaymentProduct730SpecificData


class MandateNonSepaDirectDebit(DataObject):

    __payment_product705_specific_data = None
    __payment_product730_specific_data = None

    @property
    def payment_product705_specific_data(self):
        """
        | Object containing specific data for Direct Debit UK
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit_payment_product705_specific_data.TokenNonSepaDirectDebitPaymentProduct705SpecificData`
        """
        return self.__payment_product705_specific_data

    @payment_product705_specific_data.setter
    def payment_product705_specific_data(self, value):
        self.__payment_product705_specific_data = value

    @property
    def payment_product730_specific_data(self):
        """
        | Object containing specific data for ACH
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit_payment_product730_specific_data.TokenNonSepaDirectDebitPaymentProduct730SpecificData`
        """
        return self.__payment_product730_specific_data

    @payment_product730_specific_data.setter
    def payment_product730_specific_data(self, value):
        self.__payment_product730_specific_data = value

    def to_dictionary(self):
        dictionary = super(MandateNonSepaDirectDebit, self).to_dictionary()
        if self.payment_product705_specific_data is not None:
            dictionary['paymentProduct705SpecificData'] = self.payment_product705_specific_data.to_dictionary()
        if self.payment_product730_specific_data is not None:
            dictionary['paymentProduct730SpecificData'] = self.payment_product730_specific_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateNonSepaDirectDebit, self).from_dictionary(dictionary)
        if 'paymentProduct705SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct705SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct705SpecificData']))
            value = TokenNonSepaDirectDebitPaymentProduct705SpecificData()
            self.payment_product705_specific_data = value.from_dictionary(dictionary['paymentProduct705SpecificData'])
        if 'paymentProduct730SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct730SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct730SpecificData']))
            value = TokenNonSepaDirectDebitPaymentProduct730SpecificData()
            self.payment_product730_specific_data = value.from_dictionary(dictionary['paymentProduct730SpecificData'])
        return self
