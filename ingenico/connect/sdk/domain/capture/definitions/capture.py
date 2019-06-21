# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.capture.definitions.capture_output import CaptureOutput
from ingenico.connect.sdk.domain.capture.definitions.capture_status_output import CaptureStatusOutput
from ingenico.connect.sdk.domain.definitions.abstract_order_status import AbstractOrderStatus


class Capture(AbstractOrderStatus):

    __capture_output = None
    __status = None
    __status_output = None

    @property
    def capture_output(self):
        """
        | Object containing capture details
        
        Type: :class:`ingenico.connect.sdk.domain.capture.definitions.capture_output.CaptureOutput`
        """
        return self.__capture_output

    @capture_output.setter
    def capture_output(self, value):
        self.__capture_output = value

    @property
    def status(self):
        """
        | Current high-level status of the payment in a human-readable form. Possible values are :
        
        * CAPTURE_REQUESTED - The transaction is in the queue to be captured.
        * CAPTURED - The transaction has been captured and we have received online confirmation.
        * CANCELLED - You have cancelled the transaction.
        * REJECTED_CAPTURE - We or one of our downstream acquirers/providers have rejected the capture request.
        * REVERSED - The transaction has been reversed.
        
        
        | Please see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html> for a full overview of possible values.
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def status_output(self):
        """
        | This object has the numeric representation of the current capture status, timestamp of last status change and performable action on the current payment resource.
        | In case of failed payments and negative scenarios, detailed error information is listed.
        
        Type: :class:`ingenico.connect.sdk.domain.capture.definitions.capture_status_output.CaptureStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value):
        self.__status_output = value

    def to_dictionary(self):
        dictionary = super(Capture, self).to_dictionary()
        if self.capture_output is not None:
            dictionary['captureOutput'] = self.capture_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(Capture, self).from_dictionary(dictionary)
        if 'captureOutput' in dictionary:
            if not isinstance(dictionary['captureOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['captureOutput']))
            value = CaptureOutput()
            self.capture_output = value.from_dictionary(dictionary['captureOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = CaptureStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
