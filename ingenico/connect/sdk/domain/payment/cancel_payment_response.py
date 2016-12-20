#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.cancel_payment_card_payment_method_specific_output import CancelPaymentCardPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.cancel_payment_mobile_payment_method_specific_output import CancelPaymentMobilePaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment


class CancelPaymentResponse(DataObject):
    """
    Class CancelPaymentResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CancelPaymentResponse
    """

    __card_payment_method_specific_output = None
    __mobile_payment_method_specific_output = None
    __payment = None

    @property
    def card_payment_method_specific_output(self):
        """
        :class:`CancelPaymentCardPaymentMethodSpecificOutput`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value):
        self.__card_payment_method_specific_output = value

    @property
    def mobile_payment_method_specific_output(self):
        """
        :class:`CancelPaymentMobilePaymentMethodSpecificOutput`
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

    def to_dictionary(self):
        dictionary = super(CancelPaymentResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificOutput', self.card_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'mobilePaymentMethodSpecificOutput', self.mobile_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'payment', self.payment)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CancelPaymentResponse, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = CancelPaymentCardPaymentMethodSpecificOutput()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'mobilePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificOutput']))
            value = CancelPaymentMobilePaymentMethodSpecificOutput()
            self.mobile_payment_method_specific_output = value.from_dictionary(dictionary['mobilePaymentMethodSpecificOutput'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self
