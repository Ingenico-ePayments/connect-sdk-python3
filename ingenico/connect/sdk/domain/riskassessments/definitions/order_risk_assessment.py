# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.additional_order_input_airline_data import AdditionalOrderInputAirlineData
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.riskassessments.definitions.customer_risk_assessment import CustomerRiskAssessment
from ingenico.connect.sdk.domain.riskassessments.definitions.shipping_risk_assessment import ShippingRiskAssessment


class OrderRiskAssessment(DataObject):

    __additional_input = None
    __amount_of_money = None
    __customer = None
    __shipping = None

    @property
    def additional_input(self):
        """
        | Object containing additional input on the order
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.additional_order_input_airline_data.AdditionalOrderInputAirlineData`
        """
        return self.__additional_input

    @additional_input.setter
    def additional_input(self, value):
        self.__additional_input = value

    @property
    def amount_of_money(self):
        """
        | Object containing amount and ISO currency code attributes
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def customer(self):
        """
        | Object containing the details of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.riskassessments.definitions.customer_risk_assessment.CustomerRiskAssessment`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def shipping(self):
        """
        | Object containing information regarding shipping / delivery
        
        Type: :class:`ingenico.connect.sdk.domain.riskassessments.definitions.shipping_risk_assessment.ShippingRiskAssessment`
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value):
        self.__shipping = value

    def to_dictionary(self):
        dictionary = super(OrderRiskAssessment, self).to_dictionary()
        if self.additional_input is not None:
            dictionary['additionalInput'] = self.additional_input.to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.shipping is not None:
            dictionary['shipping'] = self.shipping.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderRiskAssessment, self).from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInputAirlineData()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerRiskAssessment()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'shipping' in dictionary:
            if not isinstance(dictionary['shipping'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shipping']))
            value = ShippingRiskAssessment()
            self.shipping = value.from_dictionary(dictionary['shipping'])
        return self
