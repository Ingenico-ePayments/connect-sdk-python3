# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class DeviceFingerprintRequest(DataObject):

    __collector_callback = None

    @property
    def collector_callback(self):
        """
        | You can supply a JavaScript function call that will be called after the device fingerprint data collecting using the provided JavaScript snippet is finished. This will then be added to the snippet that is returned in the property html.
        
        Type: str
        """
        return self.__collector_callback

    @collector_callback.setter
    def collector_callback(self, value):
        self.__collector_callback = value

    def to_dictionary(self):
        dictionary = super(DeviceFingerprintRequest, self).to_dictionary()
        if self.collector_callback is not None:
            dictionary['collectorCallback'] = self.collector_callback
        return dictionary

    def from_dictionary(self, dictionary):
        super(DeviceFingerprintRequest, self).from_dictionary(dictionary)
        if 'collectorCallback' in dictionary:
            self.collector_callback = dictionary['collectorCallback']
        return self
