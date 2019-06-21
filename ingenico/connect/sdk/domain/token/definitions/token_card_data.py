# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.card_without_cvv import CardWithoutCvv


class TokenCardData(DataObject):

    __card_without_cvv = None
    __first_transaction_date = None
    __provider_reference = None

    @property
    def card_without_cvv(self):
        """
        | Object containing the card details (without CVV)
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.card_without_cvv.CardWithoutCvv`
        """
        return self.__card_without_cvv

    @card_without_cvv.setter
    def card_without_cvv(self, value):
        self.__card_without_cvv = value

    @property
    def first_transaction_date(self):
        """
        | Date of the first transaction (for ATOS)
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__first_transaction_date

    @first_transaction_date.setter
    def first_transaction_date(self, value):
        self.__first_transaction_date = value

    @property
    def provider_reference(self):
        """
        | Reference of the provider (of the first transaction) - used to store the ATOS Transaction Certificate
        
        Type: str
        """
        return self.__provider_reference

    @provider_reference.setter
    def provider_reference(self, value):
        self.__provider_reference = value

    def to_dictionary(self):
        dictionary = super(TokenCardData, self).to_dictionary()
        if self.card_without_cvv is not None:
            dictionary['cardWithoutCvv'] = self.card_without_cvv.to_dictionary()
        if self.first_transaction_date is not None:
            dictionary['firstTransactionDate'] = self.first_transaction_date
        if self.provider_reference is not None:
            dictionary['providerReference'] = self.provider_reference
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenCardData, self).from_dictionary(dictionary)
        if 'cardWithoutCvv' in dictionary:
            if not isinstance(dictionary['cardWithoutCvv'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardWithoutCvv']))
            value = CardWithoutCvv()
            self.card_without_cvv = value.from_dictionary(dictionary['cardWithoutCvv'])
        if 'firstTransactionDate' in dictionary:
            self.first_transaction_date = dictionary['firstTransactionDate']
        if 'providerReference' in dictionary:
            self.provider_reference = dictionary['providerReference']
        return self
