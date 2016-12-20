#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_card_payment_method_specific_output import ApprovePaymentCardPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_mobile_payment_method_specific_output import ApprovePaymentMobilePaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment


class PaymentApprovalResponse(DataObject):
    """
    Class PaymentApprovalResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentApprovalResponse
    """

    __card_payment_method_specific_output = None
    __mobile_payment_method_specific_output = None
    __payment = None
    __payment_method_specific_output = None

    @property
    def card_payment_method_specific_output(self):
        """
        :class:`ApprovePaymentCardPaymentMethodSpecificOutput`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value):
        self.__card_payment_method_specific_output = value

    @property
    def mobile_payment_method_specific_output(self):
        """
        :class:`ApprovePaymentMobilePaymentMethodSpecificOutput`
        """
        return self.__mobile_payment_method_specific_output

    @mobile_payment_method_specific_output.setter
    def mobile_payment_method_specific_output(self, value):
        self.__mobile_payment_method_specific_output = value

    @property
    def payment(self):
        """
        :class:`Payment`
        """
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    @property
    def payment_method_specific_output(self):
        """
        :class:`ApprovePaymentCardPaymentMethodSpecificOutput`
        
        Deprecated; Use cardPaymentMethodSpecificOutput instead
        """
        return self.__payment_method_specific_output

    @payment_method_specific_output.setter
    def payment_method_specific_output(self, value):
        self.__payment_method_specific_output = value

    def to_dictionary(self):
        dictionary = super(PaymentApprovalResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificOutput', self.card_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'mobilePaymentMethodSpecificOutput', self.mobile_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'payment', self.payment)
        self._add_to_dictionary(dictionary, 'paymentMethodSpecificOutput', self.payment_method_specific_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentApprovalResponse, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = ApprovePaymentCardPaymentMethodSpecificOutput()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'mobilePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificOutput']))
            value = ApprovePaymentMobilePaymentMethodSpecificOutput()
            self.mobile_payment_method_specific_output = value.from_dictionary(dictionary['mobilePaymentMethodSpecificOutput'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentMethodSpecificOutput']))
            value = ApprovePaymentCardPaymentMethodSpecificOutput()
            self.payment_method_specific_output = value.from_dictionary(dictionary['paymentMethodSpecificOutput'])
        return self
