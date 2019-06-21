# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.dispute.definitions.dispute_output import DisputeOutput
from ingenico.connect.sdk.domain.dispute.definitions.dispute_status_output import DisputeStatusOutput


class Dispute(DataObject):

    __dispute_output = None
    __id = None
    __payment_id = None
    __status = None
    __status_output = None

    @property
    def dispute_output(self):
        """
        | This property contains the creationDetails and default information regarding a dispute.
        
        Type: :class:`ingenico.connect.sdk.domain.dispute.definitions.dispute_output.DisputeOutput`
        """
        return self.__dispute_output

    @dispute_output.setter
    def dispute_output(self, value):
        self.__dispute_output = value

    @property
    def id(self):
        """
        | Dispute ID for a given merchant.
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def payment_id(self):
        """
        | The ID of the payment that is being disputed.
        
        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def status(self):
        """
        | Current dispute status.
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def status_output(self):
        """
        | This property contains the output for a dispute regarding the status of the dispute.
        
        Type: :class:`ingenico.connect.sdk.domain.dispute.definitions.dispute_status_output.DisputeStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value):
        self.__status_output = value

    def to_dictionary(self):
        dictionary = super(Dispute, self).to_dictionary()
        if self.dispute_output is not None:
            dictionary['disputeOutput'] = self.dispute_output.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(Dispute, self).from_dictionary(dictionary)
        if 'disputeOutput' in dictionary:
            if not isinstance(dictionary['disputeOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['disputeOutput']))
            value = DisputeOutput()
            self.dispute_output = value.from_dictionary(dictionary['disputeOutput'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = DisputeStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
