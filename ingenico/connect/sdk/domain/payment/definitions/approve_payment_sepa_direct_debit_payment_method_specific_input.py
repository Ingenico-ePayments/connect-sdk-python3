#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_payment_method_specific_input import ApprovePaymentPaymentMethodSpecificInput


class ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput(ApprovePaymentPaymentMethodSpecificInput):
    """
    Class ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput
    """

    def to_dictionary(self):
        dictionary = super(ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        return self
