# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.decrypted_payment_data import DecryptedPaymentData
from ingenico.connect.sdk.domain.payment.definitions.mobile_payment_product320_specific_input import MobilePaymentProduct320SpecificInput


class MobilePaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):

    __authorization_mode = None
    __decrypted_payment_data = None
    __encrypted_payment_data = None
    __payment_product320_specific_input = None
    __requires_approval = None
    __skip_fraud_service = None
    __transaction_id = None

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
    def decrypted_payment_data(self):
        """
        | The payment data if you want to do the decryption of the vendor's encrypted payment data yourself.
        | Typically you'd use encryptedCustomerInput in the root of the create payment request to provide the payment data for mobile payment methods.Only when you do not do this you need to use either this field or encryptedPaymentData, depending on who should do the decryption of the vendor's encrypted payment data.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.decrypted_payment_data.DecryptedPaymentData`
        """
        return self.__decrypted_payment_data

    @decrypted_payment_data.setter
    def decrypted_payment_data(self, value):
        self.__decrypted_payment_data = value

    @property
    def encrypted_payment_data(self):
        """
        | The payment data if you want to let us do the decryption of the vendor's encrypted payment data.
        | Typically you'd use encryptedCustomerInput in the root of the create payment request to provide the payment data for mobile payment methods.Only when you do not do this you need to use either this field or decryptedPaymentData, depending on who should do the decryption of the vendor's encrypted payment data.This maps to the following field in the vendor's encrypted payment data:
        
        * Apple Pay: PKPayment.token.paymentData
        * Android Pay: FullWallet.paymentMethodToken.token
        
        Type: str
        """
        return self.__encrypted_payment_data

    @encrypted_payment_data.setter
    def encrypted_payment_data(self, value):
        self.__encrypted_payment_data = value

    @property
    def payment_product320_specific_input(self):
        """
        | Android Pay (payment product 320) specific details.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.mobile_payment_product320_specific_input.MobilePaymentProduct320SpecificInput`
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

    @property
    def transaction_id(self):
        """
        | The vendor's transaction id. This maps to the following field in the vendor's encrypted payment data:
        
        * Apple Pay: PKPayment.token.transactionIdentifier
        * Android Pay: FullWallet.googleTransactionId
        
        Type: str
        """
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self.__transaction_id = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'authorizationMode', self.authorization_mode)
        self._add_to_dictionary(dictionary, 'decryptedPaymentData', self.decrypted_payment_data)
        self._add_to_dictionary(dictionary, 'encryptedPaymentData', self.encrypted_payment_data)
        self._add_to_dictionary(dictionary, 'paymentProduct320SpecificInput', self.payment_product320_specific_input)
        self._add_to_dictionary(dictionary, 'requiresApproval', self.requires_approval)
        self._add_to_dictionary(dictionary, 'skipFraudService', self.skip_fraud_service)
        self._add_to_dictionary(dictionary, 'transactionId', self.transaction_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'decryptedPaymentData' in dictionary:
            if not isinstance(dictionary['decryptedPaymentData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['decryptedPaymentData']))
            value = DecryptedPaymentData()
            self.decrypted_payment_data = value.from_dictionary(dictionary['decryptedPaymentData'])
        if 'encryptedPaymentData' in dictionary:
            self.encrypted_payment_data = dictionary['encryptedPaymentData']
        if 'paymentProduct320SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificInput']))
            value = MobilePaymentProduct320SpecificInput()
            self.payment_product320_specific_input = value.from_dictionary(dictionary['paymentProduct320SpecificInput'])
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        if 'skipFraudService' in dictionary:
            self.skip_fraud_service = dictionary['skipFraudService']
        if 'transactionId' in dictionary:
            self.transaction_id = dictionary['transactionId']
        return self
