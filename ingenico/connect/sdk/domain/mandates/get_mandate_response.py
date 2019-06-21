# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.mandates.definitions.mandate_response import MandateResponse


class GetMandateResponse(DataObject):

    __mandate = None

    @property
    def mandate(self):
        """
        | Object containing information on a mandate.
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.mandate_response.MandateResponse`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    def to_dictionary(self):
        dictionary = super(GetMandateResponse, self).to_dictionary()
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetMandateResponse, self).from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateResponse()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
