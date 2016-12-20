#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.card_essentials import CardEssentials


class CardWithoutCvv(CardEssentials):
    """
    Class CardWithoutCvv
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardWithoutCvv
    """

    __cardholder_name = None
    __issue_number = None

    @property
    def cardholder_name(self):
        """
        str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value

    @property
    def issue_number(self):
        """
        str
        """
        return self.__issue_number

    @issue_number.setter
    def issue_number(self, value):
        self.__issue_number = value

    def to_dictionary(self):
        dictionary = super(CardWithoutCvv, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardholderName', self.cardholder_name)
        self._add_to_dictionary(dictionary, 'issueNumber', self.issue_number)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardWithoutCvv, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'issueNumber' in dictionary:
            self.issue_number = dictionary['issueNumber']
        return self
