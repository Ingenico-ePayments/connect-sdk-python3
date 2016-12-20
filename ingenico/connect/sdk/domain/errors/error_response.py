#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.errors.definitions.api_error import APIError


class ErrorResponse(DataObject):
    """
    Class ErrorResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ErrorResponse
    """

    __error_id = None
    __errors = None

    @property
    def error_id(self):
        """
        str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value):
        self.__error_id = value

    @property
    def errors(self):
        """
        list[:class:`APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value):
        self.__errors = value

    def to_dictionary(self):
        dictionary = super(ErrorResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'errorId', self.error_id)
        self._add_to_dictionary(dictionary, 'errors', self.errors)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for errors_element in dictionary['errors']:
                errors_value = APIError()
                self.errors.append(errors_value.from_dictionary(errors_element))
        return self
