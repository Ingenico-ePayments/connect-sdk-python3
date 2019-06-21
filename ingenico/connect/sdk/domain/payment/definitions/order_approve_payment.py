# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.additional_order_input_airline_data import AdditionalOrderInputAirlineData
from ingenico.connect.sdk.domain.payment.definitions.customer_approve_payment import CustomerApprovePayment
from ingenico.connect.sdk.domain.payment.definitions.order_references_approve_payment import OrderReferencesApprovePayment


class OrderApprovePayment(DataObject):

    __additional_input = None
    __customer = None
    __references = None

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
    def customer(self):
        """
        | Object containing data related to the customer
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.customer_approve_payment.CustomerApprovePayment`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def references(self):
        """
        | Object that holds all reference properties that are linked to this transaction
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order_references_approve_payment.OrderReferencesApprovePayment`
        """
        return self.__references

    @references.setter
    def references(self, value):
        self.__references = value

    def to_dictionary(self):
        dictionary = super(OrderApprovePayment, self).to_dictionary()
        if self.additional_input is not None:
            dictionary['additionalInput'] = self.additional_input.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderApprovePayment, self).from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInputAirlineData()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerApprovePayment()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = OrderReferencesApprovePayment()
            self.references = value.from_dictionary(dictionary['references'])
        return self
