# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.refund.definitions.bank_refund_method_specific_input import BankRefundMethodSpecificInput
from ingenico.connect.sdk.domain.refund.definitions.refund_customer import RefundCustomer
from ingenico.connect.sdk.domain.refund.definitions.refund_references import RefundReferences


class RefundRequest(DataObject):

    __amount_of_money = None
    __bank_refund_method_specific_input = None
    __customer = None
    __refund_date = None
    __refund_references = None

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
    def bank_refund_method_specific_input(self):
        """
        | Object containing the specific input details for a bank refund
        
        Type: :class:`ingenico.connect.sdk.domain.refund.definitions.bank_refund_method_specific_input.BankRefundMethodSpecificInput`
        """
        return self.__bank_refund_method_specific_input

    @bank_refund_method_specific_input.setter
    def bank_refund_method_specific_input(self, value):
        self.__bank_refund_method_specific_input = value

    @property
    def customer(self):
        """
        | Object containing the details of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.refund.definitions.refund_customer.RefundCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def refund_date(self):
        """
        | Refund date
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__refund_date

    @refund_date.setter
    def refund_date(self, value):
        self.__refund_date = value

    @property
    def refund_references(self):
        """
        | Object that holds all reference properties that are linked to this refund
        
        Type: :class:`ingenico.connect.sdk.domain.refund.definitions.refund_references.RefundReferences`
        """
        return self.__refund_references

    @refund_references.setter
    def refund_references(self, value):
        self.__refund_references = value

    def to_dictionary(self):
        dictionary = super(RefundRequest, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.bank_refund_method_specific_input is not None:
            dictionary['bankRefundMethodSpecificInput'] = self.bank_refund_method_specific_input.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.refund_date is not None:
            dictionary['refundDate'] = self.refund_date
        if self.refund_references is not None:
            dictionary['refundReferences'] = self.refund_references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundRequest, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'bankRefundMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['bankRefundMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankRefundMethodSpecificInput']))
            value = BankRefundMethodSpecificInput()
            self.bank_refund_method_specific_input = value.from_dictionary(dictionary['bankRefundMethodSpecificInput'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = RefundCustomer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'refundDate' in dictionary:
            self.refund_date = dictionary['refundDate']
        if 'refundReferences' in dictionary:
            if not isinstance(dictionary['refundReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundReferences']))
            value = RefundReferences()
            self.refund_references = value.from_dictionary(dictionary['refundReferences'])
        return self
