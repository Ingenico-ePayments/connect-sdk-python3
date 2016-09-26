#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban


class TokenNonSepaDirectDebitPaymentProduct705SpecificData(DataObject):
    """
    Class TokenNonSepaDirectDebitPaymentProduct705SpecificData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenNonSepaDirectDebitPaymentProduct705SpecificData
    
    Attributes:
        authorisation_id:   str
        bank_account_bban:  :class:`BankAccountBban`
     """

    authorisation_id = None
    bank_account_bban = None

    def to_dictionary(self):
        dictionary = super(TokenNonSepaDirectDebitPaymentProduct705SpecificData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'authorisationId', self.authorisation_id)
        self._add_to_dictionary(dictionary, 'bankAccountBban', self.bank_account_bban)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenNonSepaDirectDebitPaymentProduct705SpecificData, self).from_dictionary(dictionary)
        if 'authorisationId' in dictionary:
            self.authorisation_id = dictionary['authorisationId']
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        return self
