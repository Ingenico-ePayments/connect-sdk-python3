#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class InvoicePaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):
    """
    Class InvoicePaymentMethodSpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_InvoicePaymentMethodSpecificInput
    
    Attributes:
        additional_reference:  str
     """

    additional_reference = None

    def to_dictionary(self):
        dictionary = super(InvoicePaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalReference', self.additional_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(InvoicePaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'additionalReference' in dictionary:
            self.additional_reference = dictionary['additionalReference']
        return self
