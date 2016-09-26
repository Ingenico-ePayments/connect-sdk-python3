#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.services.definitions.bank_data import BankData
from ingenico.connect.sdk.domain.services.definitions.swift import Swift


class BankDetailsResponse(DataObject):
    """
    Class BankDetailsResponse
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankDetailsResponse
    
    Attributes:
        bank_account_bban:  :class:`BankAccountBban`
        bank_account_iban:  :class:`BankAccountIban`
        bank_data:          :class:`BankData`
        swift:              :class:`Swift`
     """

    bank_account_bban = None
    bank_account_iban = None
    bank_data = None
    swift = None

    def to_dictionary(self):
        dictionary = super(BankDetailsResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankAccountBban', self.bank_account_bban)
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        self._add_to_dictionary(dictionary, 'bankData', self.bank_data)
        self._add_to_dictionary(dictionary, 'swift', self.swift)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankDetailsResponse, self).from_dictionary(dictionary)
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'bankData' in dictionary:
            if not isinstance(dictionary['bankData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankData']))
            value = BankData()
            self.bank_data = value.from_dictionary(dictionary['bankData'])
        if 'swift' in dictionary:
            if not isinstance(dictionary['swift'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['swift']))
            value = Swift()
            self.swift = value.from_dictionary(dictionary['swift'])
        return self
