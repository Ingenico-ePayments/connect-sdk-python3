# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest
from ingenico.connect.sdk.request_param import RequestParam


class PrivacypolicyParams(ParamRequest):
    """
    Query parameters for Get privacy policy
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/services/privacypolicy.html
    """

    __locale = None
    __payment_product_id = None

    @property
    def locale(self):
        """
        | Locale in which the privacy policy should be returned. Uses your default locale when none is provided.
        
        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def payment_product_id(self):
        """
        | ID of the payment product for which you wish to retrieve the privacy policy. When no ID is provided you will receive all privacy policies for your payment products.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        if self.locale is not None:
            result.append(RequestParam("locale", self.locale))
        if self.payment_product_id is not None:
            result.append(RequestParam("paymentProductId", str(self.payment_product_id)))
        return result
