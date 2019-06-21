# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.card_recurrence_details import CardRecurrenceDetails


class AbstractCardPaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):

    __authorization_mode = None
    __customer_reference = None
    __recurring = None
    __recurring_payment_sequence_indicator = None
    __requires_approval = None
    __skip_authentication = None
    __skip_fraud_service = None
    __token = None
    __tokenize = None
    __transaction_channel = None
    __unscheduled_card_on_file_indicator = None
    __unscheduled_card_on_file_requestor = None
    __unscheduled_card_on_file_sequence_indicator = None

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
    def recurring(self):
        """
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.card_recurrence_details.CardRecurrenceDetails`
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value):
        self.__recurring = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        Type: str
        
        Deprecated; Use recurring.recurringPaymentSequenceIndicator instead
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
        
        Deprecated; Use threeDSecure.skipAuthentication instead
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
        
        Deprecated; Use unscheduledCardOnFileSequenceIndicator instead
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

    @property
    def unscheduled_card_on_file_sequence_indicator(self):
        """
        Type: str
        """
        return self.__unscheduled_card_on_file_sequence_indicator

    @unscheduled_card_on_file_sequence_indicator.setter
    def unscheduled_card_on_file_sequence_indicator(self, value):
        self.__unscheduled_card_on_file_sequence_indicator = value

    def to_dictionary(self):
        dictionary = super(AbstractCardPaymentMethodSpecificInput, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.customer_reference is not None:
            dictionary['customerReference'] = self.customer_reference
        if self.recurring is not None:
            dictionary['recurring'] = self.recurring.to_dictionary()
        if self.recurring_payment_sequence_indicator is not None:
            dictionary['recurringPaymentSequenceIndicator'] = self.recurring_payment_sequence_indicator
        if self.requires_approval is not None:
            dictionary['requiresApproval'] = self.requires_approval
        if self.skip_authentication is not None:
            dictionary['skipAuthentication'] = self.skip_authentication
        if self.skip_fraud_service is not None:
            dictionary['skipFraudService'] = self.skip_fraud_service
        if self.token is not None:
            dictionary['token'] = self.token
        if self.tokenize is not None:
            dictionary['tokenize'] = self.tokenize
        if self.transaction_channel is not None:
            dictionary['transactionChannel'] = self.transaction_channel
        if self.unscheduled_card_on_file_indicator is not None:
            dictionary['unscheduledCardOnFileIndicator'] = self.unscheduled_card_on_file_indicator
        if self.unscheduled_card_on_file_requestor is not None:
            dictionary['unscheduledCardOnFileRequestor'] = self.unscheduled_card_on_file_requestor
        if self.unscheduled_card_on_file_sequence_indicator is not None:
            dictionary['unscheduledCardOnFileSequenceIndicator'] = self.unscheduled_card_on_file_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractCardPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'recurring' in dictionary:
            if not isinstance(dictionary['recurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurring']))
            value = CardRecurrenceDetails()
            self.recurring = value.from_dictionary(dictionary['recurring'])
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
        if 'unscheduledCardOnFileSequenceIndicator' in dictionary:
            self.unscheduled_card_on_file_sequence_indicator = dictionary['unscheduledCardOnFileSequenceIndicator']
        return self
