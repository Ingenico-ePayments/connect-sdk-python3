# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.capture.definitions.capture import Capture


class CapturesResponse(DataObject):

    __captures = None

    @property
    def captures(self):
        """
        | The list of all captures performed on the requested payment.
        
        Type: list[:class:`ingenico.connect.sdk.domain.capture.definitions.capture.Capture`]
        """
        return self.__captures

    @captures.setter
    def captures(self, value):
        self.__captures = value

    def to_dictionary(self):
        dictionary = super(CapturesResponse, self).to_dictionary()
        if self.captures is not None:
            dictionary['captures'] = []
            for element in self.captures:
                if element is not None:
                    dictionary['captures'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(CapturesResponse, self).from_dictionary(dictionary)
        if 'captures' in dictionary:
            if not isinstance(dictionary['captures'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['captures']))
            self.captures = []
            for element in dictionary['captures']:
                value = Capture()
                self.captures.append(value.from_dictionary(element))
        return self
