#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.refund.definitions.refund_result import RefundResult


class RefundResponse(RefundResult):
    """
    Class RefundResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundResponse
    """

    def to_dictionary(self):
        dictionary = super(RefundResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundResponse, self).from_dictionary(dictionary)
        return self
