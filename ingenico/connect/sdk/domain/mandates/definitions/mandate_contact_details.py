# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MandateContactDetails(DataObject):
    """
    | Contact details of the consumer
    """

    __email_address = None
    __phone_number = None

    @property
    def email_address(self):
        """
        | Email address of the consumer
        
        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

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
        dictionary = super(MandateContactDetails, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'emailAddress', self.email_address)
        self._add_to_dictionary(dictionary, 'phoneNumber', self.phone_number)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateContactDetails, self).from_dictionary(dictionary)
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'phoneNumber' in dictionary:
            self.phone_number = dictionary['phoneNumber']
        return self
