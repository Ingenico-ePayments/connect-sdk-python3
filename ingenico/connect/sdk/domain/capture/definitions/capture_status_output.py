# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class CaptureStatusOutput(DataObject):

    __status_code = None

    @property
    def status_code(self):
        """
        | Numeric status code of the legacy API. It is returned to ease the migration from the legacy APIs to Ingenico Connect. You should not write new business logic based on this property as it will be deprecated in a future version of the API. The value can also be found in the GlobalCollect Payment Console, in the Ogone BackOffice and in report files.
        
        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    def to_dictionary(self):
        dictionary = super(CaptureStatusOutput, self).to_dictionary()
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(CaptureStatusOutput, self).from_dictionary(dictionary)
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
