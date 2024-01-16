# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject


class DeviceFingerprintDetails(DataObject):

    __payment_id = None
    __raw_device_fingerprint_output = None

    @property
    def payment_id(self):
        """
        | The ID of the payment that is linked to the Device Fingerprint data.
        
        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def raw_device_fingerprint_output(self):
        """
        | The detailed data that was collected during the Device Fingerprint collection. The structure will be different depending on the collection method and device fingerprint partner used. Please contact us if you want more information on the details that are returned in this string.
        
        Type: str
        """
        return self.__raw_device_fingerprint_output

    @raw_device_fingerprint_output.setter
    def raw_device_fingerprint_output(self, value):
        self.__raw_device_fingerprint_output = value

    def to_dictionary(self):
        dictionary = super(DeviceFingerprintDetails, self).to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.raw_device_fingerprint_output is not None:
            dictionary['rawDeviceFingerprintOutput'] = self.raw_device_fingerprint_output
        return dictionary

    def from_dictionary(self, dictionary):
        super(DeviceFingerprintDetails, self).from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'rawDeviceFingerprintOutput' in dictionary:
            self.raw_device_fingerprint_output = dictionary['rawDeviceFingerprintOutput']
        return self
