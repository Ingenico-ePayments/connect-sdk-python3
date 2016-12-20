#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.refund.definitions.bank_account_bban_refund import BankAccountBbanRefund


class BankRefundMethodSpecificInput(DataObject):
    """
    Class BankRefundMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankRefundMethodSpecificInput
    """

    __bank_account_bban = None
    __bank_account_iban = None
    __country_code = None

    @property
    def bank_account_bban(self):
        """
        :class:`BankAccountBbanRefund`
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
    def country_code(self):
        """
        str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    def to_dictionary(self):
        dictionary = super(BankRefundMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankAccountBban', self.bank_account_bban)
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankRefundMethodSpecificInput, self).from_dictionary(dictionary)
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBbanRefund()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        return self
