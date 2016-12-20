#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ValueMappingElement(DataObject):
    """
    Class ValueMappingElement
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ValueMappingElement
    """

    __display_name = None
    __value = None

    @property
    def display_name(self):
        """
        str
        """
        return self.__display_name

    @display_name.setter
    def display_name(self, value):
        self.__display_name = value

    @property
    def value(self):
        """
        str
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(ValueMappingElement, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'displayName', self.display_name)
        self._add_to_dictionary(dictionary, 'value', self.value)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ValueMappingElement, self).from_dictionary(dictionary)
        if 'displayName' in dictionary:
            self.display_name = dictionary['displayName']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
