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
    """

    __card_without_cvv = None
    __first_transaction_date = None
    __provider_reference = None

    @property
    def card_without_cvv(self):
        """
        :class:`CardWithoutCvv`
        """
        return self.__card_without_cvv

    @card_without_cvv.setter
    def card_without_cvv(self, value):
        self.__card_without_cvv = value

    @property
    def first_transaction_date(self):
        """
        str
        """
        return self.__first_transaction_date

    @first_transaction_date.setter
    def first_transaction_date(self, value):
        self.__first_transaction_date = value

    @property
    def provider_reference(self):
        """
        str
        """
        return self.__provider_reference

    @provider_reference.setter
    def provider_reference(self, value):
        self.__provider_reference = value

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
