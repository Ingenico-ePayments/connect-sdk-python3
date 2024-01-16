# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject


class InAuth(DataObject):

    __device_category = None
    __device_id = None
    __risk_score = None
    __true_ip_address = None
    __true_ip_address_country = None

    @property
    def device_category(self):
        """
        | The type of device used by the customer. Example values:
        
        * SMARTPHONE
        * PERSONAL_COMPUTER 
        * TABLET 
        * WEARABLE_COMPUTER 
        * GAME_CONSOLE 
        * SMART_TV 
        * PDA 
        * OTHER 
        * UNKNOWN
        
        Type: str
        """
        return self.__device_category

    @device_category.setter
    def device_category(self, value):
        self.__device_category = value

    @property
    def device_id(self):
        """
        | This is the device fingerprint value. Based on the amount of data that the device fingerprint collector script was able to collect, this will be a proxy ID for the device used by the customer.
        
        Type: str
        """
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        self.__device_id = value

    @property
    def risk_score(self):
        """
        | The score calculated on the basis of Anomalies, Velocity, Location, Integrity, List-Based, and Device Reputation. Range of the score is between 0 and 100. A lower value is better.
        
        Type: str
        """
        return self.__risk_score

    @risk_score.setter
    def risk_score(self, value):
        self.__risk_score = value

    @property
    def true_ip_address(self):
        """
        | The true IP address as determined by inAuth. This might be different from the IP address that you are seeing on your side due to the proxy piercing technology deployed by inAuth.
        
        Type: str
        """
        return self.__true_ip_address

    @true_ip_address.setter
    def true_ip_address(self, value):
        self.__true_ip_address = value

    @property
    def true_ip_address_country(self):
        """
        | The country of the customer based on the location of the True IP Address determined by inAuth.
        
        Type: str
        """
        return self.__true_ip_address_country

    @true_ip_address_country.setter
    def true_ip_address_country(self, value):
        self.__true_ip_address_country = value

    def to_dictionary(self):
        dictionary = super(InAuth, self).to_dictionary()
        if self.device_category is not None:
            dictionary['deviceCategory'] = self.device_category
        if self.device_id is not None:
            dictionary['deviceId'] = self.device_id
        if self.risk_score is not None:
            dictionary['riskScore'] = self.risk_score
        if self.true_ip_address is not None:
            dictionary['trueIpAddress'] = self.true_ip_address
        if self.true_ip_address_country is not None:
            dictionary['trueIpAddressCountry'] = self.true_ip_address_country
        return dictionary

    def from_dictionary(self, dictionary):
        super(InAuth, self).from_dictionary(dictionary)
        if 'deviceCategory' in dictionary:
            self.device_category = dictionary['deviceCategory']
        if 'deviceId' in dictionary:
            self.device_id = dictionary['deviceId']
        if 'riskScore' in dictionary:
            self.risk_score = dictionary['riskScore']
        if 'trueIpAddress' in dictionary:
            self.true_ip_address = dictionary['trueIpAddress']
        if 'trueIpAddressCountry' in dictionary:
            self.true_ip_address_country = dictionary['trueIpAddressCountry']
        return self
