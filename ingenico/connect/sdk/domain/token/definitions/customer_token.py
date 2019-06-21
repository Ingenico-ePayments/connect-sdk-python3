# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.customer_base import CustomerBase
from ingenico.connect.sdk.domain.token.definitions.personal_information_token import PersonalInformationToken


class CustomerToken(CustomerBase):

    __billing_address = None
    __personal_information = None

    @property
    def billing_address(self):
        """
        | Object containing the billing address details
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value

    @property
    def personal_information(self):
        """
        | Object containing personal information of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.personal_information_token.PersonalInformationToken`
        """
        return self.__personal_information

    @personal_information.setter
    def personal_information(self, value):
        self.__personal_information = value

    def to_dictionary(self):
        dictionary = super(CustomerToken, self).to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.personal_information is not None:
            dictionary['personalInformation'] = self.personal_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerToken, self).from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = PersonalInformationToken()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        return self
