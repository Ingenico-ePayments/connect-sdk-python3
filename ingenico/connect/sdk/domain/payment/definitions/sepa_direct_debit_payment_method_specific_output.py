#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.fraud_results import FraudResults
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput


class SepaDirectDebitPaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):
    """
    Class SepaDirectDebitPaymentMethodSpecificOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_SepaDirectDebitPaymentMethodSpecificOutput
    
    Attributes:
        fraud_results:  :class:`FraudResults`
     """

    fraud_results = None

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'fraudResults', self.fraud_results)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = FraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        return self
