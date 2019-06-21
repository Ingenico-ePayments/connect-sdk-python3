# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MobileThreeDSecureChallengeParameters(DataObject):

    __acs_reference_number = None
    __acs_signed_content = None
    __acs_transaction_id = None
    __three_d_server_transaction_id = None

    @property
    def acs_reference_number(self):
        """
        | The unique identifier assigned by the EMVCo Secretariat upon testing and approval.
        
        Type: str
        """
        return self.__acs_reference_number

    @acs_reference_number.setter
    def acs_reference_number(self, value):
        self.__acs_reference_number = value

    @property
    def acs_signed_content(self):
        """
        | Contains the JWS object created by the ACS for the challenge (ARes).
        
        Type: str
        """
        return self.__acs_signed_content

    @acs_signed_content.setter
    def acs_signed_content(self, value):
        self.__acs_signed_content = value

    @property
    def acs_transaction_id(self):
        """
        | The ACS Transaction ID for a prior 3-D Secure authenticated transaction (for example, the first recurring transaction that was authenticated with the customer).
        
        Type: str
        """
        return self.__acs_transaction_id

    @acs_transaction_id.setter
    def acs_transaction_id(self, value):
        self.__acs_transaction_id = value

    @property
    def three_d_server_transaction_id(self):
        """
        | The 3-D Secure version 2 transaction ID that is used for the 3D Authentication
        
        Type: str
        """
        return self.__three_d_server_transaction_id

    @three_d_server_transaction_id.setter
    def three_d_server_transaction_id(self, value):
        self.__three_d_server_transaction_id = value

    def to_dictionary(self):
        dictionary = super(MobileThreeDSecureChallengeParameters, self).to_dictionary()
        if self.acs_reference_number is not None:
            dictionary['acsReferenceNumber'] = self.acs_reference_number
        if self.acs_signed_content is not None:
            dictionary['acsSignedContent'] = self.acs_signed_content
        if self.acs_transaction_id is not None:
            dictionary['acsTransactionId'] = self.acs_transaction_id
        if self.three_d_server_transaction_id is not None:
            dictionary['threeDServerTransactionId'] = self.three_d_server_transaction_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobileThreeDSecureChallengeParameters, self).from_dictionary(dictionary)
        if 'acsReferenceNumber' in dictionary:
            self.acs_reference_number = dictionary['acsReferenceNumber']
        if 'acsSignedContent' in dictionary:
            self.acs_signed_content = dictionary['acsSignedContent']
        if 'acsTransactionId' in dictionary:
            self.acs_transaction_id = dictionary['acsTransactionId']
        if 'threeDServerTransactionId' in dictionary:
            self.three_d_server_transaction_id = dictionary['threeDServerTransactionId']
        return self
