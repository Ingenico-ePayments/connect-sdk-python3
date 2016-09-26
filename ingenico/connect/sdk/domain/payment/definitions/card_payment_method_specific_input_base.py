#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class CardPaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):
    """
    Class CardPaymentMethodSpecificInputBase
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardPaymentMethodSpecificInputBase
    
    Attributes:
        customer_reference:                    str
        recurring_payment_sequence_indicator:  str
        skip_authentication:                   bool
        skip_fraud_service:                    bool
        token:                                 str
     """

    customer_reference = None
    recurring_payment_sequence_indicator = None
    skip_authentication = None
    skip_fraud_service = None
    token = None

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInputBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customerReference', self.customer_reference)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'skipAuthentication', self.skip_authentication)
        self._add_to_dictionary(dictionary, 'skipFraudService', self.skip_fraud_service)
        self._add_to_dictionary(dictionary, 'token', self.token)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        if 'skipAuthentication' in dictionary:
            self.skip_authentication = dictionary['skipAuthentication']
        if 'skipFraudService' in dictionary:
            self.skip_fraud_service = dictionary['skipFraudService']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
