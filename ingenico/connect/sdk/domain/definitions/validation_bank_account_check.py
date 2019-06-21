# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ValidationBankAccountCheck(DataObject):

    __code = None
    __description = None
    __result = None

    @property
    def code(self):
        """
        | Code of the bank account validation check
        
        Type: str
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def description(self):
        """
        | Description of check performed
        
        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def result(self):
        """
        | Result of the bank account validation check performed, with the following possible results:
        
        * PASSED - The check passed
        * ERROR - The check did not pass
        * WARNING - Depending on your needs this either needs to be treated as a passed or error response. It depends on your business logic and for what purpose you want to use the validated bank account details.
        * NOTCHECKED - This check was not performed, usually because one of the earlier checks already caused an error response to be triggered
        
        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    def to_dictionary(self):
        dictionary = super(ValidationBankAccountCheck, self).to_dictionary()
        if self.code is not None:
            dictionary['code'] = self.code
        if self.description is not None:
            dictionary['description'] = self.description
        if self.result is not None:
            dictionary['result'] = self.result
        return dictionary

    def from_dictionary(self, dictionary):
        super(ValidationBankAccountCheck, self).from_dictionary(dictionary)
        if 'code' in dictionary:
            self.code = dictionary['code']
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'result' in dictionary:
            self.result = dictionary['result']
        return self
