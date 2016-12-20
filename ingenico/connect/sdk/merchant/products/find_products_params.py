#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class FindProductsParams(ParamRequest):
    """
    Query parameters for Get payment products
    
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products_get
    """

    __amount = None
    __hide = None
    __is_recurring = None
    __country_code = None
    __locale = None
    __currency_code = None

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
    def hide(self):
        """
        list[str]
        """
        return self.__hide

    @hide.setter
    def hide(self, value):
        self.__hide = value

    def add_hide(self, value):
        """
        :param value: str
        """
        if self.hide is None:
            self.hide = []
        self.hide.append(value)

    @property
    def is_recurring(self):
        """
        bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

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
    def locale(self):
        """
        str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def currency_code(self):
        """
        str
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
        self._add_parameter(result, "amount", self.amount)
        self._add_parameter(result, "hide", self.hide)
        self._add_parameter(result, "isRecurring", self.is_recurring)
        self._add_parameter(result, "countryCode", self.country_code)
        self._add_parameter(result, "locale", self.locale)
        self._add_parameter(result, "currencyCode", self.currency_code)
        return result
