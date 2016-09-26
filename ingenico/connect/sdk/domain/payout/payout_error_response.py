#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.errors.definitions.api_error import APIError
from ingenico.connect.sdk.domain.payout.definitions.payout_result import PayoutResult


class PayoutErrorResponse(DataObject):
    """
    Class PayoutErrorResponse
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PayoutErrorResponse
    
    Attributes:
        error_id:       str
        errors:         list[:class:`APIError`]
        payout_result:  :class:`PayoutResult`
     """

    error_id = None
    errors = None
    payout_result = None

    def to_dictionary(self):
        dictionary = super(PayoutErrorResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'errorId', self.error_id)
        self._add_to_dictionary(dictionary, 'errors', self.errors)
        self._add_to_dictionary(dictionary, 'payoutResult', self.payout_result)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for errors_element in dictionary['errors']:
                errors_value = APIError()
                self.errors.append(errors_value.from_dictionary(errors_element))
        if 'payoutResult' in dictionary:
            if not isinstance(dictionary['payoutResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutResult']))
            value = PayoutResult()
            self.payout_result = value.from_dictionary(dictionary['payoutResult'])
        return self
