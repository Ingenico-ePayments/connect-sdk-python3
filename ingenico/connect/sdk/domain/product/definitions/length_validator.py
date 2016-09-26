#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class LengthValidator(DataObject):
    """
    Class LengthValidator
    See also https://developer.globalcollect.com/documentation/api/server/#schema_LengthValidator
    
    Attributes:
        max_length:  int
        min_length:  int
     """

    max_length = None
    min_length = None

    def to_dictionary(self):
        dictionary = super(LengthValidator, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'maxLength', self.max_length)
        self._add_to_dictionary(dictionary, 'minLength', self.min_length)
        return dictionary

    def from_dictionary(self, dictionary):
        super(LengthValidator, self).from_dictionary(dictionary)
        if 'maxLength' in dictionary:
            self.max_length = dictionary['maxLength']
        if 'minLength' in dictionary:
            self.min_length = dictionary['minLength']
        return self
