#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CreateTokenResponse(DataObject):
    """
    Class CreateTokenResponse
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreateTokenResponse
    
    Attributes:
        is_new_token:  bool
        token:         str
     """

    is_new_token = None
    token = None

    def to_dictionary(self):
        dictionary = super(CreateTokenResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'isNewToken', self.is_new_token)
        self._add_to_dictionary(dictionary, 'token', self.token)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateTokenResponse, self).from_dictionary(dictionary)
        if 'isNewToken' in dictionary:
            self.is_new_token = dictionary['isNewToken']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
