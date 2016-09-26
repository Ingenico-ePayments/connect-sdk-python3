#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.personal_name import PersonalName


class PersonalInformation(DataObject):
    """
    Class PersonalInformation
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PersonalInformation
    
    Attributes:
        date_of_birth:  str
        gender:         str
        name:           :class:`PersonalName`
     """

    date_of_birth = None
    gender = None
    name = None

    def to_dictionary(self):
        dictionary = super(PersonalInformation, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dateOfBirth', self.date_of_birth)
        self._add_to_dictionary(dictionary, 'gender', self.gender)
        self._add_to_dictionary(dictionary, 'name', self.name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalInformation, self).from_dictionary(dictionary)
        if 'dateOfBirth' in dictionary:
            self.date_of_birth = dictionary['dateOfBirth']
        if 'gender' in dictionary:
            self.gender = dictionary['gender']
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        return self
