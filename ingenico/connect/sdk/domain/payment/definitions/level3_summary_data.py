# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class Level3SummaryData(DataObject):
    """
    Deprecated; Use ShoppingCart.amountBreakdown instead
    """

    __discount_amount = None
    __duty_amount = None
    __shipping_amount = None

    @property
    def discount_amount(self):
        """
        | Discount on the entire transaction, with the last 2 digits are implied decimal places
        
        Type: int
        
        Deprecated; Use ShoppingCart.amountBreakdown with type DISCOUNT instead
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value

    @property
    def duty_amount(self):
        """
        | Duty on the entire transaction, with the last 2 digits are implied decimal places
        
        Type: int
        
        Deprecated; Use ShoppingCart.amountBreakdown with type DUTY instead
        """
        return self.__duty_amount

    @duty_amount.setter
    def duty_amount(self, value):
        self.__duty_amount = value

    @property
    def shipping_amount(self):
        """
        | Shippingcost on the entire transaction, with the last 2 digits are implied decimal places
        
        Type: int
        
        Deprecated; Use ShoppingCart.amountBreakdown with type SHIPPING instead
        """
        return self.__shipping_amount

    @shipping_amount.setter
    def shipping_amount(self, value):
        self.__shipping_amount = value

    def to_dictionary(self):
        dictionary = super(Level3SummaryData, self).to_dictionary()
        if self.discount_amount is not None:
            dictionary['discountAmount'] = self.discount_amount
        if self.duty_amount is not None:
            dictionary['dutyAmount'] = self.duty_amount
        if self.shipping_amount is not None:
            dictionary['shippingAmount'] = self.shipping_amount
        return dictionary

    def from_dictionary(self, dictionary):
        super(Level3SummaryData, self).from_dictionary(dictionary)
        if 'discountAmount' in dictionary:
            self.discount_amount = dictionary['discountAmount']
        if 'dutyAmount' in dictionary:
            self.duty_amount = dictionary['dutyAmount']
        if 'shippingAmount' in dictionary:
            self.shipping_amount = dictionary['shippingAmount']
        return self
