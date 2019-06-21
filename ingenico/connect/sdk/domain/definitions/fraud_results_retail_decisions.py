# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class FraudResultsRetailDecisions(DataObject):

    __fraud_code = None
    __fraud_neural = None
    __fraud_rcf = None

    @property
    def fraud_code(self):
        """
        | Result of the fraud service.
        | Provides additional information about the fraud result
        
        Type: str
        """
        return self.__fraud_code

    @fraud_code.setter
    def fraud_code(self, value):
        self.__fraud_code = value

    @property
    def fraud_neural(self):
        """
        | Returns the raw score of the neural
        
        Type: str
        """
        return self.__fraud_neural

    @fraud_neural.setter
    def fraud_neural(self, value):
        self.__fraud_neural = value

    @property
    def fraud_rcf(self):
        """
        | Result of the fraud service
        | Represent sets of fraud rules returned during the evaluation of the transaction
        
        Type: str
        """
        return self.__fraud_rcf

    @fraud_rcf.setter
    def fraud_rcf(self, value):
        self.__fraud_rcf = value

    def to_dictionary(self):
        dictionary = super(FraudResultsRetailDecisions, self).to_dictionary()
        if self.fraud_code is not None:
            dictionary['fraudCode'] = self.fraud_code
        if self.fraud_neural is not None:
            dictionary['fraudNeural'] = self.fraud_neural
        if self.fraud_rcf is not None:
            dictionary['fraudRCF'] = self.fraud_rcf
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudResultsRetailDecisions, self).from_dictionary(dictionary)
        if 'fraudCode' in dictionary:
            self.fraud_code = dictionary['fraudCode']
        if 'fraudNeural' in dictionary:
            self.fraud_neural = dictionary['fraudNeural']
        if 'fraudRCF' in dictionary:
            self.fraud_rcf = dictionary['fraudRCF']
        return self
