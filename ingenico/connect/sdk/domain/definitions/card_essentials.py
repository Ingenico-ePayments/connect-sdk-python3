#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CardEssentials(DataObject):
    """
    Class CardEssentials
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardEssentials
    """

    __card_number = None
    __expiry_date = None

    @property
    def card_number(self):
        """
        str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value):
        self.__card_number = value

    @property
    def expiry_date(self):
        """
        str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    def to_dictionary(self):
        dictionary = super(CardEssentials, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardNumber', self.card_number)
        self._add_to_dictionary(dictionary, 'expiryDate', self.expiry_date)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardEssentials, self).from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
