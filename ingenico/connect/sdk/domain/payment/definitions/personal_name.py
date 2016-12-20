#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.personal_name_base import PersonalNameBase


class PersonalName(PersonalNameBase):
    """
    Class PersonalName
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PersonalName
    """

    __title = None

    @property
    def title(self):
        """
        str
        """
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def to_dictionary(self):
        dictionary = super(PersonalName, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'title', self.title)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalName, self).from_dictionary(dictionary)
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
