#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.errors.definitions.api_error import APIError
from ingenico.connect.sdk.domain.refund.definitions.refund_result import RefundResult


class RefundErrorResponse(DataObject):
    """
    Class RefundErrorResponse
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundErrorResponse
    
    Attributes:
        error_id:       str
        errors:         list[:class:`APIError`]
        refund_result:  :class:`RefundResult`
     """

    error_id = None
    errors = None
    refund_result = None

    def to_dictionary(self):
        dictionary = super(RefundErrorResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'errorId', self.error_id)
        self._add_to_dictionary(dictionary, 'errors', self.errors)
        self._add_to_dictionary(dictionary, 'refundResult', self.refund_result)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for errors_element in dictionary['errors']:
                errors_value = APIError()
                self.errors.append(errors_value.from_dictionary(errors_element))
        if 'refundResult' in dictionary:
            if not isinstance(dictionary['refundResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundResult']))
            value = RefundResult()
            self.refund_result = value.from_dictionary(dictionary['refundResult'])
        return self
