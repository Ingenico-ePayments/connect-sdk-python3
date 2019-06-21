# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_order_status import AbstractOrderStatus
from ingenico.connect.sdk.domain.payment.definitions.hosted_checkout_specific_output import HostedCheckoutSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment_output import PaymentOutput
from ingenico.connect.sdk.domain.payment.definitions.payment_status_output import PaymentStatusOutput


class Payment(AbstractOrderStatus):

    __hosted_checkout_specific_output = None
    __payment_output = None
    __status = None
    __status_output = None

    @property
    def hosted_checkout_specific_output(self):
        """
        | Hosted Checkout specific information. Populated if the payment was created on the GlobalCollect platform through a Hosted Checkout.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.hosted_checkout_specific_output.HostedCheckoutSpecificOutput`
        """
        return self.__hosted_checkout_specific_output

    @hosted_checkout_specific_output.setter
    def hosted_checkout_specific_output(self, value):
        self.__hosted_checkout_specific_output = value

    @property
    def payment_output(self):
        """
        | Object containing payment details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment_output.PaymentOutput`
        """
        return self.__payment_output

    @payment_output.setter
    def payment_output(self, value):
        self.__payment_output = value

    @property
    def status(self):
        """
        | Current high-level status of the payment in a human-readable form. Possible values are :
        
        * ACCOUNT_VERIFIED - The account has been verified using a validation services like 0$ auth
        * CREATED - The transaction has been created. This is the initial state once a new payment is created.
        * REDIRECTED - The customer has been redirected to a 3rd party to complete the authentication/payment
        * PENDING_PAYMENT - Instructions have been provided and we are now waiting for the money to come in
        * PENDING_FRAUD_APPROVAL - The transaction has been marked for manual review after an automatic fraud screening
        * PENDING_APPROVAL - The transaction is awaiting approval from you to proceed with the capturing of the funds
        * PENDING_COMPLETION - The transaction needs to be completed.
        * PENDING_CAPTURE - The transaction is waiting for you to request one or more captures of the funds.
        * REJECTED - The transaction has been rejected
        * AUTHORIZATION_REQUESTED - we have requested an authorization against an asynchronous system and is awaiting its response
        * CAPTURE_REQUESTED - The transaction is in the queue to be captured
        * CAPTURED - The transaction has been captured and we have received online confirmation
        * PAID - We have matched the incoming funds to the transaction
        * CANCELLED - You have cancelled the transaction
        * REJECTED_CAPTURE - We or one of our downstream acquirers/providers have rejected the capture request
        * REVERSED - The transaction has been reversed
        * CHARGEBACK_NOTIFICATION - We have received a notification of chargeback and this status informs you that your account will be debited for a particular transaction
        * CHARGEBACKED - The transaction has been chargebacked
        * REFUNDED - The transaction has been refunded
        
        
        | Please see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html> for a full overview of possible values.
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def status_output(self):
        """
        | This object has the numeric representation of the current payment status, timestamp of last status change and performable action on the current payment resource.
        | In case of failed payments and negative scenarios, detailed error information is listed.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment_status_output.PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value):
        self.__status_output = value

    def to_dictionary(self):
        dictionary = super(Payment, self).to_dictionary()
        if self.hosted_checkout_specific_output is not None:
            dictionary['hostedCheckoutSpecificOutput'] = self.hosted_checkout_specific_output.to_dictionary()
        if self.payment_output is not None:
            dictionary['paymentOutput'] = self.payment_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(Payment, self).from_dictionary(dictionary)
        if 'hostedCheckoutSpecificOutput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificOutput']))
            value = HostedCheckoutSpecificOutput()
            self.hosted_checkout_specific_output = value.from_dictionary(dictionary['hostedCheckoutSpecificOutput'])
        if 'paymentOutput' in dictionary:
            if not isinstance(dictionary['paymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentOutput']))
            value = PaymentOutput()
            self.payment_output = value.from_dictionary(dictionary['paymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PaymentStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
