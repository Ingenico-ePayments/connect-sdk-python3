#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class RedirectPaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):
    """
    Class RedirectPaymentMethodSpecificInputBase
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RedirectPaymentMethodSpecificInputBase
    
    Attributes:
        recurring_payment_sequence_indicator:  str
        token:                                 str
     """

    recurring_payment_sequence_indicator = None
    token = None

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificInputBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'token', self.token)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
