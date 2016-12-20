#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input_base import BankTransferPaymentMethodSpecificInputBase


class BankTransferPaymentMethodSpecificInput(BankTransferPaymentMethodSpecificInputBase):
    """
    Class BankTransferPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankTransferPaymentMethodSpecificInput
    """

    def to_dictionary(self):
        dictionary = super(BankTransferPaymentMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankTransferPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        return self
