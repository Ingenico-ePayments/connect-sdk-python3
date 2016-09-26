#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class APIError(DataObject):
    """
    Class APIError
    See also https://developer.globalcollect.com/documentation/api/server/#schema_APIError
    
    Attributes:
        code:              str
        http_status_code:  int
        message:           str
        property_name:     str
        request_id:        str
     """

    code = None
    http_status_code = None
    message = None
    property_name = None
    request_id = None

    def to_dictionary(self):
        dictionary = super(APIError, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'code', self.code)
        self._add_to_dictionary(dictionary, 'httpStatusCode', self.http_status_code)
        self._add_to_dictionary(dictionary, 'message', self.message)
        self._add_to_dictionary(dictionary, 'propertyName', self.property_name)
        self._add_to_dictionary(dictionary, 'requestId', self.request_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(APIError, self).from_dictionary(dictionary)
        if 'code' in dictionary:
            self.code = dictionary['code']
        if 'httpStatusCode' in dictionary:
            self.http_status_code = dictionary['httpStatusCode']
        if 'message' in dictionary:
            self.message = dictionary['message']
        if 'propertyName' in dictionary:
            self.property_name = dictionary['propertyName']
        if 'requestId' in dictionary:
            self.request_id = dictionary['requestId']
        return self
