# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.token.definitions.abstract_token import AbstractToken
from ingenico.connect.sdk.domain.token.definitions.customer_token import CustomerToken
from ingenico.connect.sdk.domain.token.definitions.mandate_non_sepa_direct_debit import MandateNonSepaDirectDebit


class TokenNonSepaDirectDebit(AbstractToken):

    __customer = None
    __mandate = None

    @property
    def customer(self):
        """
        | Object containing the details of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.customer_token.CustomerToken`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def mandate(self):
        """
        | Object containing the mandate details
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.mandate_non_sepa_direct_debit.MandateNonSepaDirectDebit`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    def to_dictionary(self):
        dictionary = super(TokenNonSepaDirectDebit, self).to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenNonSepaDirectDebit, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerToken()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateNonSepaDirectDebit()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
