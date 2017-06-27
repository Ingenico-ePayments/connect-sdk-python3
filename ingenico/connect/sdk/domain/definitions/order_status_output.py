# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.errors.definitions.api_error import APIError


class OrderStatusOutput(DataObject):

    __errors = None
    __is_cancellable = None
    __status_category = None
    __status_code = None
    __status_code_change_date_time = None

    @property
    def errors(self):
        """
        | Custom object contains the set of errors
        
        Type: list[:class:`ingenico.connect.sdk.domain.errors.definitions.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value):
        self.__errors = value

    @property
    def is_cancellable(self):
        """
        | Flag indicating if the payment can be cancelled
        
        * true
        * false
        
        Type: bool
        """
        return self.__is_cancellable

    @is_cancellable.setter
    def is_cancellable(self, value):
        self.__is_cancellable = value

    @property
    def status_category(self):
        """
        | Highlevel status of the payment, payout or refund with the following possible values:
        
        * CREATED - The transaction has been created. This is the initial state once a new payment, payout or refund is created. This category groups the following statuses:
        
        * CREATED
        
        
        * PENDING_PAYMENT: The payment is waiting on consumer action. This category groups the following statuses:
        
        * PENDING_PAYMENT
        * REDIRECTED
        
        
        * ACCOUNT_VERIFIED: The account has been verified. This category groups the following statuses:
        
        * ACCOUNT_VERIFIED
        
        
        * PENDING_MERCHANT: The transaction is awaiting approval to proceed with the payment, payout or refund. This category groups the following statuses:
        
        * PENDING_APPROVAL
        * PENDING_FRAUD_APPROVAL
        
        
        * PENDING_CONNECT_OR_3RD_PARTY: The transaction is in the queue to be processed. This category groups the following statuses:
        
        * AUTHORIZATION_REQUESTED
        * CAPTURE_REQUESTED
        * PAYOUT_REQUESTED
        * REFUND_REQUESTED
        
        
        * COMPLETED: The transaction has completed. This category groups the following statuses:
        
        * CAPTURED
        * PAID
        * ACCOUNT_CREDITED
        
        
        * REVERSED: The transaction has been reversed. This category groups the following statuses:
        
        * CHARGEBACKED
        * REVERSED
        
        
        * REFUNDED: The transaction has been refunded. This category groups the following statuses:
        
        * REFUNDED
        
        
        * UNSUCCESSFUL: The transaction has been rejected or is in such a state that it will never become successful. This category groups the following statuses:
        
        * CANCELLED
        * REJECTED
        * REJECTED_CAPTURE
        * REJECTED_CREDIT
        
        
        
        
        | Please see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html> for a full overview of possible values.
        
        Type: str
        """
        return self.__status_category

    @status_category.setter
    def status_category(self, value):
        self.__status_category = value

    @property
    def status_code(self):
        """
        | Numeric status code that is returned by either Ingenico's Global Collect Payment Platform or Ingenico's Ogone Payment Platform. It is returned to ease the migration from the local APIs to Ingenico Connect. You should not write new business logic based on this field as it will be deprecated in a future version of the API. The value can also be found in the Global Collect Payment Console, in the Global Collect report files and the Ogone BackOffice and report files.
        
        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    @property
    def status_code_change_date_time(self):
        """
        | Date and time of payment
        | Format: YYYYMMDDHH24MISS
        
        Type: str
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
