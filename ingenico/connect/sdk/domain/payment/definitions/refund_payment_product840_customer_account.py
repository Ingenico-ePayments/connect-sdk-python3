# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RefundPaymentProduct840CustomerAccount(DataObject):
    """
    | PayPal account details
    """

    __customer_account_status = None
    __customer_address_status = None
    __payer_id = None

    @property
    def customer_account_status(self):
        """
        | Status of the PayPal account.
        | Possible values are:
        
        * verified - PayPal has verified the funding means for this account
        * unverified - PayPal has not verified the funding means for this account
        
        Type: str
        """
        return self.__customer_account_status

    @customer_account_status.setter
    def customer_account_status(self, value):
        self.__customer_account_status = value

    @property
    def customer_address_status(self):
        """
        | Status of the customer's shipping address as registered by PayPal
        | Possible values are:
        
        * none - Status is unknown at PayPal
        * confirmed - The address has been confirmed
        * unconfirmed - The address has not been confirmed
        
        Type: str
        """
        return self.__customer_address_status

    @customer_address_status.setter
    def customer_address_status(self, value):
        self.__customer_address_status = value

    @property
    def payer_id(self):
        """
        | The unique identifier of a PayPal account and will never change in the life cycle of a PayPal account
        
        Type: str
        """
        return self.__payer_id

    @payer_id.setter
    def payer_id(self, value):
        self.__payer_id = value

    def to_dictionary(self):
        dictionary = super(RefundPaymentProduct840CustomerAccount, self).to_dictionary()
        if self.customer_account_status is not None:
            dictionary['customerAccountStatus'] = self.customer_account_status
        if self.customer_address_status is not None:
            dictionary['customerAddressStatus'] = self.customer_address_status
        if self.payer_id is not None:
            dictionary['payerId'] = self.payer_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundPaymentProduct840CustomerAccount, self).from_dictionary(dictionary)
        if 'customerAccountStatus' in dictionary:
            self.customer_account_status = dictionary['customerAccountStatus']
        if 'customerAddressStatus' in dictionary:
            self.customer_address_status = dictionary['customerAddressStatus']
        if 'payerId' in dictionary:
            self.payer_id = dictionary['payerId']
        return self
