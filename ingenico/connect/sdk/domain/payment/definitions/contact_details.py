# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase


class ContactDetails(ContactDetailsBase):

    __fax_number = None
    __mobile_phone_number = None
    __phone_number = None
    __work_phone_number = None

    @property
    def fax_number(self):
        """
        | Fax number of the customer
        
        Type: str
        """
        return self.__fax_number

    @fax_number.setter
    def fax_number(self, value):
        self.__fax_number = value

    @property
    def mobile_phone_number(self):
        """
        | International version of the mobile phone number of the customer including the leading + (i.e. +16127779311)
        
        Type: str
        """
        return self.__mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, value):
        self.__mobile_phone_number = value

    @property
    def phone_number(self):
        """
        | Phone number of the customer
        
        Type: str
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def work_phone_number(self):
        """
        | International version of the work phone number of the customer including the leading + (i.e. +31235671500)
        
        Type: str
        """
        return self.__work_phone_number

    @work_phone_number.setter
    def work_phone_number(self, value):
        self.__work_phone_number = value

    def to_dictionary(self):
        dictionary = super(ContactDetails, self).to_dictionary()
        if self.fax_number is not None:
            dictionary['faxNumber'] = self.fax_number
        if self.mobile_phone_number is not None:
            dictionary['mobilePhoneNumber'] = self.mobile_phone_number
        if self.phone_number is not None:
            dictionary['phoneNumber'] = self.phone_number
        if self.work_phone_number is not None:
            dictionary['workPhoneNumber'] = self.work_phone_number
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetails, self).from_dictionary(dictionary)
        if 'faxNumber' in dictionary:
            self.fax_number = dictionary['faxNumber']
        if 'mobilePhoneNumber' in dictionary:
            self.mobile_phone_number = dictionary['mobilePhoneNumber']
        if 'phoneNumber' in dictionary:
            self.phone_number = dictionary['phoneNumber']
        if 'workPhoneNumber' in dictionary:
            self.work_phone_number = dictionary['workPhoneNumber']
        return self
