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
    """

    __avs_result = None
    __cvv_result = None
    __retail_decisions = None

    @property
    def avs_result(self):
        """
        str
        """
        return self.__avs_result

    @avs_result.setter
    def avs_result(self, value):
        self.__avs_result = value

    @property
    def cvv_result(self):
        """
        str
        """
        return self.__cvv_result

    @cvv_result.setter
    def cvv_result(self, value):
        self.__cvv_result = value

    @property
    def retail_decisions(self):
        """
        :class:`FraudResultsRetailDecisions`
        """
        return self.__retail_decisions

    @retail_decisions.setter
    def retail_decisions(self, value):
        self.__retail_decisions = value

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
