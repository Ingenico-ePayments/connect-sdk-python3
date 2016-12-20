#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.retail_decisions_cc_fraud_check_output import RetailDecisionsCCFraudCheckOutput
from ingenico.connect.sdk.domain.definitions.validation_bank_account_output import ValidationBankAccountOutput


class ResultDoRiskAssessment(DataObject):
    """
    Class ResultDoRiskAssessment
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ResultDoRiskAssessment
    """

    __category = None
    __result = None
    __retaildecisions_cc_fraud_check_output = None
    __validation_bank_account_output = None

    @property
    def category(self):
        """
        str
        """
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def result(self):
        """
        str
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    @property
    def retaildecisions_cc_fraud_check_output(self):
        """
        :class:`RetailDecisionsCCFraudCheckOutput`
        """
        return self.__retaildecisions_cc_fraud_check_output

    @retaildecisions_cc_fraud_check_output.setter
    def retaildecisions_cc_fraud_check_output(self, value):
        self.__retaildecisions_cc_fraud_check_output = value

    @property
    def validation_bank_account_output(self):
        """
        :class:`ValidationBankAccountOutput`
        """
        return self.__validation_bank_account_output

    @validation_bank_account_output.setter
    def validation_bank_account_output(self, value):
        self.__validation_bank_account_output = value

    def to_dictionary(self):
        dictionary = super(ResultDoRiskAssessment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'category', self.category)
        self._add_to_dictionary(dictionary, 'result', self.result)
        self._add_to_dictionary(dictionary, 'retaildecisionsCCFraudCheckOutput', self.retaildecisions_cc_fraud_check_output)
        self._add_to_dictionary(dictionary, 'validationBankAccountOutput', self.validation_bank_account_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ResultDoRiskAssessment, self).from_dictionary(dictionary)
        if 'category' in dictionary:
            self.category = dictionary['category']
        if 'result' in dictionary:
            self.result = dictionary['result']
        if 'retaildecisionsCCFraudCheckOutput' in dictionary:
            if not isinstance(dictionary['retaildecisionsCCFraudCheckOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['retaildecisionsCCFraudCheckOutput']))
            value = RetailDecisionsCCFraudCheckOutput()
            self.retaildecisions_cc_fraud_check_output = value.from_dictionary(dictionary['retaildecisionsCCFraudCheckOutput'])
        if 'validationBankAccountOutput' in dictionary:
            if not isinstance(dictionary['validationBankAccountOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['validationBankAccountOutput']))
            value = ValidationBankAccountOutput()
            self.validation_bank_account_output = value.from_dictionary(dictionary['validationBankAccountOutput'])
        return self
