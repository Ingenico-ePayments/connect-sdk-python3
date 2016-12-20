#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_payment_method_specific_input import ApprovePaymentPaymentMethodSpecificInput


class ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput(ApprovePaymentPaymentMethodSpecificInput):
    """
    Class ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput
    """

    def to_dictionary(self):
        dictionary = super(ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        return self
