#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ValidationBankAccountCheck(DataObject):
    """
    Class ValidationBankAccountCheck
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ValidationBankAccountCheck
    
    Attributes:
        code:         str
        description:  str
        result:       str
     """

    code = None
    description = None
    result = None

    def to_dictionary(self):
        dictionary = super(ValidationBankAccountCheck, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'code', self.code)
        self._add_to_dictionary(dictionary, 'description', self.description)
        self._add_to_dictionary(dictionary, 'result', self.result)
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
