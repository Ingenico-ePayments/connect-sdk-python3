# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest


class FindPaymentsParams(ParamRequest):
    """
    Query parameters for | Find payments
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/find.html
    """

    __merchant_reference = None
    __merchant_order_id = None
    __offset = None
    __limit = None

    @property
    def merchant_reference(self):
        """
        | Your unique transaction reference to filter on.
        
        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value):
        self.__merchant_reference = value

    @property
    def merchant_order_id(self):
        """
        | Your order identifier to filter on.
        
        Type: int
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self.__merchant_order_id = value

    @property
    def offset(self):
        """
        | The zero-based index of the first payment in the result. If omitted, the offset will be 0.
        
        Type: int
        """
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = value

    @property
    def limit(self):
        """
        | The maximum number of payments to return, with a maximum of 100. If omitted, the limit will be 10.
        
        Type: int
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "merchantReference", self.merchant_reference)
        self._add_parameter(result, "merchantOrderId", self.merchant_order_id)
        self._add_parameter(result, "offset", self.offset)
        self._add_parameter(result, "limit", self.limit)
        return result
