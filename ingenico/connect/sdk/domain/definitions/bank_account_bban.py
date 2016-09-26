#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.bank_account import BankAccount


class BankAccountBban(BankAccount):
    """
    Class BankAccountBban
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankAccountBban
    
    Attributes:
        account_number:  str
        bank_code:       str
        bank_name:       str
        branch_code:     str
        check_digit:     str
        country_code:    str
     """

    account_number = None
    bank_code = None
    bank_name = None
    branch_code = None
    check_digit = None
    country_code = None

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
