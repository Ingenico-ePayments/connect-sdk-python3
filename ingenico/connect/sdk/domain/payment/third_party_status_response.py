# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ThirdPartyStatusResponse(DataObject):

    __third_party_status = None

    @property
    def third_party_status(self):
        """
        | The status returned by the third party.Possible values:
        
        * WAITING - The customer has not connected to the third party
        * INITIALIZED - Authentication in progress
        * AUTHORIZED - Payment in progress
        * COMPLETED - The customer has completed the payment at the third party
        
        Type: str
        """
        return self.__third_party_status

    @third_party_status.setter
    def third_party_status(self, value):
        self.__third_party_status = value

    def to_dictionary(self):
        dictionary = super(ThirdPartyStatusResponse, self).to_dictionary()
        if self.third_party_status is not None:
            dictionary['thirdPartyStatus'] = self.third_party_status
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThirdPartyStatusResponse, self).from_dictionary(dictionary)
        if 'thirdPartyStatus' in dictionary:
            self.third_party_status = dictionary['thirdPartyStatus']
        return self
