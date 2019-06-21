# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class CustomerDeviceRiskAssessment(DataObject):
    """
    | Object containing information on the device and browser of the customer
    """

    __default_form_fill = None
    __device_fingerprint_transaction_id = None

    @property
    def default_form_fill(self):
        """
        | Degree of default form fill, with the following possible values:
        
        * automatically - All fields filled automatically
        * automatically-but-modified - All fields filled automatically, but some fields were modified manually
        * manually - All fields were entered manually
        
        Type: str
        """
        return self.__default_form_fill

    @default_form_fill.setter
    def default_form_fill(self, value):
        self.__default_form_fill = value

    @property
    def device_fingerprint_transaction_id(self):
        """
        | One must set the deviceFingerprintTransactionId received by the response of the endpoint /{merchant}/products/{paymentProductId}/deviceFingerprint
        
        Type: str
        """
        return self.__device_fingerprint_transaction_id

    @device_fingerprint_transaction_id.setter
    def device_fingerprint_transaction_id(self, value):
        self.__device_fingerprint_transaction_id = value

    def to_dictionary(self):
        dictionary = super(CustomerDeviceRiskAssessment, self).to_dictionary()
        if self.default_form_fill is not None:
            dictionary['defaultFormFill'] = self.default_form_fill
        if self.device_fingerprint_transaction_id is not None:
            dictionary['deviceFingerprintTransactionId'] = self.device_fingerprint_transaction_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerDeviceRiskAssessment, self).from_dictionary(dictionary)
        if 'defaultFormFill' in dictionary:
            self.default_form_fill = dictionary['defaultFormFill']
        if 'deviceFingerprintTransactionId' in dictionary:
            self.device_fingerprint_transaction_id = dictionary['deviceFingerprintTransactionId']
        return self
