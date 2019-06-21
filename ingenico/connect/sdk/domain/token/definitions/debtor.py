# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class Debtor(DataObject):
    """
    | This object describes the the consumer (or company) that will be debited and it is part of a SEPA Direct Debit Mandate
    """

    __additional_address_info = None
    __city = None
    __country_code = None
    __first_name = None
    __house_number = None
    __state = None
    __state_code = None
    __street = None
    __surname = None
    __surname_prefix = None
    __zip = None

    @property
    def additional_address_info(self):
        """
        | Additional information about the debtor's address, like Suite II, Apartment 2a
        
        Type: str
        """
        return self.__additional_address_info

    @additional_address_info.setter
    def additional_address_info(self, value):
        self.__additional_address_info = value

    @property
    def city(self):
        """
        | City of the debtor's address
        
        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def country_code(self):
        """
        | ISO 3166-1 alpha-2 country code of the debtor's address
        
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def first_name(self):
        """
        | Debtor first name
        
        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def house_number(self):
        """
        | House number of the debtor's address
        
        Type: str
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, value):
        self.__house_number = value

    @property
    def state(self):
        """
        | State of debtor address
        
        Type: str
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def state_code(self):
        """
        | State Code of the debtor's address
        
        Type: str
        """
        return self.__state_code

    @state_code.setter
    def state_code(self, value):
        self.__state_code = value

    @property
    def street(self):
        """
        | Street of debtor's address
        
        Type: str
        """
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def surname(self):
        """
        | Debtor's last name
        
        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def surname_prefix(self):
        """
        | Prefix of the debtor's last name
        
        Type: str
        """
        return self.__surname_prefix

    @surname_prefix.setter
    def surname_prefix(self, value):
        self.__surname_prefix = value

    @property
    def zip(self):
        """
        | ZIP code of the debtor's address
        
        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    def to_dictionary(self):
        dictionary = super(Debtor, self).to_dictionary()
        if self.additional_address_info is not None:
            dictionary['additionalAddressInfo'] = self.additional_address_info
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.house_number is not None:
            dictionary['houseNumber'] = self.house_number
        if self.state is not None:
            dictionary['state'] = self.state
        if self.state_code is not None:
            dictionary['stateCode'] = self.state_code
        if self.street is not None:
            dictionary['street'] = self.street
        if self.surname is not None:
            dictionary['surname'] = self.surname
        if self.surname_prefix is not None:
            dictionary['surnamePrefix'] = self.surname_prefix
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary):
        super(Debtor, self).from_dictionary(dictionary)
        if 'additionalAddressInfo' in dictionary:
            self.additional_address_info = dictionary['additionalAddressInfo']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'state' in dictionary:
            self.state = dictionary['state']
        if 'stateCode' in dictionary:
            self.state_code = dictionary['stateCode']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'surnamePrefix' in dictionary:
            self.surname_prefix = dictionary['surnamePrefix']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
