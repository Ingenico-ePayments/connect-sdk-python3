#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.riskassessments.definitions.personal_name_risk_assessment import PersonalNameRiskAssessment


class PersonalInformationRiskAssessment(DataObject):
    """
    Class PersonalInformationRiskAssessment
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PersonalInformationRiskAssessment
    """

    __name = None

    @property
    def name(self):
        """
        :class:`PersonalNameRiskAssessment`
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(PersonalInformationRiskAssessment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'name', self.name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalInformationRiskAssessment, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalNameRiskAssessment()
            self.name = value.from_dictionary(dictionary['name'])
        return self
