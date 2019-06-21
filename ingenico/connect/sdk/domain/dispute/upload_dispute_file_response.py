# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class UploadDisputeFileResponse(DataObject):
    """
    | Response of a file upload request
    """

    __dispute_id = None
    __file_id = None

    @property
    def dispute_id(self):
        """
        | Dispute ID that is associated with the created dispute.
        
        Type: str
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value

    @property
    def file_id(self):
        """
        | The file ID that is associated with the uploaded file. This ID can be used for further communication regarding the file and retrieval of aforementioned property.
        
        Type: str
        """
        return self.__file_id

    @file_id.setter
    def file_id(self, value):
        self.__file_id = value

    def to_dictionary(self):
        dictionary = super(UploadDisputeFileResponse, self).to_dictionary()
        if self.dispute_id is not None:
            dictionary['disputeId'] = self.dispute_id
        if self.file_id is not None:
            dictionary['fileId'] = self.file_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(UploadDisputeFileResponse, self).from_dictionary(dictionary)
        if 'disputeId' in dictionary:
            self.dispute_id = dictionary['disputeId']
        if 'fileId' in dictionary:
            self.file_id = dictionary['fileId']
        return self
