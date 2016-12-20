#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.token.definitions.mandate_approval import MandateApproval


class ApproveTokenRequest(MandateApproval):
    """
    Class ApproveTokenRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApproveTokenRequest
    """

    def to_dictionary(self):
        dictionary = super(ApproveTokenRequest, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApproveTokenRequest, self).from_dictionary(dictionary)
        return self
