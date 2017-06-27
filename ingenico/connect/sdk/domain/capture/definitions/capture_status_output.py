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
        | Numeric status code that is returned by either Ingenico's Global Collect Payment Platform or Ingenico's Ogone Payment Platform. It is returned to ease the migration from the local APIs to Ingenico Connect. You should not write new business logic based on this field as it will be deprecated in a future version of the API. The value can also be found in the Global Collect Payment Console, in the Global Collect report files and the Ogone BackOffice and report files.
        
        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    def to_dictionary(self):
        dictionary = super(CaptureStatusOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'statusCode', self.status_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CaptureStatusOutput, self).from_dictionary(dictionary)
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
