# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.retail_decisions_cc_fraud_check_output import RetailDecisionsCCFraudCheckOutput
from ingenico.connect.sdk.domain.definitions.validation_bank_account_output import ValidationBankAccountOutput


class ResultDoRiskAssessment(DataObject):

    __category = None
    __result = None
    __retaildecisions_cc_fraud_check_output = None
    __validation_bank_account_output = None

    @property
    def category(self):
        """
        | The Risk Services category with the following possible values:
        
        * retaildecisionsCCFraudCheck - checks performed by Retail Decisions
        * globalcollectBlacklistCheckCC - Checked against the blacklist on the GlobalCollect platform
        * authorizationCheck - 0$ auth card account validation check
        * ddFraudCheck - Check performed for German market via InterCard
        * validationbankAccount - Bank account details are algorithmically checked if they could exist
        * globalcollectBlacklistCheckDD - Checked against the blacklist on the GlobalCollect platform
        
        Type: str
        """
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def result(self):
        """
        | Risk service result with the following possible results:
        
        * accepted - Based on the checks performed the transaction can be accepted
        * challenged - Based on the checks performed the transaction should be manually reviewed
        * denied - Based on the checks performed the transaction should be rejected
        * no-advice - No fraud check was requested/performed
        * error - The fraud check resulted in an error and the fraud check was thus not performed
        
        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    @property
    def retaildecisions_cc_fraud_check_output(self):
        """
        | Object containing the results of the fraud checks performed by Retail Decisions
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.retail_decisions_cc_fraud_check_output.RetailDecisionsCCFraudCheckOutput`
        """
        return self.__retaildecisions_cc_fraud_check_output

    @retaildecisions_cc_fraud_check_output.setter
    def retaildecisions_cc_fraud_check_output(self, value):
        self.__retaildecisions_cc_fraud_check_output = value

    @property
    def validation_bank_account_output(self):
        """
        | Object containing the results of the fraud checks performed on the bank account data
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.validation_bank_account_output.ValidationBankAccountOutput`
        """
        return self.__validation_bank_account_output

    @validation_bank_account_output.setter
    def validation_bank_account_output(self, value):
        self.__validation_bank_account_output = value

    def to_dictionary(self):
        dictionary = super(ResultDoRiskAssessment, self).to_dictionary()
        if self.category is not None:
            dictionary['category'] = self.category
        if self.result is not None:
            dictionary['result'] = self.result
        if self.retaildecisions_cc_fraud_check_output is not None:
            dictionary['retaildecisionsCCFraudCheckOutput'] = self.retaildecisions_cc_fraud_check_output.to_dictionary()
        if self.validation_bank_account_output is not None:
            dictionary['validationBankAccountOutput'] = self.validation_bank_account_output.to_dictionary()
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
