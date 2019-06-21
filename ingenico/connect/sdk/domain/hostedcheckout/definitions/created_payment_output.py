# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.hostedcheckout.definitions.displayed_data import DisplayedData
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment
from ingenico.connect.sdk.domain.payment.definitions.payment_creation_references import PaymentCreationReferences


class CreatedPaymentOutput(DataObject):
    """
    | This object is used when a payment was created during a HostedCheckout. It is part of the response of a GET HostedCheckout object and contains the details of the created payment object.
    """

    __displayed_data = None
    __payment = None
    __payment_creation_references = None
    __payment_status_category = None
    __tokenization_succeeded = None
    __tokens = None

    @property
    def displayed_data(self):
        """
        | Object that contains the action, including the needed data, that you should perform next, like showing instruction, showing the transaction results or redirect to a third party to complete the payment
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.displayed_data.DisplayedData`
        """
        return self.__displayed_data

    @displayed_data.setter
    def displayed_data(self, value):
        self.__displayed_data = value

    @property
    def payment(self):
        """
        | Object that holds the payment data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment.Payment`
        """
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    @property
    def payment_creation_references(self):
        """
        | Object containing the created references
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment_creation_references.PaymentCreationReferences`
        """
        return self.__payment_creation_references

    @payment_creation_references.setter
    def payment_creation_references(self, value):
        self.__payment_creation_references = value

    @property
    def payment_status_category(self):
        """
        | Highlevel indication of the payment status with the following possible values:
        
        * REJECTED - The payment has been rejected or is in such a state that it will never become successful. This category groups the following statuses:
        
        * CREATED
        * REJECTED
        * REJECTED CAPTURE
        * REJECTED REFUND
        * REJECTED PAYOUT
        * CANCELLED
        
        
        * SUCCESSFUL - The payment was not (yet) rejected. Use the payment statuses to determine if it was completed, see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html>. This category groups the following statuses:
        
        * PENDING PAYMENT
        * ACCOUNT VERIFIED
        * PENDING FRAUD APPROVAL
        * PENDING APPROVAL
        * AUTHORIZATION REQUESTED
        * CAPTURE REQUESTED
        * REFUND REQUESTED
        * PAYOUT REQUESTED
        * CAPTURED
        * PAID
        * ACCOUNT CREDITED
        * REVERSED
        * CHARGEBACK_NOTIFICATION
        * CHARGEBACKED
        * REFUNDED
        
        
        * STATUS_UNKNOWN - The status of the payment is unknown at this moment. This category groups the following statuses:
        
        * REDIRECTED
        
        
        
        
        | Please see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html> for a full overview of possible values.
        
        Type: str
        
        Deprecated; Use Payment.statusOutput.statusCategory instead
        """
        return self.__payment_status_category

    @payment_status_category.setter
    def payment_status_category(self, value):
        self.__payment_status_category = value

    @property
    def tokenization_succeeded(self):
        """
        | If the payment was attempted to be tokenized, indicates if tokenization was successful or not.
        
        Type: bool
        """
        return self.__tokenization_succeeded

    @tokenization_succeeded.setter
    def tokenization_succeeded(self, value):
        self.__tokenization_succeeded = value

    @property
    def tokens(self):
        """
        | This property contains the tokens that are associated with the hosted checkout session/customer. You can use the tokens listed in this list for a future checkout of the same customer.
        
        Type: str
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value):
        self.__tokens = value

    def to_dictionary(self):
        dictionary = super(CreatedPaymentOutput, self).to_dictionary()
        if self.displayed_data is not None:
            dictionary['displayedData'] = self.displayed_data.to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        if self.payment_creation_references is not None:
            dictionary['paymentCreationReferences'] = self.payment_creation_references.to_dictionary()
        if self.payment_status_category is not None:
            dictionary['paymentStatusCategory'] = self.payment_status_category
        if self.tokenization_succeeded is not None:
            dictionary['tokenizationSucceeded'] = self.tokenization_succeeded
        if self.tokens is not None:
            dictionary['tokens'] = self.tokens
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatedPaymentOutput, self).from_dictionary(dictionary)
        if 'displayedData' in dictionary:
            if not isinstance(dictionary['displayedData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayedData']))
            value = DisplayedData()
            self.displayed_data = value.from_dictionary(dictionary['displayedData'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentCreationReferences' in dictionary:
            if not isinstance(dictionary['paymentCreationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentCreationReferences']))
            value = PaymentCreationReferences()
            self.payment_creation_references = value.from_dictionary(dictionary['paymentCreationReferences'])
        if 'paymentStatusCategory' in dictionary:
            self.payment_status_category = dictionary['paymentStatusCategory']
        if 'tokenizationSucceeded' in dictionary:
            self.tokenization_succeeded = dictionary['tokenizationSucceeded']
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        return self
