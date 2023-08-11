# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest
from ingenico.connect.sdk.request_param import RequestParam


class FindPaymentsParams(ParamRequest):
    """
    Query parameters for Find payments
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/find.html
    """

    __hosted_checkout_id = None
    __merchant_reference = None
    __merchant_order_id = None
    __offset = None
    __limit = None

    @property
    def hosted_checkout_id(self):
        """
        | Your hosted checkout identifier to filter on.
        
        Type: str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value):
        self.__hosted_checkout_id = value

    @property
    def merchant_reference(self):
        """
        | Your unique transaction reference to filter on. The maximum length is 52 characters for payments that are processed by WL Online Payment Acceptance platform.
        
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
        if self.hosted_checkout_id is not None:
            result.append(RequestParam("hostedCheckoutId", self.hosted_checkout_id))
        if self.merchant_reference is not None:
            result.append(RequestParam("merchantReference", self.merchant_reference))
        if self.merchant_order_id is not None:
            result.append(RequestParam("merchantOrderId", str(self.merchant_order_id)))
        if self.offset is not None:
            result.append(RequestParam("offset", str(self.offset)))
        if self.limit is not None:
            result.append(RequestParam("limit", str(self.limit)))
        return result
