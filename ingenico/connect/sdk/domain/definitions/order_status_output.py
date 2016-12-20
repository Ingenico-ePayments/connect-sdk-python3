#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.errors.definitions.api_error import APIError


class OrderStatusOutput(DataObject):
    """
    Class OrderStatusOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_OrderStatusOutput
    """

    __errors = None
    __is_cancellable = None
    __status_category = None
    __status_code = None
    __status_code_change_date_time = None

    @property
    def errors(self):
        """
        list[:class:`APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value):
        self.__errors = value

    @property
    def is_cancellable(self):
        """
        bool
        """
        return self.__is_cancellable

    @is_cancellable.setter
    def is_cancellable(self, value):
        self.__is_cancellable = value

    @property
    def status_category(self):
        """
        str
        """
        return self.__status_category

    @status_category.setter
    def status_category(self, value):
        self.__status_category = value

    @property
    def status_code(self):
        """
        int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    @property
    def status_code_change_date_time(self):
        """
        str
        """
        return self.__status_code_change_date_time

    @status_code_change_date_time.setter
    def status_code_change_date_time(self, value):
        self.__status_code_change_date_time = value

    def to_dictionary(self):
        dictionary = super(OrderStatusOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'errors', self.errors)
        self._add_to_dictionary(dictionary, 'isCancellable', self.is_cancellable)
        self._add_to_dictionary(dictionary, 'statusCategory', self.status_category)
        self._add_to_dictionary(dictionary, 'statusCode', self.status_code)
        self._add_to_dictionary(dictionary, 'statusCodeChangeDateTime', self.status_code_change_date_time)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderStatusOutput, self).from_dictionary(dictionary)
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for errors_element in dictionary['errors']:
                errors_value = APIError()
                self.errors.append(errors_value.from_dictionary(errors_element))
        if 'isCancellable' in dictionary:
            self.is_cancellable = dictionary['isCancellable']
        if 'statusCategory' in dictionary:
            self.status_category = dictionary['statusCategory']
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        if 'statusCodeChangeDateTime' in dictionary:
            self.status_code_change_date_time = dictionary['statusCodeChangeDateTime']
        return self
