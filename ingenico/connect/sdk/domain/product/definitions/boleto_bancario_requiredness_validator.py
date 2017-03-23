#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class BoletoBancarioRequirednessValidator(DataObject):
    """
    Class BoletoBancarioRequirednessValidator
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BoletoBancarioRequirednessValidator
    """

    __fiscal_number_length = None

    @property
    def fiscal_number_length(self):
        """
        int
        """
        return self.__fiscal_number_length

    @fiscal_number_length.setter
    def fiscal_number_length(self, value):
        self.__fiscal_number_length = value

    def to_dictionary(self):
        dictionary = super(BoletoBancarioRequirednessValidator, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'fiscalNumberLength', self.fiscal_number_length)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BoletoBancarioRequirednessValidator, self).from_dictionary(dictionary)
        if 'fiscalNumberLength' in dictionary:
            self.fiscal_number_length = dictionary['fiscalNumberLength']
        return self
