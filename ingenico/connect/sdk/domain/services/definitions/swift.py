# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class Swift(DataObject):

    __bic = None
    __category = None
    __chips_uid = None
    __extra_info = None
    __po_box_country = None
    __po_box_location = None
    __po_box_number = None
    __po_box_zip = None
    __routing_bic = None
    __services = None

    @property
    def bic(self):
        """
        | The BIC is the Business Identifier Code, also known as SWIFT or Bank Identifier code. It is a code with an internationally agreed format to Identify a specific bank or even branch. The BIC contains 8 or 11 positions: the first 4 contain the bank code, followed by the country code and location code.
        
        Type: str
        """
        return self.__bic

    @bic.setter
    def bic(self, value):
        self.__bic = value

    @property
    def category(self):
        """
        | SWIFT category
        
        Type: str
        """
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def chips_uid(self):
        """
        | Clearing House Interbank Payments System (CHIPS) UID
        | CHIPS is one half of the primary US network of large-value domestic and international payments.
        
        Type: str
        """
        return self.__chips_uid

    @chips_uid.setter
    def chips_uid(self, value):
        self.__chips_uid = value

    @property
    def extra_info(self):
        """
        | SWIFT extra information
        
        Type: str
        """
        return self.__extra_info

    @extra_info.setter
    def extra_info(self, value):
        self.__extra_info = value

    @property
    def po_box_country(self):
        """
        | Institution PO Box country
        
        Type: str
        """
        return self.__po_box_country

    @po_box_country.setter
    def po_box_country(self, value):
        self.__po_box_country = value

    @property
    def po_box_location(self):
        """
        | Institution PO Box location
        
        Type: str
        """
        return self.__po_box_location

    @po_box_location.setter
    def po_box_location(self, value):
        self.__po_box_location = value

    @property
    def po_box_number(self):
        """
        | Institution PO Box number
        
        Type: str
        """
        return self.__po_box_number

    @po_box_number.setter
    def po_box_number(self, value):
        self.__po_box_number = value

    @property
    def po_box_zip(self):
        """
        | Institution PO Box ZIP
        
        Type: str
        """
        return self.__po_box_zip

    @po_box_zip.setter
    def po_box_zip(self, value):
        self.__po_box_zip = value

    @property
    def routing_bic(self):
        """
        | Payment routing BIC
        
        Type: str
        """
        return self.__routing_bic

    @routing_bic.setter
    def routing_bic(self, value):
        self.__routing_bic = value

    @property
    def services(self):
        """
        | SWIFT services
        
        Type: str
        """
        return self.__services

    @services.setter
    def services(self, value):
        self.__services = value

    def to_dictionary(self):
        dictionary = super(Swift, self).to_dictionary()
        if self.bic is not None:
            dictionary['bic'] = self.bic
        if self.category is not None:
            dictionary['category'] = self.category
        if self.chips_uid is not None:
            dictionary['chipsUID'] = self.chips_uid
        if self.extra_info is not None:
            dictionary['extraInfo'] = self.extra_info
        if self.po_box_country is not None:
            dictionary['poBoxCountry'] = self.po_box_country
        if self.po_box_location is not None:
            dictionary['poBoxLocation'] = self.po_box_location
        if self.po_box_number is not None:
            dictionary['poBoxNumber'] = self.po_box_number
        if self.po_box_zip is not None:
            dictionary['poBoxZip'] = self.po_box_zip
        if self.routing_bic is not None:
            dictionary['routingBic'] = self.routing_bic
        if self.services is not None:
            dictionary['services'] = self.services
        return dictionary

    def from_dictionary(self, dictionary):
        super(Swift, self).from_dictionary(dictionary)
        if 'bic' in dictionary:
            self.bic = dictionary['bic']
        if 'category' in dictionary:
            self.category = dictionary['category']
        if 'chipsUID' in dictionary:
            self.chips_uid = dictionary['chipsUID']
        if 'extraInfo' in dictionary:
            self.extra_info = dictionary['extraInfo']
        if 'poBoxCountry' in dictionary:
            self.po_box_country = dictionary['poBoxCountry']
        if 'poBoxLocation' in dictionary:
            self.po_box_location = dictionary['poBoxLocation']
        if 'poBoxNumber' in dictionary:
            self.po_box_number = dictionary['poBoxNumber']
        if 'poBoxZip' in dictionary:
            self.po_box_zip = dictionary['poBoxZip']
        if 'routingBic' in dictionary:
            self.routing_bic = dictionary['routingBic']
        if 'services' in dictionary:
            self.services = dictionary['services']
        return self
