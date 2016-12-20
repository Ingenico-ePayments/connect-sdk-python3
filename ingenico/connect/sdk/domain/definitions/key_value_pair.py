#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class KeyValuePair(DataObject):
    """
    Class KeyValuePair
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_KeyValuePair
    """

    __key = None
    __value = None

    @property
    def key(self):
        """
        str
        """
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

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
        dictionary = super(KeyValuePair, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'key', self.key)
        self._add_to_dictionary(dictionary, 'value', self.value)
        return dictionary

    def from_dictionary(self, dictionary):
        super(KeyValuePair, self).from_dictionary(dictionary)
        if 'key' in dictionary:
            self.key = dictionary['key']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
