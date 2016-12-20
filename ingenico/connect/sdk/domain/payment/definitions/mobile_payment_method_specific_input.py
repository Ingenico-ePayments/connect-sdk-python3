#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.decrypted_payment_data import DecryptedPaymentData
from ingenico.connect.sdk.domain.payment.definitions.mobile_payment_product320_specific_input import MobilePaymentProduct320SpecificInput


class MobilePaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):
    """
    Class MobilePaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MobilePaymentMethodSpecificInput
    """

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
        str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value):
        self.__authorization_mode = value

    @property
    def decrypted_payment_data(self):
        """
        :class:`DecryptedPaymentData`
        """
        return self.__decrypted_payment_data

    @decrypted_payment_data.setter
    def decrypted_payment_data(self, value):
        self.__decrypted_payment_data = value

    @property
    def encrypted_payment_data(self):
        """
        str
        """
        return self.__encrypted_payment_data

    @encrypted_payment_data.setter
    def encrypted_payment_data(self, value):
        self.__encrypted_payment_data = value

    @property
    def payment_product320_specific_input(self):
        """
        :class:`MobilePaymentProduct320SpecificInput`
        """
        return self.__payment_product320_specific_input

    @payment_product320_specific_input.setter
    def payment_product320_specific_input(self, value):
        self.__payment_product320_specific_input = value

    @property
    def requires_approval(self):
        """
        bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value):
        self.__requires_approval = value

    @property
    def skip_fraud_service(self):
        """
        bool
        """
        return self.__skip_fraud_service

    @skip_fraud_service.setter
    def skip_fraud_service(self, value):
        self.__skip_fraud_service = value

    @property
    def transaction_id(self):
        """
        str
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
