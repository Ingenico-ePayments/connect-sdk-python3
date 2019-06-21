# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.payment.definitions.payment_product840_customer_account import PaymentProduct840CustomerAccount
from ingenico.connect.sdk.domain.payment.definitions.protection_eligibility import ProtectionEligibility


class PaymentProduct840SpecificOutput(DataObject):

    __customer_account = None
    __customer_address = None
    __protection_eligibility = None

    @property
    def customer_account(self):
        """
        | Object containing the details of the PayPal account
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment_product840_customer_account.PaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value):
        self.__customer_account = value

    @property
    def customer_address(self):
        """
        | Object containing the address details of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        """
        return self.__customer_address

    @customer_address.setter
    def customer_address(self, value):
        self.__customer_address = value

    @property
    def protection_eligibility(self):
        """
        | Protection Eligibility data of the PayPal customer
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.protection_eligibility.ProtectionEligibility`
        """
        return self.__protection_eligibility

    @protection_eligibility.setter
    def protection_eligibility(self, value):
        self.__protection_eligibility = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct840SpecificOutput, self).to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        if self.customer_address is not None:
            dictionary['customerAddress'] = self.customer_address.to_dictionary()
        if self.protection_eligibility is not None:
            dictionary['protectionEligibility'] = self.protection_eligibility.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct840SpecificOutput, self).from_dictionary(dictionary)
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = PaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        if 'customerAddress' in dictionary:
            if not isinstance(dictionary['customerAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAddress']))
            value = Address()
            self.customer_address = value.from_dictionary(dictionary['customerAddress'])
        if 'protectionEligibility' in dictionary:
            if not isinstance(dictionary['protectionEligibility'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['protectionEligibility']))
            value = ProtectionEligibility()
            self.protection_eligibility = value.from_dictionary(dictionary['protectionEligibility'])
        return self
