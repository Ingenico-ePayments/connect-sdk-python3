# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card_without_cvv import CardWithoutCvv


class Card(CardWithoutCvv):

    __cvv = None
    __partial_pin = None

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

    @property
    def partial_pin(self):
        """
        | The first 2 digits of the card's PIN code. May be optionally submitted for South Korean cards (paymentProductIds 180, 181, 182, 183, 184, 185 and 186). Submitting this property may improve your authorization rate.
        
        Type: str
        """
        return self.__partial_pin

    @partial_pin.setter
    def partial_pin(self, value):
        self.__partial_pin = value

    def to_dictionary(self):
        dictionary = super(Card, self).to_dictionary()
        if self.cvv is not None:
            dictionary['cvv'] = self.cvv
        if self.partial_pin is not None:
            dictionary['partialPin'] = self.partial_pin
        return dictionary

    def from_dictionary(self, dictionary):
        super(Card, self).from_dictionary(dictionary)
        if 'cvv' in dictionary:
            self.cvv = dictionary['cvv']
        if 'partialPin' in dictionary:
            self.partial_pin = dictionary['partialPin']
        return self
