# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.sdk_data_output import SdkDataOutput
from ingenico.connect.sdk.domain.payment.definitions.three_d_secure_data import ThreeDSecureData


class ThreeDSecureResults(DataObject):
    """
    | Object containing the 3-D Secure specific results
    """

    __cavv = None
    __directory_server_transaction_id = None
    __eci = None
    __sdk_data = None
    __three_d_secure_data = None
    __three_d_secure_version = None
    __three_d_server_transaction_id = None
    __xid = None

    @property
    def cavv(self):
        """
        | CAVV or AVV result indicating authentication validation value
        
        Type: str
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value

    @property
    def directory_server_transaction_id(self):
        """
        | The 3-D Secure Directory Server transaction ID that is used for the 3D Authentication
        
        Type: str
        """
        return self.__directory_server_transaction_id

    @directory_server_transaction_id.setter
    def directory_server_transaction_id(self, value):
        self.__directory_server_transaction_id = value

    @property
    def eci(self):
        """
        | Indicates Authentication validation results returned after AuthenticationValidation
        
        Type: str
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def sdk_data(self):
        """
        | Object containing 3-D Secure in-app SDK data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.sdk_data_output.SdkDataOutput`
        """
        return self.__sdk_data

    @sdk_data.setter
    def sdk_data(self, value):
        self.__sdk_data = value

    @property
    def three_d_secure_data(self):
        """
        | Object containing data regarding the 3-D Secure authentication
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.three_d_secure_data.ThreeDSecureData`
        """
        return self.__three_d_secure_data

    @three_d_secure_data.setter
    def three_d_secure_data(self, value):
        self.__three_d_secure_data = value

    @property
    def three_d_secure_version(self):
        """
        | The 3-D Secure version used for the authentication.
        
        | This property is used in the communication with the acquirer
        
        Type: str
        """
        return self.__three_d_secure_version

    @three_d_secure_version.setter
    def three_d_secure_version(self, value):
        self.__three_d_secure_version = value

    @property
    def three_d_server_transaction_id(self):
        """
        | The 3-D Secure Server transaction ID that is used for the 3-D Secure version 2 Authentication.
        
        Type: str
        """
        return self.__three_d_server_transaction_id

    @three_d_server_transaction_id.setter
    def three_d_server_transaction_id(self, value):
        self.__three_d_server_transaction_id = value

    @property
    def xid(self):
        """
        | Transaction ID for the Authentication
        
        Type: str
        """
        return self.__xid

    @xid.setter
    def xid(self, value):
        self.__xid = value

    def to_dictionary(self):
        dictionary = super(ThreeDSecureResults, self).to_dictionary()
        if self.cavv is not None:
            dictionary['cavv'] = self.cavv
        if self.directory_server_transaction_id is not None:
            dictionary['directoryServerTransactionId'] = self.directory_server_transaction_id
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.sdk_data is not None:
            dictionary['sdkData'] = self.sdk_data.to_dictionary()
        if self.three_d_secure_data is not None:
            dictionary['threeDSecureData'] = self.three_d_secure_data.to_dictionary()
        if self.three_d_secure_version is not None:
            dictionary['threeDSecureVersion'] = self.three_d_secure_version
        if self.three_d_server_transaction_id is not None:
            dictionary['threeDServerTransactionId'] = self.three_d_server_transaction_id
        if self.xid is not None:
            dictionary['xid'] = self.xid
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSecureResults, self).from_dictionary(dictionary)
        if 'cavv' in dictionary:
            self.cavv = dictionary['cavv']
        if 'directoryServerTransactionId' in dictionary:
            self.directory_server_transaction_id = dictionary['directoryServerTransactionId']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'sdkData' in dictionary:
            if not isinstance(dictionary['sdkData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sdkData']))
            value = SdkDataOutput()
            self.sdk_data = value.from_dictionary(dictionary['sdkData'])
        if 'threeDSecureData' in dictionary:
            if not isinstance(dictionary['threeDSecureData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureData']))
            value = ThreeDSecureData()
            self.three_d_secure_data = value.from_dictionary(dictionary['threeDSecureData'])
        if 'threeDSecureVersion' in dictionary:
            self.three_d_secure_version = dictionary['threeDSecureVersion']
        if 'threeDServerTransactionId' in dictionary:
            self.three_d_server_transaction_id = dictionary['threeDServerTransactionId']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self
