# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card_fraud_results import CardFraudResults
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.mobile_payment_data import MobilePaymentData
from ingenico.connect.sdk.domain.payment.definitions.three_d_secure_results import ThreeDSecureResults


class MobilePaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):

    __authorisation_code = None
    __fraud_results = None
    __network = None
    __payment_data = None
    __three_d_secure_results = None

    @property
    def authorisation_code(self):
        """
        | Card Authorization code as returned by the acquirer
        
        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value):
        self.__authorisation_code = value

    @property
    def fraud_results(self):
        """
        | Fraud results contained in the CardFraudResults object
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.card_fraud_results.CardFraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value):
        self.__fraud_results = value

    @property
    def network(self):
        """
        | The network that was used for the refund
        
        Type: str
        """
        return self.__network

    @network.setter
    def network(self, value):
        self.__network = value

    @property
    def payment_data(self):
        """
        | Object containing payment details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.mobile_payment_data.MobilePaymentData`
        """
        return self.__payment_data

    @payment_data.setter
    def payment_data(self, value):
        self.__payment_data = value

    @property
    def three_d_secure_results(self):
        """
        | 3D Secure results object
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.three_d_secure_results.ThreeDSecureResults`
        """
        return self.__three_d_secure_results

    @three_d_secure_results.setter
    def three_d_secure_results(self, value):
        self.__three_d_secure_results = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentMethodSpecificOutput, self).to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.network is not None:
            dictionary['network'] = self.network
        if self.payment_data is not None:
            dictionary['paymentData'] = self.payment_data.to_dictionary()
        if self.three_d_secure_results is not None:
            dictionary['threeDSecureResults'] = self.three_d_secure_results.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = CardFraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'network' in dictionary:
            self.network = dictionary['network']
        if 'paymentData' in dictionary:
            if not isinstance(dictionary['paymentData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentData']))
            value = MobilePaymentData()
            self.payment_data = value.from_dictionary(dictionary['paymentData'])
        if 'threeDSecureResults' in dictionary:
            if not isinstance(dictionary['threeDSecureResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureResults']))
            value = ThreeDSecureResults()
            self.three_d_secure_results = value.from_dictionary(dictionary['threeDSecureResults'])
        return self
