#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.token.definitions.abstract_token import AbstractToken
from ingenico.connect.sdk.domain.token.definitions.customer_token import CustomerToken
from ingenico.connect.sdk.domain.token.definitions.token_e_wallet_data import TokenEWalletData


class TokenEWallet(AbstractToken):
    """
    Class TokenEWallet
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenEWallet
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
        :class:`TokenEWalletData`
        """
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def to_dictionary(self):
        dictionary = super(TokenEWallet, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'data', self.data)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenEWallet, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerToken()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenEWalletData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
