# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation


class CustomerBase(DataObject):
    """
    | Basic information of a consumer
    """

    __company_information = None
    __merchant_customer_id = None
    __vat_number = None

    @property
    def company_information(self):
        """
        | Object containing company information
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.company_information.CompanyInformation`
        """
        return self.__company_information

    @company_information.setter
    def company_information(self, value):
        self.__company_information = value

    @property
    def merchant_customer_id(self):
        """
        | Your identifier for the consumer that can be used as a search criteria in the Global Collect Payment Console and is also included in the Global Collect report files. For Ingenco's Ogone Payment Platform this field is used in the fraud-screening process.
        
        Type: str
        """
        return self.__merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, value):
        self.__merchant_customer_id = value

    @property
    def vat_number(self):
        """
        | Local VAT number of the consumer
        
        Type: str
        """
        return self.__vat_number

    @vat_number.setter
    def vat_number(self, value):
        self.__vat_number = value

    def to_dictionary(self):
        dictionary = super(CustomerBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'companyInformation', self.company_information)
        self._add_to_dictionary(dictionary, 'merchantCustomerId', self.merchant_customer_id)
        self._add_to_dictionary(dictionary, 'vatNumber', self.vat_number)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerBase, self).from_dictionary(dictionary)
        if 'companyInformation' in dictionary:
            if not isinstance(dictionary['companyInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['companyInformation']))
            value = CompanyInformation()
            self.company_information = value.from_dictionary(dictionary['companyInformation'])
        if 'merchantCustomerId' in dictionary:
            self.merchant_customer_id = dictionary['merchantCustomerId']
        if 'vatNumber' in dictionary:
            self.vat_number = dictionary['vatNumber']
        return self
