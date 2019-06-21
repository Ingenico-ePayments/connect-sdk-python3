# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.param_request import ParamRequest
from ingenico.connect.sdk.request_param import RequestParam


class DeleteTokenParams(ParamRequest):
    """
    Query parameters for Delete token
    
    See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/tokens/delete.html
    """

    __mandate_cancel_date = None

    @property
    def mandate_cancel_date(self):
        """
        | Date of the mandate cancellation
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__mandate_cancel_date

    @mandate_cancel_date.setter
    def mandate_cancel_date(self, value):
        self.__mandate_cancel_date = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        if self.mandate_cancel_date is not None:
            result.append(RequestParam("mandateCancelDate", self.mandate_cancel_date))
        return result
