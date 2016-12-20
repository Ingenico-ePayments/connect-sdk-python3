#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput


class RefundBankMethodSpecificOutput(RefundMethodSpecificOutput):
    """
    Class RefundBankMethodSpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundBankMethodSpecificOutput
    """

    def to_dictionary(self):
        dictionary = super(RefundBankMethodSpecificOutput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundBankMethodSpecificOutput, self).from_dictionary(dictionary)
        return self
