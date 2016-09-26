#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ValueMappingElement(DataObject):
    """
    Class ValueMappingElement
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ValueMappingElement
    
    Attributes:
        display_name:  str
        value:         str
     """

    display_name = None
    value = None

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
