# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RefundMethodSpecificOutput(DataObject):

    __refund_product_id = None
    __total_amount_paid = None
    __total_amount_refunded = None

    @property
    def refund_product_id(self):
        """
        | Refund product identifier
        | Please see refund products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/refundproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__refund_product_id

    @refund_product_id.setter
    def refund_product_id(self, value):
        self.__refund_product_id = value

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
        if self.refund_product_id is not None:
            dictionary['refundProductId'] = self.refund_product_id
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'refundProductId' in dictionary:
            self.refund_product_id = dictionary['refundProductId']
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
