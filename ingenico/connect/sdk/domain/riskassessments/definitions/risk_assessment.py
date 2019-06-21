# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.fraud_fields import FraudFields
from ingenico.connect.sdk.domain.riskassessments.definitions.merchant_risk_assessment import MerchantRiskAssessment
from ingenico.connect.sdk.domain.riskassessments.definitions.order_risk_assessment import OrderRiskAssessment


class RiskAssessment(DataObject):

    __fraud_fields = None
    __merchant = None
    __order = None
    __payment_product_id = None

    @property
    def fraud_fields(self):
        """
        | Object containing additional data that will be used to assess the risk of fraud
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.fraud_fields.FraudFields`
        """
        return self.__fraud_fields

    @fraud_fields.setter
    def fraud_fields(self, value):
        self.__fraud_fields = value

    @property
    def merchant(self):
        """
        Type: :class:`ingenico.connect.sdk.domain.riskassessments.definitions.merchant_risk_assessment.MerchantRiskAssessment`
        """
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value

    @property
    def order(self):
        """
        Type: :class:`ingenico.connect.sdk.domain.riskassessments.definitions.order_risk_assessment.OrderRiskAssessment`
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def payment_product_id(self):
        """
        | Payment product identifier
        | Please see payment products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(RiskAssessment, self).to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.merchant is not None:
            dictionary['merchant'] = self.merchant.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(RiskAssessment, self).from_dictionary(dictionary)
        if 'fraudFields' in dictionary:
            if not isinstance(dictionary['fraudFields'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudFields']))
            value = FraudFields()
            self.fraud_fields = value.from_dictionary(dictionary['fraudFields'])
        if 'merchant' in dictionary:
            if not isinstance(dictionary['merchant'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchant']))
            value = MerchantRiskAssessment()
            self.merchant = value.from_dictionary(dictionary['merchant'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = OrderRiskAssessment()
            self.order = value.from_dictionary(dictionary['order'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
