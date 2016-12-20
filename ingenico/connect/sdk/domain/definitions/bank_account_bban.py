#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.bank_account import BankAccount


class BankAccountBban(BankAccount):
    """
    Class BankAccountBban
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankAccountBban
    """

    __account_number = None
    __bank_code = None
    __bank_name = None
    __branch_code = None
    __check_digit = None
    __country_code = None

    @property
    def account_number(self):
        """
        str
        """
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def bank_code(self):
        """
        str
        """
        return self.__bank_code

    @bank_code.setter
    def bank_code(self, value):
        self.__bank_code = value

    @property
    def bank_name(self):
        """
        str
        """
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = value

    @property
    def branch_code(self):
        """
        str
        """
        return self.__branch_code

    @branch_code.setter
    def branch_code(self, value):
        self.__branch_code = value

    @property
    def check_digit(self):
        """
        str
        """
        return self.__check_digit

    @check_digit.setter
    def check_digit(self, value):
        self.__check_digit = value

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
        dictionary = super(BankAccountBban, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'accountNumber', self.account_number)
        self._add_to_dictionary(dictionary, 'bankCode', self.bank_code)
        self._add_to_dictionary(dictionary, 'bankName', self.bank_name)
        self._add_to_dictionary(dictionary, 'branchCode', self.branch_code)
        self._add_to_dictionary(dictionary, 'checkDigit', self.check_digit)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccountBban, self).from_dictionary(dictionary)
        if 'accountNumber' in dictionary:
            self.account_number = dictionary['accountNumber']
        if 'bankCode' in dictionary:
            self.bank_code = dictionary['bankCode']
        if 'bankName' in dictionary:
            self.bank_name = dictionary['bankName']
        if 'branchCode' in dictionary:
            self.branch_code = dictionary['branchCode']
        if 'checkDigit' in dictionary:
            self.check_digit = dictionary['checkDigit']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        return self
