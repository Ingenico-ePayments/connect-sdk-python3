# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest
from ingenico.connect.sdk.request_param import RequestParam


class DirectoryParams(ParamRequest):
    """
    Query parameters for Get payment product directory
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/directory.html
    """

    __country_code = None
    __currency_code = None

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
        | Three-letter ISO currency code representing the currency of the transaction
        
        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        self.__currency_code = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        if self.country_code is not None:
            result.append(RequestParam("countryCode", self.country_code))
        if self.currency_code is not None:
            result.append(RequestParam("currencyCode", self.currency_code))
        return result
