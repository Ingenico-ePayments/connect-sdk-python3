# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.payment.definitions.trustly_bank_account import TrustlyBankAccount


class PaymentProduct806SpecificOutput(DataObject):

    __billing_address = None
    __customer_account = None

    @property
    def billing_address(self):
        """
        | Object containing the billing address details of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value

    @property
    def customer_account(self):
        """
        | Object containing the account details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.trustly_bank_account.TrustlyBankAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value):
        self.__customer_account = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct806SpecificOutput, self).to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct806SpecificOutput, self).from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = TrustlyBankAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        return self
