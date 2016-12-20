#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban


class BankDetails(DataObject):
    """
    Class BankDetails
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankDetails
    """

    __bank_account_bban = None
    __bank_account_iban = None

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

    def to_dictionary(self):
        dictionary = super(BankDetails, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankAccountBban', self.bank_account_bban)
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankDetails, self).from_dictionary(dictionary)
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
        return self
