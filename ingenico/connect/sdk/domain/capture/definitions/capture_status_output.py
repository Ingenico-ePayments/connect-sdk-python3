# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair


class CaptureStatusOutput(DataObject):

    __is_retriable = None
    __provider_raw_output = None
    __status_code = None

    @property
    def is_retriable(self):
        """
        | Flag indicating whether a rejected payment may be retried by the merchant without incurring a fee 
        
        * true
        * false
        
        Type: bool
        """
        return self.__is_retriable

    @is_retriable.setter
    def is_retriable(self, value):
        self.__is_retriable = value

    @property
    def provider_raw_output(self):
        """
        | This is the raw response returned by the acquirer. This property contains unprocessed data directly returned by the acquirer. It's recommended for data analysis only due to its dynamic nature, which may undergo future changes.
        
        Type: list[:class:`ingenico.connect.sdk.domain.definitions.key_value_pair.KeyValuePair`]
        """
        return self.__provider_raw_output

    @provider_raw_output.setter
    def provider_raw_output(self, value):
        self.__provider_raw_output = value

    @property
    def status_code(self):
        """
        | Numeric status code of the legacy API. It is returned to ease the migration from the legacy APIs to Worldline Connect. You should not write new business logic based on this property as it will be deprecated in a future version of the API. The value can also be found in the GlobalCollect Payment Console, in the Ogone BackOffice and in report files.
        
        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    def to_dictionary(self):
        dictionary = super(CaptureStatusOutput, self).to_dictionary()
        if self.is_retriable is not None:
            dictionary['isRetriable'] = self.is_retriable
        if self.provider_raw_output is not None:
            dictionary['providerRawOutput'] = []
            for element in self.provider_raw_output:
                if element is not None:
                    dictionary['providerRawOutput'].append(element.to_dictionary())
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(CaptureStatusOutput, self).from_dictionary(dictionary)
        if 'isRetriable' in dictionary:
            self.is_retriable = dictionary['isRetriable']
        if 'providerRawOutput' in dictionary:
            if not isinstance(dictionary['providerRawOutput'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['providerRawOutput']))
            self.provider_raw_output = []
            for element in dictionary['providerRawOutput']:
                value = KeyValuePair()
                self.provider_raw_output.append(value.from_dictionary(element))
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
