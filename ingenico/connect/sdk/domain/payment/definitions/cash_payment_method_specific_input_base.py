#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class CashPaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):
    """
    Class CashPaymentMethodSpecificInputBase
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CashPaymentMethodSpecificInputBase
    """

    def to_dictionary(self):
        dictionary = super(CashPaymentMethodSpecificInputBase, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CashPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        return self
