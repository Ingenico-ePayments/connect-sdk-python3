# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase


class ContactDetails(ContactDetailsBase):

    __fax_number = None
    __phone_number = None

    @property
    def fax_number(self):
        """
        | Fax number of the consumer
        
        Type: str
        """
        return self.__fax_number

    @fax_number.setter
    def fax_number(self, value):
        self.__fax_number = value

    @property
    def phone_number(self):
        """
        | Phone number of the consumer
        
        Type: str
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    def to_dictionary(self):
        dictionary = super(ContactDetails, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'faxNumber', self.fax_number)
        self._add_to_dictionary(dictionary, 'phoneNumber', self.phone_number)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetails, self).from_dictionary(dictionary)
        if 'faxNumber' in dictionary:
            self.fax_number = dictionary['faxNumber']
        if 'phoneNumber' in dictionary:
            self.phone_number = dictionary['phoneNumber']
        return self
