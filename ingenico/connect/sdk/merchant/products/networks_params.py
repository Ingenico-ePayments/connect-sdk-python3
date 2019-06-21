# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest
from ingenico.connect.sdk.request_param import RequestParam


class NetworksParams(ParamRequest):
    """
    Query parameters for Get payment product networks
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/networks.html
    """

    __country_code = None
    __currency_code = None
    __amount = None
    __is_recurring = None

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
    def currency_code(self):
        """
        | Three-letter ISO currency code representing the currency for the amount
        
        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        self.__currency_code = value

    @property
    def amount(self):
        """
        | Amount in cents and always having 2 decimals
        
        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def is_recurring(self):
        """
        | This allows you to filter networks based on their support for recurring or not
        
        * true
        * false
        
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        if self.country_code is not None:
            result.append(RequestParam("countryCode", self.country_code))
        if self.currency_code is not None:
            result.append(RequestParam("currencyCode", self.currency_code))
        if self.amount is not None:
            result.append(RequestParam("amount", str(self.amount)))
        if self.is_recurring is not None:
            result.append(RequestParam("isRecurring", str(self.is_recurring)))
        return result
