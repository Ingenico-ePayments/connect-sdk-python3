# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.token.definitions.abstract_token import AbstractToken
from ingenico.connect.sdk.domain.token.definitions.customer_token import CustomerToken
from ingenico.connect.sdk.domain.token.definitions.token_e_wallet_data import TokenEWalletData


class TokenEWallet(AbstractToken):

    __customer = None
    __data = None

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
    def data(self):
        """
        | Object containing the eWallet tokenizable data
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.token_e_wallet_data.TokenEWalletData`
        """
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def to_dictionary(self):
        dictionary = super(TokenEWallet, self).to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.data is not None:
            dictionary['data'] = self.data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenEWallet, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerToken()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenEWalletData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
