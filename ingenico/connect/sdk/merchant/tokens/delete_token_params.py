#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class DeleteTokenParams(ParamRequest):
    """
    Query parameters for Delete token
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__tokens__tokenId__delete
    
    Attributes:
        mandate_cancel_date:  str
    """

    mandate_cancel_date = None

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "mandateCancelDate", self.mandate_cancel_date)
        return result
