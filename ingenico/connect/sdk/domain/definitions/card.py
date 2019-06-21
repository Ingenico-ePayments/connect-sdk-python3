# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card_without_cvv import CardWithoutCvv


class Card(CardWithoutCvv):

    __cvv = None

    @property
    def cvv(self):
        """
        | Card Verification Value, a 3 or 4 digit code used as an additional security feature for card not present transactions.
        
        Type: str
        """
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    def to_dictionary(self):
        dictionary = super(Card, self).to_dictionary()
        if self.cvv is not None:
            dictionary['cvv'] = self.cvv
        return dictionary

    def from_dictionary(self, dictionary):
        super(Card, self).from_dictionary(dictionary)
        if 'cvv' in dictionary:
            self.cvv = dictionary['cvv']
        return self
