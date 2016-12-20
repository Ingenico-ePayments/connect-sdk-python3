#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput


class InvoicePaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):
    """
    Class InvoicePaymentMethodSpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_InvoicePaymentMethodSpecificOutput
    """

    def to_dictionary(self):
        dictionary = super(InvoicePaymentMethodSpecificOutput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(InvoicePaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        return self
