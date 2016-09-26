#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class FraudResultsRetailDecisions(DataObject):
    """
    Class FraudResultsRetailDecisions
    See also https://developer.globalcollect.com/documentation/api/server/#schema_FraudResultsRetailDecisions
    
    Attributes:
        fraud_code:    str
        fraud_neural:  str
        fraud_rcf:     str
     """

    fraud_code = None
    fraud_neural = None
    fraud_rcf = None

    def to_dictionary(self):
        dictionary = super(FraudResultsRetailDecisions, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'fraudCode', self.fraud_code)
        self._add_to_dictionary(dictionary, 'fraudNeural', self.fraud_neural)
        self._add_to_dictionary(dictionary, 'fraudRCF', self.fraud_rcf)
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
