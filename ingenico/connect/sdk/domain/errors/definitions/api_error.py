#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class APIError(DataObject):
    """
    Class APIError
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_APIError
    """

    __category = None
    __code = None
    __http_status_code = None
    __id = None
    __message = None
    __property_name = None
    __request_id = None

    @property
    def category(self):
        """
        str
        """
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def code(self):
        """
        str
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def http_status_code(self):
        """
        int
        """
        return self.__http_status_code

    @http_status_code.setter
    def http_status_code(self, value):
        self.__http_status_code = value

    @property
    def id(self):
        """
        str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def message(self):
        """
        str
        """
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def property_name(self):
        """
        str
        """
        return self.__property_name

    @property_name.setter
    def property_name(self, value):
        self.__property_name = value

    @property
    def request_id(self):
        """
        str
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value

    def to_dictionary(self):
        dictionary = super(APIError, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'category', self.category)
        self._add_to_dictionary(dictionary, 'code', self.code)
        self._add_to_dictionary(dictionary, 'httpStatusCode', self.http_status_code)
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'message', self.message)
        self._add_to_dictionary(dictionary, 'propertyName', self.property_name)
        self._add_to_dictionary(dictionary, 'requestId', self.request_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(APIError, self).from_dictionary(dictionary)
        if 'category' in dictionary:
            self.category = dictionary['category']
        if 'code' in dictionary:
            self.code = dictionary['code']
        if 'httpStatusCode' in dictionary:
            self.http_status_code = dictionary['httpStatusCode']
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'message' in dictionary:
            self.message = dictionary['message']
        if 'propertyName' in dictionary:
            self.property_name = dictionary['propertyName']
        if 'requestId' in dictionary:
            self.request_id = dictionary['requestId']
        return self
