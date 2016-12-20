#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RangeValidator(DataObject):
    """
    Class RangeValidator
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RangeValidator
    """

    __max_value = None
    __min_value = None

    @property
    def max_value(self):
        """
        int
        """
        return self.__max_value

    @max_value.setter
    def max_value(self, value):
        self.__max_value = value

    @property
    def min_value(self):
        """
        int
        """
        return self.__min_value

    @min_value.setter
    def min_value(self, value):
        self.__min_value = value

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
