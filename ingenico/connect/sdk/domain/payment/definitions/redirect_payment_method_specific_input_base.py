# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class RedirectPaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):

    __expiration_period = None
    __recurring_payment_sequence_indicator = None
    __requires_approval = None
    __token = None
    __tokenize = None

    @property
    def expiration_period(self):
        """
        | This sets the maximum amount of minutes a consumer has to complete the payment at the bank. After this period has expired it is impossible for the consumer to make a payment and in case no payment has been made the transaction will be marked as unsuccessful and expired by the bank. Setting the expirationPeriod is convenient if you want to maximise the time a consumer has to complete the payment. Please note that it is normal for a consumer to take up to 5 minutes to complete a payment. Setting this value below 10 minutes is not advised.
        | You can set this value in minutes with a maximum value of 60 minutes. If no input is provided the default value of 60 is used for the transaction.
        | This value can be set for the following payment products
        
        * 809 - iDeal
        * 402 - e-Przelewy
        
        Type: int
        """
        return self.__expiration_period

    @expiration_period.setter
    def expiration_period(self, value):
        self.__expiration_period = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        * first = This transaction is the first of a series of recurring transactions
        * recurring = This transaction is a subsequent transaction in a series of recurring transactions
        
        | Note: Will default to first when isRecurring is set to true, with the following exception that it is set to recurring when the consumer is making the payment using a PayPal token.
        | Note: For any first of a recurring the system will automatically create a token as you will need to use a token for any subsequent recurring transactions. In case a token already exists this is indicated in the response with a value of False for the isNewToken property in the response.
        
        Type: str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value):
        self.__recurring_payment_sequence_indicator = value

    @property
    def requires_approval(self):
        """
        * true = the payment requires approval before the funds will be captured using the Capture payment <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/approve.html> API
        * false = the payment does not require approval, and the funds will be captured automatically
        
        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value):
        self.__requires_approval = value

    @property
    def token(self):
        """
        | ID of the token
        
        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    @property
    def tokenize(self):
        """
        | Indicates if this transaction should be tokenized
        
        * true - Tokenize the transaction. Note that a payment on the GlobalCollect platform that results in a status REDIRECTED cannot be tokenized in this way. In this case, use the 'Create a token from payment' <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/tokenize.html> functionality after your customer succesfully completes the redirection.
        * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.
        
        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value):
        self.__tokenize = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificInputBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'expirationPeriod', self.expiration_period)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'requiresApproval', self.requires_approval)
        self._add_to_dictionary(dictionary, 'token', self.token)
        self._add_to_dictionary(dictionary, 'tokenize', self.tokenize)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
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
