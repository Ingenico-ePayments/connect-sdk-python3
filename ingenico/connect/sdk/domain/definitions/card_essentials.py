#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CardEssentials(DataObject):
    """
    Class CardEssentials
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardEssentials
    
    Attributes:
        card_number:  str
        expiry_date:  str
     """

    card_number = None
    expiry_date = None

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
