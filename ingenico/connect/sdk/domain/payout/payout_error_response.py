# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.errors.definitions.api_error import APIError
from ingenico.connect.sdk.domain.payout.definitions.payout_result import PayoutResult


class PayoutErrorResponse(DataObject):

    __error_id = None
    __errors = None
    __payout_result = None

    @property
    def error_id(self):
        """
        | Unique reference, for debugging purposes, of this error response
        
        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value):
        self.__error_id = value

    @property
    def errors(self):
        """
        | List of one or more errors
        
        Type: list[:class:`ingenico.connect.sdk.domain.errors.definitions.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value):
        self.__errors = value

    @property
    def payout_result(self):
        """
        | Object that contains details on the created payout in case one has been created
        
        Type: :class:`ingenico.connect.sdk.domain.payout.definitions.payout_result.PayoutResult`
        """
        return self.__payout_result

    @payout_result.setter
    def payout_result(self, value):
        self.__payout_result = value

    def to_dictionary(self):
        dictionary = super(PayoutErrorResponse, self).to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.payout_result is not None:
            dictionary['payoutResult'] = self.payout_result.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'payoutResult' in dictionary:
            if not isinstance(dictionary['payoutResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutResult']))
            value = PayoutResult()
            self.payout_result = value.from_dictionary(dictionary['payoutResult'])
        return self
