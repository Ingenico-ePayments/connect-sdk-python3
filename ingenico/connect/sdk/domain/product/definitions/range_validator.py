#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RangeValidator(DataObject):
    """
    Class RangeValidator
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RangeValidator
    
    Attributes:
        max_value:  int
        min_value:  int
     """

    max_value = None
    min_value = None

    def to_dictionary(self):
        dictionary = super(RangeValidator, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'maxValue', self.max_value)
        self._add_to_dictionary(dictionary, 'minValue', self.min_value)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RangeValidator, self).from_dictionary(dictionary)
        if 'maxValue' in dictionary:
            self.max_value = dictionary['maxValue']
        if 'minValue' in dictionary:
            self.min_value = dictionary['minValue']
        return self
