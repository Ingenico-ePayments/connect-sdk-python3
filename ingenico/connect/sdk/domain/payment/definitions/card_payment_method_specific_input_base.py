#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class CardPaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):
    """
    Class CardPaymentMethodSpecificInputBase
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardPaymentMethodSpecificInputBase
    """

    __authorization_mode = None
    __customer_reference = None
    __recurring_payment_sequence_indicator = None
    __requires_approval = None
    __skip_authentication = None
    __skip_fraud_service = None
    __token = None
    __tokenize = None

    @property
    def authorization_mode(self):
        """
        str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value):
        self.__authorization_mode = value

    @property
    def customer_reference(self):
        """
        str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value):
        self.__customer_reference = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value):
        self.__recurring_payment_sequence_indicator = value

    @property
    def requires_approval(self):
        """
        bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value):
        self.__requires_approval = value

    @property
    def skip_authentication(self):
        """
        bool
        """
        return self.__skip_authentication

    @skip_authentication.setter
    def skip_authentication(self, value):
        self.__skip_authentication = value

    @property
    def skip_fraud_service(self):
        """
        bool
        """
        return self.__skip_fraud_service

    @skip_fraud_service.setter
    def skip_fraud_service(self, value):
        self.__skip_fraud_service = value

    @property
    def token(self):
        """
        str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    @property
    def tokenize(self):
        """
        bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value):
        self.__tokenize = value

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInputBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'authorizationMode', self.authorization_mode)
        self._add_to_dictionary(dictionary, 'customerReference', self.customer_reference)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'requiresApproval', self.requires_approval)
        self._add_to_dictionary(dictionary, 'skipAuthentication', self.skip_authentication)
        self._add_to_dictionary(dictionary, 'skipFraudService', self.skip_fraud_service)
        self._add_to_dictionary(dictionary, 'token', self.token)
        self._add_to_dictionary(dictionary, 'tokenize', self.tokenize)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        if 'skipAuthentication' in dictionary:
            self.skip_authentication = dictionary['skipAuthentication']
        if 'skipFraudService' in dictionary:
            self.skip_fraud_service = dictionary['skipFraudService']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self
