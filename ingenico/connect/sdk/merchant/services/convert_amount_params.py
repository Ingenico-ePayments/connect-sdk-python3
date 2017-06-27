# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest


class ConvertAmountParams(ParamRequest):
    """
    Query parameters for | Convert amount
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/services/convertAmount.html
    """

    __source = None
    __target = None
    __amount = None

    @property
    def source(self):
        """
        | Three-letter ISO currency code representing the source currency
        
        Type: str
        """
        return self.__source

    @source.setter
    def source(self, value):
        self.__source = value

    @property
    def target(self):
        """
        | Three-letter ISO currency code representing the target currency
        
        Type: str
        """
        return self.__target

    @target.setter
    def target(self, value):
        self.__target = value

    @property
    def amount(self):
        """
        | Amount to be converted in cents and always having 2 decimals
        
        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "source", self.source)
        self._add_parameter(result, "target", self.target)
        self._add_parameter(result, "amount", self.amount)
        return result
