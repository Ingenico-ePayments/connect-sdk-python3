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
    
    Attributes:
        errors:                        list[:class:`APIError`]
        is_cancellable:                bool
        status_category:               str
        status_code:                   int
        status_code_change_date_time:  str
     """

    errors = None
    is_cancellable = None
    status_category = None
    status_code = None
    status_code_change_date_time = None

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
