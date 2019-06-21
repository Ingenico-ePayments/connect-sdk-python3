# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class Address(DataObject):

    __additional_info = None
    __city = None
    __country_code = None
    __house_number = None
    __state = None
    __state_code = None
    __street = None
    __zip = None

    @property
    def additional_info(self):
        """
        | Additional address information
        
        Type: str
        """
        return self.__additional_info

    @additional_info.setter
    def additional_info(self, value):
        self.__additional_info = value

    @property
    def city(self):
        """
        | City
        | Note: For payments with product 1503 the maximum length is not 40 but 20.
        
        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def country_code(self):
        """
        | ISO 3166-1 alpha-2 country code
        
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def house_number(self):
        """
        | House number
        
        Type: str
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, value):
        self.__house_number = value

    @property
    def state(self):
        """
        | Full name of the state or province
        
        Type: str
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def state_code(self):
        """
        | State code
        | Note: For payments with product 1503 the maximum length is not 9 but 2.
        
        Type: str
        """
        return self.__state_code

    @state_code.setter
    def state_code(self, value):
        self.__state_code = value

    @property
    def street(self):
        """
        | Streetname
        
        Type: str
        """
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def zip(self):
        """
        | Zip code
        | Note: For payments with product 1503 the maximum length is not 10 but 8.
        
        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    def to_dictionary(self):
        dictionary = super(Address, self).to_dictionary()
        if self.additional_info is not None:
            dictionary['additionalInfo'] = self.additional_info
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.house_number is not None:
            dictionary['houseNumber'] = self.house_number
        if self.state is not None:
            dictionary['state'] = self.state
        if self.state_code is not None:
            dictionary['stateCode'] = self.state_code
        if self.street is not None:
            dictionary['street'] = self.street
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary):
        super(Address, self).from_dictionary(dictionary)
        if 'additionalInfo' in dictionary:
            self.additional_info = dictionary['additionalInfo']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'state' in dictionary:
            self.state = dictionary['state']
        if 'stateCode' in dictionary:
            self.state_code = dictionary['stateCode']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
