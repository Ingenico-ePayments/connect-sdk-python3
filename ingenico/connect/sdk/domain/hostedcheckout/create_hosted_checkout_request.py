#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.fraud_fields import FraudFields
from ingenico.connect.sdk.domain.hostedcheckout.definitions.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input_base import BankTransferPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_input_base import CashPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input_base import RedirectPaymentMethodSpecificInputBase


class CreateHostedCheckoutRequest(DataObject):
    """
    Class CreateHostedCheckoutRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreateHostedCheckoutRequest
    """

    __bank_transfer_payment_method_specific_input = None
    __card_payment_method_specific_input = None
    __cash_payment_method_specific_input = None
    __fraud_fields = None
    __hosted_checkout_specific_input = None
    __order = None
    __redirect_payment_method_specific_input = None

    @property
    def bank_transfer_payment_method_specific_input(self):
        """
        :class:`BankTransferPaymentMethodSpecificInputBase`
        """
        return self.__bank_transfer_payment_method_specific_input

    @bank_transfer_payment_method_specific_input.setter
    def bank_transfer_payment_method_specific_input(self, value):
        self.__bank_transfer_payment_method_specific_input = value

    @property
    def card_payment_method_specific_input(self):
        """
        :class:`CardPaymentMethodSpecificInputBase`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value):
        self.__card_payment_method_specific_input = value

    @property
    def cash_payment_method_specific_input(self):
        """
        :class:`CashPaymentMethodSpecificInputBase`
        """
        return self.__cash_payment_method_specific_input

    @cash_payment_method_specific_input.setter
    def cash_payment_method_specific_input(self, value):
        self.__cash_payment_method_specific_input = value

    @property
    def fraud_fields(self):
        """
        :class:`FraudFields`
        """
        return self.__fraud_fields

    @fraud_fields.setter
    def fraud_fields(self, value):
        self.__fraud_fields = value

    @property
    def hosted_checkout_specific_input(self):
        """
        :class:`HostedCheckoutSpecificInput`
        """
        return self.__hosted_checkout_specific_input

    @hosted_checkout_specific_input.setter
    def hosted_checkout_specific_input(self, value):
        self.__hosted_checkout_specific_input = value

    @property
    def order(self):
        """
        :class:`Order`
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def redirect_payment_method_specific_input(self):
        """
        :class:`RedirectPaymentMethodSpecificInputBase`
        """
        return self.__redirect_payment_method_specific_input

    @redirect_payment_method_specific_input.setter
    def redirect_payment_method_specific_input(self, value):
        self.__redirect_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreateHostedCheckoutRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankTransferPaymentMethodSpecificInput', self.bank_transfer_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificInput', self.card_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'cashPaymentMethodSpecificInput', self.cash_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'fraudFields', self.fraud_fields)
        self._add_to_dictionary(dictionary, 'hostedCheckoutSpecificInput', self.hosted_checkout_specific_input)
        self._add_to_dictionary(dictionary, 'order', self.order)
        self._add_to_dictionary(dictionary, 'redirectPaymentMethodSpecificInput', self.redirect_payment_method_specific_input)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedCheckoutRequest, self).from_dictionary(dictionary)
        if 'bankTransferPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['bankTransferPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankTransferPaymentMethodSpecificInput']))
            value = BankTransferPaymentMethodSpecificInputBase()
            self.bank_transfer_payment_method_specific_input = value.from_dictionary(dictionary['bankTransferPaymentMethodSpecificInput'])
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputBase()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'cashPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cashPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cashPaymentMethodSpecificInput']))
            value = CashPaymentMethodSpecificInputBase()
            self.cash_payment_method_specific_input = value.from_dictionary(dictionary['cashPaymentMethodSpecificInput'])
        if 'fraudFields' in dictionary:
            if not isinstance(dictionary['fraudFields'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudFields']))
            value = FraudFields()
            self.fraud_fields = value.from_dictionary(dictionary['fraudFields'])
        if 'hostedCheckoutSpecificInput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificInput']))
            value = HostedCheckoutSpecificInput()
            self.hosted_checkout_specific_input = value.from_dictionary(dictionary['hostedCheckoutSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        if 'redirectPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificInput']))
            value = RedirectPaymentMethodSpecificInputBase()
            self.redirect_payment_method_specific_input = value.from_dictionary(dictionary['redirectPaymentMethodSpecificInput'])
        return self
