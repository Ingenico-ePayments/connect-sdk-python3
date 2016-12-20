#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput


class RefundCardMethodSpecificOutput(RefundMethodSpecificOutput):
    """
    Class RefundCardMethodSpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundCardMethodSpecificOutput
    """

    def to_dictionary(self):
        dictionary = super(RefundCardMethodSpecificOutput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundCardMethodSpecificOutput, self).from_dictionary(dictionary)
        return self
