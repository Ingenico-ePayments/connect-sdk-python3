#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.token.definitions.abstract_token import AbstractToken
from ingenico.connect.sdk.domain.token.definitions.customer_token import CustomerToken
from ingenico.connect.sdk.domain.token.definitions.token_card_data import TokenCardData


class TokenCard(AbstractToken):
    """
    Class TokenCard
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenCard
    """

    __customer = None
    __data = None

    @property
    def customer(self):
        """
        :class:`CustomerToken`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def data(self):
        """
        :class:`TokenCardData`
        """
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def to_dictionary(self):
        dictionary = super(TokenCard, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'data', self.data)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenCard, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerToken()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenCardData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
