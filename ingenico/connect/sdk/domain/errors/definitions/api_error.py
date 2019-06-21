# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class APIError(DataObject):

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
        | Category the error belongs to. The category should give an indication of the type of error you are dealing with.Possible values:
        
        * CONNECT_PLATFORM_ERROR - indicating that a functional error has occurred in the Connect platform.
        * PAYMENT_PLATFORM_ERROR - indicating that a functional error has occurred in the Payment platform.
        * IO_ERROR - indicating that a technical error has occurred within the Connect platform or between Connect and any of the payment platforms or third party systems.
        
        Type: str
        """
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def code(self):
        """
        | Error code
        
        Type: str
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def http_status_code(self):
        """
        | HTTP status code for this error that can be used to determine the type of error
        
        Type: int
        """
        return self.__http_status_code

    @http_status_code.setter
    def http_status_code(self, value):
        self.__http_status_code = value

    @property
    def id(self):
        """
        | ID of the error. This is a short human-readable message that briefly describes the error.
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def message(self):
        """
        | Human-readable error message that is not meant to be relayed to customer as it might tip off people who are trying to commit fraud
        
        Type: str
        """
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def property_name(self):
        """
        | Returned only if the error relates to a value that was missing or incorrect.
        | Contains a location path to the value as a JSonata query <http://docs.jsonata.org/basic.html>.
        | Some common examples:
        
        * a.b selects the value of property b of root property a,
        * a[1] selects the first element of the array in root property a,
        * a[b='some value'] selects all elements of the array in root property a that have a property b with value 'some value'.
        
        Type: str
        """
        return self.__property_name

    @property_name.setter
    def property_name(self, value):
        self.__property_name = value

    @property
    def request_id(self):
        """
        | ID of the request that can be used for debugging purposes
        
        Type: str
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value

    def to_dictionary(self):
        dictionary = super(APIError, self).to_dictionary()
        if self.category is not None:
            dictionary['category'] = self.category
        if self.code is not None:
            dictionary['code'] = self.code
        if self.http_status_code is not None:
            dictionary['httpStatusCode'] = self.http_status_code
        if self.id is not None:
            dictionary['id'] = self.id
        if self.message is not None:
            dictionary['message'] = self.message
        if self.property_name is not None:
            dictionary['propertyName'] = self.property_name
        if self.request_id is not None:
            dictionary['requestId'] = self.request_id
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
