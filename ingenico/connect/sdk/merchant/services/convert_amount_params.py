#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class ConvertAmountParams(ParamRequest):
    """
    Query parameters for Convert amount
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__services_convert_amount_get
    
    Attributes:
        source:  str
        amount:  int
        target:  str
    """

    source = None
    amount = None
    target = None

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "source", self.source)
        self._add_parameter(result, "amount", self.amount)
        self._add_parameter(result, "target", self.target)
        return result
