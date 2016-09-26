#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PersonalNameBase(DataObject):
    """
    Class PersonalNameBase
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PersonalNameBase
    
    Attributes:
        first_name:      str
        surname:         str
        surname_prefix:  str
     """

    first_name = None
    surname = None
    surname_prefix = None

    def to_dictionary(self):
        dictionary = super(PersonalNameBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'firstName', self.first_name)
        self._add_to_dictionary(dictionary, 'surname', self.surname)
        self._add_to_dictionary(dictionary, 'surnamePrefix', self.surname_prefix)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalNameBase, self).from_dictionary(dictionary)
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'surnamePrefix' in dictionary:
            self.surname_prefix = dictionary['surnamePrefix']
        return self
