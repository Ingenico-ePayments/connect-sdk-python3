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
    
    Attributes:
        card:                   :class:`TokenCard`
        e_wallet:               :class:`TokenEWallet`
        non_sepa_direct_debit:  :class:`TokenNonSepaDirectDebit`
        payment_product_id:     int
        sepa_direct_debit:      :class:`TokenSepaDirectDebitWithoutCreditor`
     """

    card = None
    e_wallet = None
    non_sepa_direct_debit = None
    payment_product_id = None
    sepa_direct_debit = None

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
