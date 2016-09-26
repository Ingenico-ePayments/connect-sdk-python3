#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class TestConnection(DataObject):
    """
    Class TestConnection
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TestConnection
    
    Attributes:
        result:  str
     """

    result = None

    def to_dictionary(self):
        dictionary = super(TestConnection, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'result', self.result)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TestConnection, self).from_dictionary(dictionary)
        if 'result' in dictionary:
            self.result = dictionary['result']
        return self
