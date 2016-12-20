#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.result_do_risk_assessment import ResultDoRiskAssessment


class RiskAssessmentResponse(DataObject):
    """
    Class RiskAssessmentResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RiskAssessmentResponse
    """

    __results = None

    @property
    def results(self):
        """
        list[:class:`ResultDoRiskAssessment`]
        """
        return self.__results

    @results.setter
    def results(self, value):
        self.__results = value

    def to_dictionary(self):
        dictionary = super(RiskAssessmentResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'results', self.results)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RiskAssessmentResponse, self).from_dictionary(dictionary)
        if 'results' in dictionary:
            if not isinstance(dictionary['results'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['results']))
            self.results = []
            for results_element in dictionary['results']:
                results_value = ResultDoRiskAssessment()
                self.results.append(results_value.from_dictionary(results_element))
        return self
