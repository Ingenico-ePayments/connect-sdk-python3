# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.token.definitions.token_card import TokenCard
from ingenico.connect.sdk.domain.token.definitions.token_e_wallet import TokenEWallet
from ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit import TokenNonSepaDirectDebit
from ingenico.connect.sdk.domain.token.definitions.token_sepa_direct_debit_without_creditor import TokenSepaDirectDebitWithoutCreditor


class UpdateTokenRequest(DataObject):

    __card = None
    __e_wallet = None
    __non_sepa_direct_debit = None
    __payment_product_id = None
    __sepa_direct_debit = None

    @property
    def card(self):
        """
        | Object containing card details
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.token_card.TokenCard`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def e_wallet(self):
        """
        | Object containing eWallet details
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.token_e_wallet.TokenEWallet`
        """
        return self.__e_wallet

    @e_wallet.setter
    def e_wallet(self, value):
        self.__e_wallet = value

    @property
    def non_sepa_direct_debit(self):
        """
        | Object containing the non SEPA Direct Debit details
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit.TokenNonSepaDirectDebit`
        """
        return self.__non_sepa_direct_debit

    @non_sepa_direct_debit.setter
    def non_sepa_direct_debit(self, value):
        self.__non_sepa_direct_debit = value

    @property
    def payment_product_id(self):
        """
        | Payment product identifier
        | Please see payment products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    @property
    def sepa_direct_debit(self):
        """
        | Object containing the SEPA Direct Debit details
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.token_sepa_direct_debit_without_creditor.TokenSepaDirectDebitWithoutCreditor`
        """
        return self.__sepa_direct_debit

    @sepa_direct_debit.setter
    def sepa_direct_debit(self, value):
        self.__sepa_direct_debit = value

    def to_dictionary(self):
        dictionary = super(UpdateTokenRequest, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.e_wallet is not None:
            dictionary['eWallet'] = self.e_wallet.to_dictionary()
        if self.non_sepa_direct_debit is not None:
            dictionary['nonSepaDirectDebit'] = self.non_sepa_direct_debit.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.sepa_direct_debit is not None:
            dictionary['sepaDirectDebit'] = self.sepa_direct_debit.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(UpdateTokenRequest, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = TokenCard()
            self.card = value.from_dictionary(dictionary['card'])
        if 'eWallet' in dictionary:
            if not isinstance(dictionary['eWallet'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eWallet']))
            value = TokenEWallet()
            self.e_wallet = value.from_dictionary(dictionary['eWallet'])
        if 'nonSepaDirectDebit' in dictionary:
            if not isinstance(dictionary['nonSepaDirectDebit'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['nonSepaDirectDebit']))
            value = TokenNonSepaDirectDebit()
            self.non_sepa_direct_debit = value.from_dictionary(dictionary['nonSepaDirectDebit'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'sepaDirectDebit' in dictionary:
            if not isinstance(dictionary['sepaDirectDebit'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebit']))
            value = TokenSepaDirectDebitWithoutCreditor()
            self.sepa_direct_debit = value.from_dictionary(dictionary['sepaDirectDebit'])
        return self
