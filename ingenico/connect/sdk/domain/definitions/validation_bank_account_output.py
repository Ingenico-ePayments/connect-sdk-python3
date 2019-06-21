# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.validation_bank_account_check import ValidationBankAccountCheck


class ValidationBankAccountOutput(DataObject):

    __checks = None
    __new_bank_name = None
    __reformatted_account_number = None
    __reformatted_bank_code = None
    __reformatted_branch_code = None

    @property
    def checks(self):
        """
        | Array of checks performed with the results of each check
        
        Type: list[:class:`ingenico.connect.sdk.domain.definitions.validation_bank_account_check.ValidationBankAccountCheck`]
        """
        return self.__checks

    @checks.setter
    def checks(self, value):
        self.__checks = value

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
        dictionary = super(ValidationBankAccountOutput, self).to_dictionary()
        if self.checks is not None:
            dictionary['checks'] = []
            for element in self.checks:
                if element is not None:
                    dictionary['checks'].append(element.to_dictionary())
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
        super(ValidationBankAccountOutput, self).from_dictionary(dictionary)
        if 'checks' in dictionary:
            if not isinstance(dictionary['checks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['checks']))
            self.checks = []
            for element in dictionary['checks']:
                value = ValidationBankAccountCheck()
                self.checks.append(value.from_dictionary(element))
        if 'newBankName' in dictionary:
            self.new_bank_name = dictionary['newBankName']
        if 'reformattedAccountNumber' in dictionary:
            self.reformatted_account_number = dictionary['reformattedAccountNumber']
        if 'reformattedBankCode' in dictionary:
            self.reformatted_bank_code = dictionary['reformattedBankCode']
        if 'reformattedBranchCode' in dictionary:
            self.reformatted_branch_code = dictionary['reformattedBranchCode']
        return self
