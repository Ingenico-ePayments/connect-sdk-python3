# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class SdkDataOutput(DataObject):

    __sdk_transaction_id = None

    @property
    def sdk_transaction_id(self):
        """
        | Universally unique transaction identifier assigned by the 3-D Secure SDK to identify this transaction.
        
        Type: str
        """
        return self.__sdk_transaction_id

    @sdk_transaction_id.setter
    def sdk_transaction_id(self, value):
        self.__sdk_transaction_id = value

    def to_dictionary(self):
        dictionary = super(SdkDataOutput, self).to_dictionary()
        if self.sdk_transaction_id is not None:
            dictionary['sdkTransactionId'] = self.sdk_transaction_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(SdkDataOutput, self).from_dictionary(dictionary)
        if 'sdkTransactionId' in dictionary:
            self.sdk_transaction_id = dictionary['sdkTransactionId']
        return self
