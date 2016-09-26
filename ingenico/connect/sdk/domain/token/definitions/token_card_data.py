#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.card_without_cvv import CardWithoutCvv


class TokenCardData(DataObject):
    """
    Class TokenCardData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenCardData
    
    Attributes:
        card_without_cvv:        :class:`CardWithoutCvv`
        first_transaction_date:  str
        provider_reference:      str
     """

    card_without_cvv = None
    first_transaction_date = None
    provider_reference = None

    def to_dictionary(self):
        dictionary = super(TokenCardData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardWithoutCvv', self.card_without_cvv)
        self._add_to_dictionary(dictionary, 'firstTransactionDate', self.first_transaction_date)
        self._add_to_dictionary(dictionary, 'providerReference', self.provider_reference)
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
