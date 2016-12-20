#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class NetworksParams(ParamRequest):
    """
    Query parameters for Get payment product networks
    
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products__paymentProductId__networks_get
    """

    __country_code = None
    __currency_code = None
    __amount = None
    __is_recurring = None

    @property
    def country_code(self):
        """
        str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

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
    def amount(self):
        """
        int
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def is_recurring(self):
        """
        bool
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
        self._add_parameter(result, "countryCode", self.country_code)
        self._add_parameter(result, "currencyCode", self.currency_code)
        self._add_parameter(result, "amount", self.amount)
        self._add_parameter(result, "isRecurring", self.is_recurring)
        return result
