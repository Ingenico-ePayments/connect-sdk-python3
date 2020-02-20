# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.in_auth import InAuth


class FraudResults(DataObject):

    __fraud_service_result = None
    __in_auth = None

    @property
    def fraud_service_result(self):
        """
        | Results from the fraud prevention check. Possible values are:
        
        * accepted - Based on the checks performed the transaction can be accepted
        * challenged - Based on the checks performed the transaction should be manually reviewed
        * denied - Based on the checks performed the transaction should be rejected
        * no-advice - No fraud check was requested/performed
        * error - The fraud check resulted in an error and the fraud check was thus not performed
        
        Type: str
        """
        return self.__fraud_service_result

    @fraud_service_result.setter
    def fraud_service_result(self, value):
        self.__fraud_service_result = value

    @property
    def in_auth(self):
        """
        | Object containing device fingerprinting details from InAuth
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.in_auth.InAuth`
        """
        return self.__in_auth

    @in_auth.setter
    def in_auth(self, value):
        self.__in_auth = value

    def to_dictionary(self):
        dictionary = super(FraudResults, self).to_dictionary()
        if self.fraud_service_result is not None:
            dictionary['fraudServiceResult'] = self.fraud_service_result
        if self.in_auth is not None:
            dictionary['inAuth'] = self.in_auth.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudResults, self).from_dictionary(dictionary)
        if 'fraudServiceResult' in dictionary:
            self.fraud_service_result = dictionary['fraudServiceResult']
        if 'inAuth' in dictionary:
            if not isinstance(dictionary['inAuth'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['inAuth']))
            value = InAuth()
            self.in_auth = value.from_dictionary(dictionary['inAuth'])
        return self
