# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class GetCustomerDetailsResponse(DataObject):
    """
    | Output for the retrieval of a customer's details.
    """

    __city = None
    __country = None
    __email_address = None
    __first_name = None
    __fiscal_number = None
    __language_code = None
    __phone_number = None
    __street = None
    __surname = None
    __zip = None

    @property
    def city(self):
        """
        | The city in which the customer resides.
        
        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def country(self):
        """
        | The country in which the customer resides.
        
        Type: str
        """
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def email_address(self):
        """
        | The email address registered to the customer.
        
        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def first_name(self):
        """
        | The first name of the customer
        
        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def fiscal_number(self):
        """
        | The fiscal number (SSN) for the consumer.
        
        Type: str
        """
        return self.__fiscal_number

    @fiscal_number.setter
    def fiscal_number(self, value):
        self.__fiscal_number = value

    @property
    def language_code(self):
        """
        | The code of the language used by the customer.
        
        Type: str
        """
        return self.__language_code

    @language_code.setter
    def language_code(self, value):
        self.__language_code = value

    @property
    def phone_number(self):
        """
        | The phone number registered to the customer.
        
        Type: str
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def street(self):
        """
        | The street on which the customer resides.
        
        Type: str
        """
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def surname(self):
        """
        | The surname or family name of the customer.
        
        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def zip(self):
        """
        | The ZIP or postal code for the area in which the customer resides.
        
        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    def to_dictionary(self):
        dictionary = super(GetCustomerDetailsResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'city', self.city)
        self._add_to_dictionary(dictionary, 'country', self.country)
        self._add_to_dictionary(dictionary, 'emailAddress', self.email_address)
        self._add_to_dictionary(dictionary, 'firstName', self.first_name)
        self._add_to_dictionary(dictionary, 'fiscalNumber', self.fiscal_number)
        self._add_to_dictionary(dictionary, 'languageCode', self.language_code)
        self._add_to_dictionary(dictionary, 'phoneNumber', self.phone_number)
        self._add_to_dictionary(dictionary, 'street', self.street)
        self._add_to_dictionary(dictionary, 'surname', self.surname)
        self._add_to_dictionary(dictionary, 'zip', self.zip)
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetCustomerDetailsResponse, self).from_dictionary(dictionary)
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'country' in dictionary:
            self.country = dictionary['country']
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'fiscalNumber' in dictionary:
            self.fiscal_number = dictionary['fiscalNumber']
        if 'languageCode' in dictionary:
            self.language_code = dictionary['languageCode']
        if 'phoneNumber' in dictionary:
            self.phone_number = dictionary['phoneNumber']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
