#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class BankData(DataObject):
    """
    Class BankData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankData
    """

    __new_bank_name = None
    __reformatted_account_number = None
    __reformatted_bank_code = None
    __reformatted_branch_code = None

    @property
    def new_bank_name(self):
        """
        str
        """
        return self.__new_bank_name

    @new_bank_name.setter
    def new_bank_name(self, value):
        self.__new_bank_name = value

    @property
    def reformatted_account_number(self):
        """
        str
        """
        return self.__reformatted_account_number

    @reformatted_account_number.setter
    def reformatted_account_number(self, value):
        self.__reformatted_account_number = value

    @property
    def reformatted_bank_code(self):
        """
        str
        """
        return self.__reformatted_bank_code

    @reformatted_bank_code.setter
    def reformatted_bank_code(self, value):
        self.__reformatted_bank_code = value

    @property
    def reformatted_branch_code(self):
        """
        str
        """
        return self.__reformatted_branch_code

    @reformatted_branch_code.setter
    def reformatted_branch_code(self, value):
        self.__reformatted_branch_code = value

    def to_dictionary(self):
        dictionary = super(BankData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'newBankName', self.new_bank_name)
        self._add_to_dictionary(dictionary, 'reformattedAccountNumber', self.reformatted_account_number)
        self._add_to_dictionary(dictionary, 'reformattedBankCode', self.reformatted_bank_code)
        self._add_to_dictionary(dictionary, 'reformattedBranchCode', self.reformatted_branch_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankData, self).from_dictionary(dictionary)
        if 'newBankName' in dictionary:
            self.new_bank_name = dictionary['newBankName']
        if 'reformattedAccountNumber' in dictionary:
            self.reformatted_account_number = dictionary['reformattedAccountNumber']
        if 'reformattedBankCode' in dictionary:
            self.reformatted_bank_code = dictionary['reformattedBankCode']
        if 'reformattedBranchCode' in dictionary:
            self.reformatted_branch_code = dictionary['reformattedBranchCode']
        return self
