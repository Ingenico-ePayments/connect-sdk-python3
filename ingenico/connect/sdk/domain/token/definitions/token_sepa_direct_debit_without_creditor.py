#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.token.definitions.abstract_token import AbstractToken
from ingenico.connect.sdk.domain.token.definitions.customer_token_with_contact_details import CustomerTokenWithContactDetails
from ingenico.connect.sdk.domain.token.definitions.mandate_sepa_direct_debit_without_creditor import MandateSepaDirectDebitWithoutCreditor


class TokenSepaDirectDebitWithoutCreditor(AbstractToken):
    """
    Class TokenSepaDirectDebitWithoutCreditor
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenSepaDirectDebitWithoutCreditor
    
    Attributes:
        customer:  :class:`CustomerTokenWithContactDetails`
        mandate:   :class:`MandateSepaDirectDebitWithoutCreditor`
     """

    customer = None
    mandate = None

    def to_dictionary(self):
        dictionary = super(TokenSepaDirectDebitWithoutCreditor, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'mandate', self.mandate)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenSepaDirectDebitWithoutCreditor, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerTokenWithContactDetails()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateSepaDirectDebitWithoutCreditor()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
