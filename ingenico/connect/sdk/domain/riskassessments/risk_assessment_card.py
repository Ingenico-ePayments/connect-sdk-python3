# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.riskassessments.definitions.risk_assessment import RiskAssessment


class RiskAssessmentCard(RiskAssessment):

    __card = None

    @property
    def card(self):
        """
        | Object containing Card object
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    def to_dictionary(self):
        dictionary = super(RiskAssessmentCard, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RiskAssessmentCard, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        return self
