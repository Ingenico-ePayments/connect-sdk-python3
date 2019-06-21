# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.fraud_fields import FraudFields
from ingenico.connect.sdk.domain.hostedcheckout.definitions.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from ingenico.connect.sdk.domain.hostedcheckout.definitions.mobile_payment_method_specific_input_hosted_checkout import MobilePaymentMethodSpecificInputHostedCheckout
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input_base import BankTransferPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_input_base import CashPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_method_specific_input_base import EInvoicePaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.merchant import Merchant
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input_base import RedirectPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_input_base import SepaDirectDebitPaymentMethodSpecificInputBase


class CreateHostedCheckoutRequest(DataObject):

    __bank_transfer_payment_method_specific_input = None
    __card_payment_method_specific_input = None
    __cash_payment_method_specific_input = None
    __e_invoice_payment_method_specific_input = None
    __fraud_fields = None
    __hosted_checkout_specific_input = None
    __merchant = None
    __mobile_payment_method_specific_input = None
    __order = None
    __redirect_payment_method_specific_input = None
    __sepa_direct_debit_payment_method_specific_input = None

    @property
    def bank_transfer_payment_method_specific_input(self):
        """
        | Object containing the specific input details for bank transfer payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input_base.BankTransferPaymentMethodSpecificInputBase`
        """
        return self.__bank_transfer_payment_method_specific_input

    @bank_transfer_payment_method_specific_input.setter
    def bank_transfer_payment_method_specific_input(self, value):
        self.__bank_transfer_payment_method_specific_input = value

    @property
    def card_payment_method_specific_input(self):
        """
        | Object containing the specific input details for card payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input_base.CardPaymentMethodSpecificInputBase`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value):
        self.__card_payment_method_specific_input = value

    @property
    def cash_payment_method_specific_input(self):
        """
        | Object containing the specific input details for cash payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_input_base.CashPaymentMethodSpecificInputBase`
        """
        return self.__cash_payment_method_specific_input

    @cash_payment_method_specific_input.setter
    def cash_payment_method_specific_input(self, value):
        self.__cash_payment_method_specific_input = value

    @property
    def e_invoice_payment_method_specific_input(self):
        """
        | Object containing the specific input details for eInvoice payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_method_specific_input_base.EInvoicePaymentMethodSpecificInputBase`
        """
        return self.__e_invoice_payment_method_specific_input

    @e_invoice_payment_method_specific_input.setter
    def e_invoice_payment_method_specific_input(self, value):
        self.__e_invoice_payment_method_specific_input = value

    @property
    def fraud_fields(self):
        """
        | Object containing additional data that will be used to assess the risk of fraud
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.fraud_fields.FraudFields`
        """
        return self.__fraud_fields

    @fraud_fields.setter
    def fraud_fields(self, value):
        self.__fraud_fields = value

    @property
    def hosted_checkout_specific_input(self):
        """
        | Object containing hosted checkout specific data
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.hosted_checkout_specific_input.HostedCheckoutSpecificInput`
        """
        return self.__hosted_checkout_specific_input

    @hosted_checkout_specific_input.setter
    def hosted_checkout_specific_input(self, value):
        self.__hosted_checkout_specific_input = value

    @property
    def merchant(self):
        """
        | Object containing information on you, the merchant
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.merchant.Merchant`
        """
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value

    @property
    def mobile_payment_method_specific_input(self):
        """
        | Object containing reference data for Google Pay.
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.mobile_payment_method_specific_input_hosted_checkout.MobilePaymentMethodSpecificInputHostedCheckout`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value):
        self.__mobile_payment_method_specific_input = value

    @property
    def order(self):
        """
        | Order object containing order related data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def redirect_payment_method_specific_input(self):
        """
        | Object containing the specific input details for payments that involve redirects to 3rd parties to complete, like iDeal and PayPal
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input_base.RedirectPaymentMethodSpecificInputBase`
        """
        return self.__redirect_payment_method_specific_input

    @redirect_payment_method_specific_input.setter
    def redirect_payment_method_specific_input(self, value):
        self.__redirect_payment_method_specific_input = value

    @property
    def sepa_direct_debit_payment_method_specific_input(self):
        """
        | Object containing the specific input details for SEPA direct debit payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_input_base.SepaDirectDebitPaymentMethodSpecificInputBase`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value):
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreateHostedCheckoutRequest, self).to_dictionary()
        if self.bank_transfer_payment_method_specific_input is not None:
            dictionary['bankTransferPaymentMethodSpecificInput'] = self.bank_transfer_payment_method_specific_input.to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.cash_payment_method_specific_input is not None:
            dictionary['cashPaymentMethodSpecificInput'] = self.cash_payment_method_specific_input.to_dictionary()
        if self.e_invoice_payment_method_specific_input is not None:
            dictionary['eInvoicePaymentMethodSpecificInput'] = self.e_invoice_payment_method_specific_input.to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_checkout_specific_input is not None:
            dictionary['hostedCheckoutSpecificInput'] = self.hosted_checkout_specific_input.to_dictionary()
        if self.merchant is not None:
            dictionary['merchant'] = self.merchant.to_dictionary()
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
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
        if 'eInvoicePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['eInvoicePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eInvoicePaymentMethodSpecificInput']))
            value = EInvoicePaymentMethodSpecificInputBase()
            self.e_invoice_payment_method_specific_input = value.from_dictionary(dictionary['eInvoicePaymentMethodSpecificInput'])
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
        if 'merchant' in dictionary:
            if not isinstance(dictionary['merchant'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchant']))
            value = Merchant()
            self.merchant = value.from_dictionary(dictionary['merchant'])
        if 'mobilePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificInput']))
            value = MobilePaymentMethodSpecificInputHostedCheckout()
            self.mobile_payment_method_specific_input = value.from_dictionary(dictionary['mobilePaymentMethodSpecificInput'])
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
        if 'sepaDirectDebitPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificInput']))
            value = SepaDirectDebitPaymentMethodSpecificInputBase()
            self.sepa_direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificInput'])
        return self
