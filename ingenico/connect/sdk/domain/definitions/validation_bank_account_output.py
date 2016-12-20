#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.validation_bank_account_check import ValidationBankAccountCheck


class ValidationBankAccountOutput(DataObject):
    """
    Class ValidationBankAccountOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ValidationBankAccountOutput
    """

    __checks = None
    __new_bank_name = None
    __reformatted_account_number = None
    __reformatted_bank_code = None
    __reformatted_branch_code = None

    @property
    def checks(self):
        """
        list[:class:`ValidationBankAccountCheck`]
        """
        return self.__checks

    @checks.setter
    def checks(self, value):
        self.__checks = value

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
        dictionary = super(ValidationBankAccountOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'checks', self.checks)
        self._add_to_dictionary(dictionary, 'newBankName', self.new_bank_name)
        self._add_to_dictionary(dictionary, 'reformattedAccountNumber', self.reformatted_account_number)
        self._add_to_dictionary(dictionary, 'reformattedBankCode', self.reformatted_bank_code)
        self._add_to_dictionary(dictionary, 'reformattedBranchCode', self.reformatted_branch_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ValidationBankAccountOutput, self).from_dictionary(dictionary)
        if 'checks' in dictionary:
            if not isinstance(dictionary['checks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['checks']))
            self.checks = []
            for checks_element in dictionary['checks']:
                checks_value = ValidationBankAccountCheck()
                self.checks.append(checks_value.from_dictionary(checks_element))
        if 'newBankName' in dictionary:
            self.new_bank_name = dictionary['newBankName']
        if 'reformattedAccountNumber' in dictionary:
            self.reformatted_account_number = dictionary['reformattedAccountNumber']
        if 'reformattedBankCode' in dictionary:
            self.reformatted_bank_code = dictionary['reformattedBankCode']
        if 'reformattedBranchCode' in dictionary:
            self.reformatted_branch_code = dictionary['reformattedBranchCode']
        return self
