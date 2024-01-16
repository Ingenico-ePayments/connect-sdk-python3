# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.domain.definitions.card_essentials import CardEssentials
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput


class RefundCardMethodSpecificOutput(RefundMethodSpecificOutput):

    __authorisation_code = None
    __card = None

    @property
    def authorisation_code(self):
        """
        | Card Authorization code as returned by the acquirer
        
        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value):
        self.__authorisation_code = value

    @property
    def card(self):
        """
        | Object containing card details
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.card_essentials.CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    def to_dictionary(self):
        dictionary = super(RefundCardMethodSpecificOutput, self).to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundCardMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardEssentials()
            self.card = value.from_dictionary(dictionary['card'])
        return self
