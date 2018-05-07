# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput


class CardPaymentMethodSpecificInputBase(AbstractPaymentMethodSpecificInput):

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
        | Determines the type of the authorization that will be used. Allowed values:
        
        * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days.
        * PRE_AUTHORIZATION - The payment creation results in a pre-authorization that is ready for capture. Pre-authortizations can be reversed and can be captured within 30 days. The capture amount can be lower than the authorized amount.
        
        | Only used with some acquirers, ingnored for acquirers that don't support this. In case the acquirer doesn't allow this to be specified the authorizationMode is 'unspecified', which behaves similar to a final authorization.
        
        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value):
        self.__authorization_mode = value

    @property
    def customer_reference(self):
        """
        | Reference of the consumer for the payment (purchase order #, etc.) Only used with some acquirers.
        
        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value):
        self.__customer_reference = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        * first = This transaction is the first of a series of recurring transactions
        * recurring = This transaction is a subsequent transaction in a series of recurring transactions
        
        | Note: This field will default to first when isRecurring is set to true.
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
        * true = the payment requires approval before the funds will be captured
        * false = the payment does not require approval, and the funds will be captured automatically
        
        | If true, payments with status PENDING_APPROVAL can be captured with the Capture payment <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/approve.html> API
        
        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value):
        self.__requires_approval = value

    @property
    def skip_authentication(self):
        """
        * true = 3D Secure Authentication will be skipped for this transaction. This setting should be used when isRecurring is set to true and recurringPaymentSequenceIndicator is set to recurring.
        * false = 3D Secure Authentication will not be skipped for this transaction.
        
        | Note: This is only possible if your account in our system is setup for 3D Secure authentication and if your configuration in our system allows you to override it per transaction.
        
        Type: bool
        """
        return self.__skip_authentication

    @skip_authentication.setter
    def skip_authentication(self, value):
        self.__skip_authentication = value

    @property
    def skip_fraud_service(self):
        """
        * true = Fraud scoring will be skipped for this transaction
        * false = Fraud scoring will not be skipped for this transaction
        
        | Note: This is only possible if your account in our system is setup for Fraud scoring and if your configuration in our system allows you to override it per transaction.
        
        Type: bool
        """
        return self.__skip_fraud_service

    @skip_fraud_service.setter
    def skip_fraud_service(self, value):
        self.__skip_fraud_service = value

    @property
    def token(self):
        """
        | ID of the token that holds previously stored card data
        
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

    @property
    def transaction_channel(self):
        """
        | Indicates the channel via which the payment is created. Allowed values:
        
        * ECOMMERCE - The transaction is a regular E-Commerce transaction.
        * MOTO - The transaction is a Mail Order/Telephone Order.
        
        Type: str
        """
        return self.__transaction_channel

    @transaction_channel.setter
    def transaction_channel(self, value):
        self.__transaction_channel = value

    @property
    def unscheduled_card_on_file_indicator(self):
        """
        * first = This transaction is the first of a series of unscheduled recurring transactions
        * subsequent = This transaction is a subsequent transaction in a series of unscheduled recurring transactions
        
        
        | Note: this field is not allowed if isRecurring is true.
        
        Type: str
        """
        return self.__unscheduled_card_on_file_indicator

    @unscheduled_card_on_file_indicator.setter
    def unscheduled_card_on_file_indicator(self, value):
        self.__unscheduled_card_on_file_indicator = value

    @property
    def unscheduled_card_on_file_requestor(self):
        """
        | Indicates which party initiated the unscheduled recurring transaction. Allowed values:
        
        * merchantInitiated - Merchant Initiated Transaction.
        * cardholderInitiated - Cardholder Initiated Transaction.
        
        
        | Note: this field is not allowed if isRecurring is true.
        
        Type: str
        """
        return self.__unscheduled_card_on_file_requestor

    @unscheduled_card_on_file_requestor.setter
    def unscheduled_card_on_file_requestor(self, value):
        self.__unscheduled_card_on_file_requestor = value

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
        self._add_to_dictionary(dictionary, 'transactionChannel', self.transaction_channel)
        self._add_to_dictionary(dictionary, 'unscheduledCardOnFileIndicator', self.unscheduled_card_on_file_indicator)
        self._add_to_dictionary(dictionary, 'unscheduledCardOnFileRequestor', self.unscheduled_card_on_file_requestor)
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
        if 'transactionChannel' in dictionary:
            self.transaction_channel = dictionary['transactionChannel']
        if 'unscheduledCardOnFileIndicator' in dictionary:
            self.unscheduled_card_on_file_indicator = dictionary['unscheduledCardOnFileIndicator']
        if 'unscheduledCardOnFileRequestor' in dictionary:
            self.unscheduled_card_on_file_requestor = dictionary['unscheduledCardOnFileRequestor']
        return self
