#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.card_essentials import CardEssentials
from ingenico.connect.sdk.domain.definitions.card_fraud_results import CardFraudResults
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.three_d_secure_results import ThreeDSecureResults


class CardPaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):
    """
    Class CardPaymentMethodSpecificOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardPaymentMethodSpecificOutput
    
    Attributes:
        authorisation_code:      str
        card:                    :class:`CardEssentials`
        fraud_results:           :class:`CardFraudResults`
        three_d_secure_results:  :class:`ThreeDSecureResults`
     """

    authorisation_code = None
    card = None
    fraud_results = None
    three_d_secure_results = None

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'authorisationCode', self.authorisation_code)
        self._add_to_dictionary(dictionary, 'card', self.card)
        self._add_to_dictionary(dictionary, 'fraudResults', self.fraud_results)
        self._add_to_dictionary(dictionary, 'threeDSecureResults', self.three_d_secure_results)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardEssentials()
            self.card = value.from_dictionary(dictionary['card'])
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = CardFraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'threeDSecureResults' in dictionary:
            if not isinstance(dictionary['threeDSecureResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureResults']))
            value = ThreeDSecureResults()
            self.three_d_secure_results = value.from_dictionary(dictionary['threeDSecureResults'])
        return self
