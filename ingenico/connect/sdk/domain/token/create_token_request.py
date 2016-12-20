#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.token.definitions.token_card import TokenCard
from ingenico.connect.sdk.domain.token.definitions.token_e_wallet import TokenEWallet
from ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit import TokenNonSepaDirectDebit
from ingenico.connect.sdk.domain.token.definitions.token_sepa_direct_debit_without_creditor import TokenSepaDirectDebitWithoutCreditor


class CreateTokenRequest(DataObject):
    """
    Class CreateTokenRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreateTokenRequest
    """

    __card = None
    __e_wallet = None
    __non_sepa_direct_debit = None
    __payment_product_id = None
    __sepa_direct_debit = None

    @property
    def card(self):
        """
        :class:`TokenCard`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def e_wallet(self):
        """
        :class:`TokenEWallet`
        """
        return self.__e_wallet

    @e_wallet.setter
    def e_wallet(self, value):
        self.__e_wallet = value

    @property
    def non_sepa_direct_debit(self):
        """
        :class:`TokenNonSepaDirectDebit`
        """
        return self.__non_sepa_direct_debit

    @non_sepa_direct_debit.setter
    def non_sepa_direct_debit(self, value):
        self.__non_sepa_direct_debit = value

    @property
    def payment_product_id(self):
        """
        int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    @property
    def sepa_direct_debit(self):
        """
        :class:`TokenSepaDirectDebitWithoutCreditor`
        """
        return self.__sepa_direct_debit

    @sepa_direct_debit.setter
    def sepa_direct_debit(self, value):
        self.__sepa_direct_debit = value

    def to_dictionary(self):
        dictionary = super(CreateTokenRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'card', self.card)
        self._add_to_dictionary(dictionary, 'eWallet', self.e_wallet)
        self._add_to_dictionary(dictionary, 'nonSepaDirectDebit', self.non_sepa_direct_debit)
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        self._add_to_dictionary(dictionary, 'sepaDirectDebit', self.sepa_direct_debit)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateTokenRequest, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = TokenCard()
            self.card = value.from_dictionary(dictionary['card'])
        if 'eWallet' in dictionary:
            if not isinstance(dictionary['eWallet'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eWallet']))
            value = TokenEWallet()
            self.e_wallet = value.from_dictionary(dictionary['eWallet'])
        if 'nonSepaDirectDebit' in dictionary:
            if not isinstance(dictionary['nonSepaDirectDebit'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['nonSepaDirectDebit']))
            value = TokenNonSepaDirectDebit()
            self.non_sepa_direct_debit = value.from_dictionary(dictionary['nonSepaDirectDebit'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'sepaDirectDebit' in dictionary:
            if not isinstance(dictionary['sepaDirectDebit'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebit']))
            value = TokenSepaDirectDebitWithoutCreditor()
            self.sepa_direct_debit = value.from_dictionary(dictionary['sepaDirectDebit'])
        return self
