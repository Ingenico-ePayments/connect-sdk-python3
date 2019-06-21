# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.refund_payment_product840_customer_account import RefundPaymentProduct840CustomerAccount


class RefundPaymentProduct840SpecificOutput(DataObject):
    """
    | PayPal refund details
    """

    __customer_account = None

    @property
    def customer_account(self):
        """
        | Object containing the PayPal account details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.refund_payment_product840_customer_account.RefundPaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value):
        self.__customer_account = value

    def to_dictionary(self):
        dictionary = super(RefundPaymentProduct840SpecificOutput, self).to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundPaymentProduct840SpecificOutput, self).from_dictionary(dictionary)
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = RefundPaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        return self
