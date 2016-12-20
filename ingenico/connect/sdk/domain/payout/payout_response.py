#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payout.definitions.payout_result import PayoutResult


class PayoutResponse(PayoutResult):
    """
    Class PayoutResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PayoutResponse
    """

    def to_dictionary(self):
        dictionary = super(PayoutResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutResponse, self).from_dictionary(dictionary)
        return self
