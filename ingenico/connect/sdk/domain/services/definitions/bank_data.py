# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class BankData(DataObject):

    __new_bank_name = None
    __reformatted_account_number = None
    __reformatted_bank_code = None
    __reformatted_branch_code = None

    @property
    def new_bank_name(self):
        """
        | Bank name, matching the bank code of the request
        
        Type: str
        """
        return self.__new_bank_name

    @new_bank_name.setter
    def new_bank_name(self, value):
        self.__new_bank_name = value

    @property
    def reformatted_account_number(self):
        """
        | Reformatted account number according to local clearing rules
        
        Type: str
        """
        return self.__reformatted_account_number

    @reformatted_account_number.setter
    def reformatted_account_number(self, value):
        self.__reformatted_account_number = value

    @property
    def reformatted_bank_code(self):
        """
        | Reformatted bank code according to local clearing rules
        
        Type: str
        """
        return self.__reformatted_bank_code

    @reformatted_bank_code.setter
    def reformatted_bank_code(self, value):
        self.__reformatted_bank_code = value

    @property
    def reformatted_branch_code(self):
        """
        | Reformatted branch code according to local clearing rules
        
        Type: str
        """
        return self.__reformatted_branch_code

    @reformatted_branch_code.setter
    def reformatted_branch_code(self, value):
        self.__reformatted_branch_code = value

    def to_dictionary(self):
        dictionary = super(BankData, self).to_dictionary()
        if self.new_bank_name is not None:
            dictionary['newBankName'] = self.new_bank_name
        if self.reformatted_account_number is not None:
            dictionary['reformattedAccountNumber'] = self.reformatted_account_number
        if self.reformatted_bank_code is not None:
            dictionary['reformattedBankCode'] = self.reformatted_bank_code
        if self.reformatted_branch_code is not None:
            dictionary['reformattedBranchCode'] = self.reformatted_branch_code
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
