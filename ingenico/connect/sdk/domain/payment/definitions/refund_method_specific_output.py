# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RefundMethodSpecificOutput(DataObject):

    __total_amount_paid = None
    __total_amount_refunded = None

    @property
    def total_amount_paid(self):
        """
        | Total paid amount (in cents and always with 2 decimals)
        
        Type: int
        """
        return self.__total_amount_paid

    @total_amount_paid.setter
    def total_amount_paid(self, value):
        self.__total_amount_paid = value

    @property
    def total_amount_refunded(self):
        """
        Type: int
        """
        return self.__total_amount_refunded

    @total_amount_refunded.setter
    def total_amount_refunded(self, value):
        self.__total_amount_refunded = value

    def to_dictionary(self):
        dictionary = super(RefundMethodSpecificOutput, self).to_dictionary()
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
