# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MandateAddress(DataObject):
    """
    | Address details of the consumer
    """

    __city = None
    __country_code = None
    __house_number = None
    __street = None
    __zip = None

    @property
    def city(self):
        """
        | City
        
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
        
        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    def to_dictionary(self):
        dictionary = super(MandateAddress, self).to_dictionary()
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.house_number is not None:
            dictionary['houseNumber'] = self.house_number
        if self.street is not None:
            dictionary['street'] = self.street
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateAddress, self).from_dictionary(dictionary)
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
