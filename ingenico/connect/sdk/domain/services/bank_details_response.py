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
    """

    __bank_account_bban = None
    __bank_account_iban = None
    __bank_data = None
    __swift = None

    @property
    def bank_account_bban(self):
        """
        :class:`BankAccountBban`
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value):
        self.__bank_account_bban = value

    @property
    def bank_account_iban(self):
        """
        :class:`BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value):
        self.__bank_account_iban = value

    @property
    def bank_data(self):
        """
        :class:`BankData`
        """
        return self.__bank_data

    @bank_data.setter
    def bank_data(self, value):
        self.__bank_data = value

    @property
    def swift(self):
        """
        :class:`Swift`
        """
        return self.__swift

    @swift.setter
    def swift(self, value):
        self.__swift = value

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
