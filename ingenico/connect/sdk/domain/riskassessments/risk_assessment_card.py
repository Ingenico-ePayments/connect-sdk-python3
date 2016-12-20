#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.riskassessments.definitions.risk_assessment import RiskAssessment


class RiskAssessmentCard(RiskAssessment):
    """
    Class RiskAssessmentCard
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RiskAssessmentCard
    """

    __card = None

    @property
    def card(self):
        """
        :class:`Card`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    def to_dictionary(self):
        dictionary = super(RiskAssessmentCard, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'card', self.card)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RiskAssessmentCard, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        return self
