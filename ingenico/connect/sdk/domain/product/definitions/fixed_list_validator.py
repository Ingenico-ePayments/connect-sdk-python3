#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class FixedListValidator(DataObject):
    """
    Class FixedListValidator
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_FixedListValidator
    """

    __allowed_values = None

    @property
    def allowed_values(self):
        """
        list[str]
        """
        return self.__allowed_values

    @allowed_values.setter
    def allowed_values(self, value):
        self.__allowed_values = value

    def to_dictionary(self):
        dictionary = super(FixedListValidator, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'allowedValues', self.allowed_values)
        return dictionary

    def from_dictionary(self, dictionary):
        super(FixedListValidator, self).from_dictionary(dictionary)
        if 'allowedValues' in dictionary:
            if not isinstance(dictionary['allowedValues'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['allowedValues']))
            self.allowed_values = []
            for allowedValues_element in dictionary['allowedValues']:
                self.allowed_values.append(allowedValues_element)
        return self
