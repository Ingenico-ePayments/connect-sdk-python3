#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class EmptyValidator(DataObject):
    """
    Class EmptyValidator
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_EmptyValidator
    """

    def to_dictionary(self):
        dictionary = super(EmptyValidator, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(EmptyValidator, self).from_dictionary(dictionary)
        return self
