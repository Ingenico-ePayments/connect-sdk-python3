# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class AbstractCardPaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):

    __authorization_mode = None
    __customer_reference = None
    __recurring_payment_sequence_indicator = None
    __requires_approval = None
    __skip_authentication = None
    __skip_fraud_service = None
    __token = None
    __tokenize = None
    __transaction_channel = None
    __unscheduled_card_on_file_indicator = None
    __unscheduled_card_on_file_requestor = None

    @property
    def authorization_mode(self):
        """
        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value):
        self.__authorization_mode = value

    @property
    def customer_reference(self):
        """
        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value):
        self.__customer_reference = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        Type: str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value):
        self.__recurring_payment_sequence_indicator = value

    @property
    def requires_approval(self):
        """
        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value):
        self.__requires_approval = value

    @property
    def skip_authentication(self):
        """
        Type: bool
        """
        return self.__skip_authentication

    @skip_authentication.setter
    def skip_authentication(self, value):
        self.__skip_authentication = value

    @property
    def skip_fraud_service(self):
        """
        Type: bool
        """
        return self.__skip_fraud_service

    @skip_fraud_service.setter
    def skip_fraud_service(self, value):
        self.__skip_fraud_service = value

    @property
    def token(self):
        """
        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    @property
    def tokenize(self):
        """
        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value):
        self.__tokenize = value

    @property
    def transaction_channel(self):
        """
        Type: str
        """
        return self.__transaction_channel

    @transaction_channel.setter
    def transaction_channel(self, value):
        self.__transaction_channel = value

    @property
    def unscheduled_card_on_file_indicator(self):
        """
        Type: str
        """
        return self.__unscheduled_card_on_file_indicator

    @unscheduled_card_on_file_indicator.setter
    def unscheduled_card_on_file_indicator(self, value):
        self.__unscheduled_card_on_file_indicator = value

    @property
    def unscheduled_card_on_file_requestor(self):
        """
        Type: str
        """
        return self.__unscheduled_card_on_file_requestor

    @unscheduled_card_on_file_requestor.setter
    def unscheduled_card_on_file_requestor(self, value):
        self.__unscheduled_card_on_file_requestor = value

    def to_dictionary(self):
        dictionary = super(AbstractCardPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'authorizationMode', self.authorization_mode)
        self._add_to_dictionary(dictionary, 'customerReference', self.customer_reference)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'requiresApproval', self.requires_approval)
        self._add_to_dictionary(dictionary, 'skipAuthentication', self.skip_authentication)
        self._add_to_dictionary(dictionary, 'skipFraudService', self.skip_fraud_service)
        self._add_to_dictionary(dictionary, 'token', self.token)
        self._add_to_dictionary(dictionary, 'tokenize', self.tokenize)
        self._add_to_dictionary(dictionary, 'transactionChannel', self.transaction_channel)
        self._add_to_dictionary(dictionary, 'unscheduledCardOnFileIndicator', self.unscheduled_card_on_file_indicator)
        self._add_to_dictionary(dictionary, 'unscheduledCardOnFileRequestor', self.unscheduled_card_on_file_requestor)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractCardPaymentMethodSpecificInput, self).from_dictionary(dictionary)
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
        if 'transactionChannel' in dictionary:
            self.transaction_channel = dictionary['transactionChannel']
        if 'unscheduledCardOnFileIndicator' in dictionary:
            self.unscheduled_card_on_file_indicator = dictionary['unscheduledCardOnFileIndicator']
        if 'unscheduledCardOnFileRequestor' in dictionary:
            self.unscheduled_card_on_file_requestor = dictionary['unscheduledCardOnFileRequestor']
        return self
