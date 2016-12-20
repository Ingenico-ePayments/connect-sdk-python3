#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class DirectoryParams(ParamRequest):
    """
    Query parameters for Get payment product directory
    
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products__paymentProductId__directory_get
    """

    __currency_code = None
    __country_code = None

    @property
    def currency_code(self):
        """
        str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        self.__currency_code = value

    @property
    def country_code(self):
        """
        str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "currencyCode", self.currency_code)
        self._add_parameter(result, "countryCode", self.country_code)
        return result
