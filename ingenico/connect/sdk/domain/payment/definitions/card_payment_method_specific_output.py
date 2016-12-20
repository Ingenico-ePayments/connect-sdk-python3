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
    """

    __authorisation_code = None
    __card = None
    __fraud_results = None
    __three_d_secure_results = None

    @property
    def authorisation_code(self):
        """
        str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value):
        self.__authorisation_code = value

    @property
    def card(self):
        """
        :class:`CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def fraud_results(self):
        """
        :class:`CardFraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value):
        self.__fraud_results = value

    @property
    def three_d_secure_results(self):
        """
        :class:`ThreeDSecureResults`
        """
        return self.__three_d_secure_results

    @three_d_secure_results.setter
    def three_d_secure_results(self, value):
        self.__three_d_secure_results = value

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
