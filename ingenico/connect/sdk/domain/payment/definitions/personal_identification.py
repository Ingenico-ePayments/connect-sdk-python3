# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject


class PersonalIdentification(DataObject):

    __id_issuing_country_code = None
    __id_type = None
    __id_value = None

    @property
    def id_issuing_country_code(self):
        """
        | ISO 3166-1 alpha-2 country code of the country that issued the identification document
        
        Type: str
        """
        return self.__id_issuing_country_code

    @id_issuing_country_code.setter
    def id_issuing_country_code(self, value):
        self.__id_issuing_country_code = value

    @property
    def id_type(self):
        """
        | Indicates the type of identification 
        
        * nationalIdentification = The provided idValue is a national identification number.
        * passportNumber = The provided idValue is a passport number.
        * driverLicense = The provided idValue is driving License of the individual.
        * companyRegistrationNumber = The provided idValue is a company identifier. It verifies its legal existence as an incorporated entity.
        * socialSecurityNumber =n The provided idValue is a social security number, issued to an individual by the individual's government.
        * alienRegistrationNumber = The provided idValue is an alien registration number, provided by immigration services of a country.
        * lawEnforcementIdentification = The provided idValue is an alien registration number, provided by immigration services of a country.
        * militaryIdentification = The provided idValue is an identification issued to military personnel of a country.
        
        Type: str
        """
        return self.__id_type

    @id_type.setter
    def id_type(self, value):
        self.__id_type = value

    @property
    def id_value(self):
        """
        | The value of the identification
        
        Type: str
        """
        return self.__id_value

    @id_value.setter
    def id_value(self, value):
        self.__id_value = value

    def to_dictionary(self):
        dictionary = super(PersonalIdentification, self).to_dictionary()
        if self.id_issuing_country_code is not None:
            dictionary['idIssuingCountryCode'] = self.id_issuing_country_code
        if self.id_type is not None:
            dictionary['idType'] = self.id_type
        if self.id_value is not None:
            dictionary['idValue'] = self.id_value
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalIdentification, self).from_dictionary(dictionary)
        if 'idIssuingCountryCode' in dictionary:
            self.id_issuing_country_code = dictionary['idIssuingCountryCode']
        if 'idType' in dictionary:
            self.id_type = dictionary['idType']
        if 'idValue' in dictionary:
            self.id_value = dictionary['idValue']
        return self
