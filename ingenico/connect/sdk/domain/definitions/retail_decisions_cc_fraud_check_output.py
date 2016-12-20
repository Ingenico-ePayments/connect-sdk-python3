#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RetailDecisionsCCFraudCheckOutput(DataObject):
    """
    Class RetailDecisionsCCFraudCheckOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RetailDecisionsCCFraudCheckOutput
    """

    __fraud_code = None
    __fraud_neural = None
    __fraud_rcf = None

    @property
    def fraud_code(self):
        """
        str
        """
        return self.__fraud_code

    @fraud_code.setter
    def fraud_code(self, value):
        self.__fraud_code = value

    @property
    def fraud_neural(self):
        """
        str
        """
        return self.__fraud_neural

    @fraud_neural.setter
    def fraud_neural(self, value):
        self.__fraud_neural = value

    @property
    def fraud_rcf(self):
        """
        str
        """
        return self.__fraud_rcf

    @fraud_rcf.setter
    def fraud_rcf(self, value):
        self.__fraud_rcf = value

    def to_dictionary(self):
        dictionary = super(RetailDecisionsCCFraudCheckOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'fraudCode', self.fraud_code)
        self._add_to_dictionary(dictionary, 'fraudNeural', self.fraud_neural)
        self._add_to_dictionary(dictionary, 'fraudRCF', self.fraud_rcf)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RetailDecisionsCCFraudCheckOutput, self).from_dictionary(dictionary)
        if 'fraudCode' in dictionary:
            self.fraud_code = dictionary['fraudCode']
        if 'fraudNeural' in dictionary:
            self.fraud_neural = dictionary['fraudNeural']
        if 'fraudRCF' in dictionary:
            self.fraud_rcf = dictionary['fraudRCF']
        return self
