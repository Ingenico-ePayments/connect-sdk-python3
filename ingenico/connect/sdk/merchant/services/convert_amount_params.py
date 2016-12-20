#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class ConvertAmountParams(ParamRequest):
    """
    Query parameters for Convert amount
    
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__services_convert_amount_get
    """

    __source = None
    __amount = None
    __target = None

    @property
    def source(self):
        """
        str
        """
        return self.__source

    @source.setter
    def source(self, value):
        self.__source = value

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
    def target(self):
        """
        str
        """
        return self.__target

    @target.setter
    def target(self, value):
        self.__target = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "source", self.source)
        self._add_parameter(result, "amount", self.amount)
        self._add_parameter(result, "target", self.target)
        return result
