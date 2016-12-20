#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.card_without_cvv import CardWithoutCvv


class Card(CardWithoutCvv):
    """
    Class Card
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Card
    """

    __cvv = None

    @property
    def cvv(self):
        """
        str
        """
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    def to_dictionary(self):
        dictionary = super(Card, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cvv', self.cvv)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Card, self).from_dictionary(dictionary)
        if 'cvv' in dictionary:
            self.cvv = dictionary['cvv']
        return self
