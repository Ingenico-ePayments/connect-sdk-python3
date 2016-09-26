#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class BankData(DataObject):
    """
    Class BankData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankData
    
    Attributes:
        new_bank_name:               str
        reformatted_account_number:  str
        reformatted_bank_code:       str
        reformatted_branch_code:     str
     """

    new_bank_name = None
    reformatted_account_number = None
    reformatted_bank_code = None
    reformatted_branch_code = None

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
