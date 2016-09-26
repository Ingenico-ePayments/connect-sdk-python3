#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class SessionRequest(DataObject):
    """
    Class SessionRequest
    See also https://developer.globalcollect.com/documentation/api/server/#schema_SessionRequest
    
    Attributes:
        tokens:  list[str]
     """

    tokens = None

    def to_dictionary(self):
        dictionary = super(SessionRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'tokens', self.tokens)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SessionRequest, self).from_dictionary(dictionary)
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for tokens_element in dictionary['tokens']:
                self.tokens.append(tokens_element)
        return self
