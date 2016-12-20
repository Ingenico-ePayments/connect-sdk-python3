#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.personal_name_base import PersonalNameBase


class PersonalNameToken(PersonalNameBase):
    """
    Class PersonalNameToken
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PersonalNameToken
    """

    def to_dictionary(self):
        dictionary = super(PersonalNameToken, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalNameToken, self).from_dictionary(dictionary)
        return self
