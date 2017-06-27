# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal


class RefundCustomer(DataObject):

    __address = None
    __company_information = None
    __contact_details = None

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

    def to_dictionary(self):
        dictionary = super(RefundCustomer, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'address', self.address)
        self._add_to_dictionary(dictionary, 'companyInformation', self.company_information)
        self._add_to_dictionary(dictionary, 'contactDetails', self.contact_details)
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
        return self
