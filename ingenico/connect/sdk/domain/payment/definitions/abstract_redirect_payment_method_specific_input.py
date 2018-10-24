# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class AbstractRedirectPaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):

    __expiration_period = None
    __recurring_payment_sequence_indicator = None
    __requires_approval = None
    __token = None
    __tokenize = None

    @property
    def expiration_period(self):
        """
        Type: int
        """
        return self.__expiration_period

    @expiration_period.setter
    def expiration_period(self, value):
        self.__expiration_period = value

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

    def to_dictionary(self):
        dictionary = super(AbstractRedirectPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'expirationPeriod', self.expiration_period)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'requiresApproval', self.requires_approval)
        self._add_to_dictionary(dictionary, 'token', self.token)
        self._add_to_dictionary(dictionary, 'tokenize', self.tokenize)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractRedirectPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'expirationPeriod' in dictionary:
            self.expiration_period = dictionary['expirationPeriod']
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self
