# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal


class RefundCustomer(DataObject):

    __address = None
    __company_information = None
    __contact_details = None
    __fiscal_number = None

    @property
    def address(self):
        """
        | Object containing address details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.address_personal.AddressPersonal`
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

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
    def contact_details(self):
        """
        | Object containing contact details like email address and phone number
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.contact_details_base.ContactDetailsBase`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value):
        self.__contact_details = value

    @property
    def fiscal_number(self):
        """
        | The fiscal registration number of the customer or the tax registration number of the company in case of a business customer. Please find below specifics per country:
        
        * Argentina - Consumer (DNI) with a length of 7 or 8 digits
        * Argentina - Company (CUIT) with a length of 11 digits
        * Brazil - Consumer (CPF) with a length of 11 digits
        * Brazil - Company (CNPJ) with a length of 14 digits
        * Chile - Consumer (RUT) with a length of 9 digits
        * Colombia - Consumer (NIT) with a length of 8, 9 or 10 digits
        * Denmark - Consumer (CPR-nummer or personnummer) with a length of 10 digits
        * Dominican Republic - Consumer (RNC) with a length of 11 digits
        * Finland - Consumer (Finnish: henkilötunnus (abbreviated as HETU)) with a length of 11 characters
        * India - Consumer (PAN) with a length of 10 characters
        * Mexico - Consumer (RFC) with a length of 13 digits
        * Mexico - Company (RFC) with a length of 12 digits
        * Norway - Consumer (fødselsnummer) with a length of 11 digits
        * Peru - Consumer (RUC) with a length of 11 digits
        * Sweden - Consumer (personnummer) with a length of 10 or 12 digits
        * Uruguay - Consumer (CI) with a length of 8 digits
        * Uruguay - Consumer (NIE) with a length of 9 digits
        * Uruguay - Company (RUT) with a length of 12 digits
        
        Type: str
        """
        return self.__fiscal_number

    @fiscal_number.setter
    def fiscal_number(self, value):
        self.__fiscal_number = value

    def to_dictionary(self):
        dictionary = super(RefundCustomer, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.company_information is not None:
            dictionary['companyInformation'] = self.company_information.to_dictionary()
        if self.contact_details is not None:
            dictionary['contactDetails'] = self.contact_details.to_dictionary()
        if self.fiscal_number is not None:
            dictionary['fiscalNumber'] = self.fiscal_number
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundCustomer, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = AddressPersonal()
            self.address = value.from_dictionary(dictionary['address'])
        if 'companyInformation' in dictionary:
            if not isinstance(dictionary['companyInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['companyInformation']))
            value = CompanyInformation()
            self.company_information = value.from_dictionary(dictionary['companyInformation'])
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = ContactDetailsBase()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        if 'fiscalNumber' in dictionary:
            self.fiscal_number = dictionary['fiscalNumber']
        return self
