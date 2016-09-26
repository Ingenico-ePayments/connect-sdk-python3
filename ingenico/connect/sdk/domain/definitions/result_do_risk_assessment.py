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
    
    Attributes:
        category:                               str
        result:                                 str
        retaildecisions_cc_fraud_check_output:  :class:`RetailDecisionsCCFraudCheckOutput`
        validation_bank_account_output:         :class:`ValidationBankAccountOutput`
     """

    category = None
    result = None
    retaildecisions_cc_fraud_check_output = None
    validation_bank_account_output = None

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
