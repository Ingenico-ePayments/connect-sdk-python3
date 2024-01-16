# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.hostedcheckout.definitions.mobile_payment_product302_specific_input_hosted_checkout import MobilePaymentProduct302SpecificInputHostedCheckout
from ingenico.connect.sdk.domain.hostedcheckout.definitions.mobile_payment_product320_specific_input_hosted_checkout import MobilePaymentProduct320SpecificInputHostedCheckout


class MobilePaymentMethodSpecificInputHostedCheckout(AbstractPaymentMethodSpecificInput):

    __authorization_mode = None
    __customer_reference = None
    __payment_product302_specific_input = None
    __payment_product320_specific_input = None
    __requires_approval = None
    __skip_fraud_service = None

    @property
    def authorization_mode(self):
        """
        | Determines the type of the authorization that will be used. Allowed values:
        
        * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days.
        * PRE_AUTHORIZATION - The payment creation results in a pre-authorization that is ready for capture. Pre-authortizations can be reversed and can be captured within 30 days. The capture amount can be lower than the authorized amount.
        * SALE - The payment creation results in an authorization that is already captured at the moment of approval.
        
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
        | Reference of the customer for the payment (purchase order #, etc.). Only used with some acquirers.
        
        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value):
        self.__customer_reference = value

    @property
    def payment_product302_specific_input(self):
        """
        | Object containing information specific to Apple Pay
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.mobile_payment_product302_specific_input_hosted_checkout.MobilePaymentProduct302SpecificInputHostedCheckout`
        """
        return self.__payment_product302_specific_input

    @payment_product302_specific_input.setter
    def payment_product302_specific_input(self, value):
        self.__payment_product302_specific_input = value

    @property
    def payment_product320_specific_input(self):
        """
        | Object containing information specific to Google Pay (paymentProductId 320)
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.mobile_payment_product320_specific_input_hosted_checkout.MobilePaymentProduct320SpecificInputHostedCheckout`
        """
        return self.__payment_product320_specific_input

    @payment_product320_specific_input.setter
    def payment_product320_specific_input(self, value):
        self.__payment_product320_specific_input = value

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

    def to_dictionary(self):
        dictionary = super(MobilePaymentMethodSpecificInputHostedCheckout, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.customer_reference is not None:
            dictionary['customerReference'] = self.customer_reference
        if self.payment_product302_specific_input is not None:
            dictionary['paymentProduct302SpecificInput'] = self.payment_product302_specific_input.to_dictionary()
        if self.payment_product320_specific_input is not None:
            dictionary['paymentProduct320SpecificInput'] = self.payment_product320_specific_input.to_dictionary()
        if self.requires_approval is not None:
            dictionary['requiresApproval'] = self.requires_approval
        if self.skip_fraud_service is not None:
            dictionary['skipFraudService'] = self.skip_fraud_service
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentMethodSpecificInputHostedCheckout, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'paymentProduct302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct302SpecificInput']))
            value = MobilePaymentProduct302SpecificInputHostedCheckout()
            self.payment_product302_specific_input = value.from_dictionary(dictionary['paymentProduct302SpecificInput'])
        if 'paymentProduct320SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificInput']))
            value = MobilePaymentProduct320SpecificInputHostedCheckout()
            self.payment_product320_specific_input = value.from_dictionary(dictionary['paymentProduct320SpecificInput'])
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        if 'skipFraudService' in dictionary:
            self.skip_fraud_service = dictionary['skipFraudService']
        return self
