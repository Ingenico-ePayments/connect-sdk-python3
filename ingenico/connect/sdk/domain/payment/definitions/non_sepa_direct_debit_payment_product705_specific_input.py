#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban


class NonSepaDirectDebitPaymentProduct705SpecificInput(DataObject):
    """
    Class NonSepaDirectDebitPaymentProduct705SpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_NonSepaDirectDebitPaymentProduct705SpecificInput
    
    Attributes:
        authorisation_id:   str
        bank_account_bban:  :class:`BankAccountBban`
        transaction_type:   str
     """

    authorisation_id = None
    bank_account_bban = None
    transaction_type = None

    def to_dictionary(self):
        dictionary = super(NonSepaDirectDebitPaymentProduct705SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'authorisationId', self.authorisation_id)
        self._add_to_dictionary(dictionary, 'bankAccountBban', self.bank_account_bban)
        self._add_to_dictionary(dictionary, 'transactionType', self.transaction_type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(NonSepaDirectDebitPaymentProduct705SpecificInput, self).from_dictionary(dictionary)
        if 'authorisationId' in dictionary:
            self.authorisation_id = dictionary['authorisationId']
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        if 'transactionType' in dictionary:
            self.transaction_type = dictionary['transactionType']
        return self
