# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class FraudResults(DataObject):

    __fraud_service_result = None

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

    def to_dictionary(self):
        dictionary = super(FraudResults, self).to_dictionary()
        if self.fraud_service_result is not None:
            dictionary['fraudServiceResult'] = self.fraud_service_result
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudResults, self).from_dictionary(dictionary)
        if 'fraudServiceResult' in dictionary:
            self.fraud_service_result = dictionary['fraudServiceResult']
        return self
