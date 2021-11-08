# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MicrosoftFraudResults(DataObject):

    __fraud_score = None

    @property
    def fraud_score(self):
        """
        | Result of the Microsoft Fraud Protection check. This contains the normalized fraud score from a scale of 0 to 100. A higher score indicates an increased risk of fraud.
        
        Type: int
        """
        return self.__fraud_score

    @fraud_score.setter
    def fraud_score(self, value):
        self.__fraud_score = value

    def to_dictionary(self):
        dictionary = super(MicrosoftFraudResults, self).to_dictionary()
        if self.fraud_score is not None:
            dictionary['fraudScore'] = self.fraud_score
        return dictionary

    def from_dictionary(self, dictionary):
        super(MicrosoftFraudResults, self).from_dictionary(dictionary)
        if 'fraudScore' in dictionary:
            self.fraud_score = dictionary['fraudScore']
        return self
