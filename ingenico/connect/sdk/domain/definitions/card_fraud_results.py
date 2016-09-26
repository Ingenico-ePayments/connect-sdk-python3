#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.fraud_results import FraudResults
from ingenico.connect.sdk.domain.definitions.fraud_results_retail_decisions import FraudResultsRetailDecisions


class CardFraudResults(FraudResults):
    """
    Class CardFraudResults
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardFraudResults
    
    Attributes:
        avs_result:        str
        cvv_result:        str
        retail_decisions:  :class:`FraudResultsRetailDecisions`
     """

    avs_result = None
    cvv_result = None
    retail_decisions = None

    def to_dictionary(self):
        dictionary = super(CardFraudResults, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'avsResult', self.avs_result)
        self._add_to_dictionary(dictionary, 'cvvResult', self.cvv_result)
        self._add_to_dictionary(dictionary, 'retailDecisions', self.retail_decisions)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardFraudResults, self).from_dictionary(dictionary)
        if 'avsResult' in dictionary:
            self.avs_result = dictionary['avsResult']
        if 'cvvResult' in dictionary:
            self.cvv_result = dictionary['cvvResult']
        if 'retailDecisions' in dictionary:
            if not isinstance(dictionary['retailDecisions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['retailDecisions']))
            value = FraudResultsRetailDecisions()
            self.retail_decisions = value.from_dictionary(dictionary['retailDecisions'])
        return self
