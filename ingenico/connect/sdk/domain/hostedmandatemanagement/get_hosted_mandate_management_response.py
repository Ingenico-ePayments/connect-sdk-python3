# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.mandates.definitions.mandate_response import MandateResponse


class GetHostedMandateManagementResponse(DataObject):

    __mandate = None
    __status = None

    @property
    def mandate(self):
        """
        | When a mandate has been created during the hosted mandate management session this object will return the details.
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.mandate_response.MandateResponse`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    @property
    def status(self):
        """
        | This is the status of the hosted mandate management. Possible values are:
        
        * IN_PROGRESS - The session has been created, but no mandate has been created yet.
        * MANDATE_CREATED - A mandate has been created, the customer might still need to sign the mandate.
        * FAILED - There was an error while creating the mandate, the session can not continue.
        * CANCELLED_BY_CONSUMER - The session was cancelled before a mandate was created
        
        | .
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def to_dictionary(self):
        dictionary = super(GetHostedMandateManagementResponse, self).to_dictionary()
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetHostedMandateManagementResponse, self).from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateResponse()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
