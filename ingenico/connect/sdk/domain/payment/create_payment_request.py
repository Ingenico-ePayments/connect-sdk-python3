# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.fraud_fields import FraudFields
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input import BankTransferPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_input import CashPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_method_specific_input import EInvoicePaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.invoice_payment_method_specific_input import InvoicePaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.mobile_payment_method_specific_input import MobilePaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_method_specific_input import NonSepaDirectDebitPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_input import SepaDirectDebitPaymentMethodSpecificInput


class CreatePaymentRequest(DataObject):

    __bank_transfer_payment_method_specific_input = None
    __card_payment_method_specific_input = None
    __cash_payment_method_specific_input = None
    __direct_debit_payment_method_specific_input = None
    __e_invoice_payment_method_specific_input = None
    __encrypted_customer_input = None
    __fraud_fields = None
    __invoice_payment_method_specific_input = None
    __mobile_payment_method_specific_input = None
    __order = None
    __redirect_payment_method_specific_input = None
    __sepa_direct_debit_payment_method_specific_input = None

    @property
    def bank_transfer_payment_method_specific_input(self):
        """
        | Object containing the specific input details for bank transfer payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input.BankTransferPaymentMethodSpecificInput`
        """
        return self.__bank_transfer_payment_method_specific_input

    @bank_transfer_payment_method_specific_input.setter
    def bank_transfer_payment_method_specific_input(self, value):
        self.__bank_transfer_payment_method_specific_input = value

    @property
    def card_payment_method_specific_input(self):
        """
        | Object containing the specific input details for card payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input.CardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value):
        self.__card_payment_method_specific_input = value

    @property
    def cash_payment_method_specific_input(self):
        """
        | Object containing the specific input details for cash payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_input.CashPaymentMethodSpecificInput`
        """
        return self.__cash_payment_method_specific_input

    @cash_payment_method_specific_input.setter
    def cash_payment_method_specific_input(self, value):
        self.__cash_payment_method_specific_input = value

    @property
    def direct_debit_payment_method_specific_input(self):
        """
        | Object containing the specific input details for direct debit payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_method_specific_input.NonSepaDirectDebitPaymentMethodSpecificInput`
        """
        return self.__direct_debit_payment_method_specific_input

    @direct_debit_payment_method_specific_input.setter
    def direct_debit_payment_method_specific_input(self, value):
        self.__direct_debit_payment_method_specific_input = value

    @property
    def e_invoice_payment_method_specific_input(self):
        """
        | Object containing the specific input details for e-invoice payments.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.e_invoice_payment_method_specific_input.EInvoicePaymentMethodSpecificInput`
        """
        return self.__e_invoice_payment_method_specific_input

    @e_invoice_payment_method_specific_input.setter
    def e_invoice_payment_method_specific_input(self, value):
        self.__e_invoice_payment_method_specific_input = value

    @property
    def encrypted_customer_input(self):
        """
        | Data that was encrypted client side containing all consumer entered data elements like card data.
        | Note: Because this data can only be submitted once to our system and contains encrypted card data you should not store it. As the data was captured within the context of a client session you also need to submit it to us before the session has expired.
        
        Type: str
        """
        return self.__encrypted_customer_input

    @encrypted_customer_input.setter
    def encrypted_customer_input(self, value):
        self.__encrypted_customer_input = value

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
    def invoice_payment_method_specific_input(self):
        """
        | Object containing the specific input details for invoice payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.invoice_payment_method_specific_input.InvoicePaymentMethodSpecificInput`
        """
        return self.__invoice_payment_method_specific_input

    @invoice_payment_method_specific_input.setter
    def invoice_payment_method_specific_input(self, value):
        self.__invoice_payment_method_specific_input = value

    @property
    def mobile_payment_method_specific_input(self):
        """
        | Object containing the specific input details for mobile payments.
        
        | Mobile payments produce the required payment data in encrypted form.
        
        * For Apple Pay, the encrypted payment data can be found in field data of the PKPayment <https://developer.apple.com/documentation/passkit/pkpayment>.token.paymentData property.
        * For Google Pay, the encrypted payment data can be found in field paymentMethodData.tokenizationData.token of the PaymentData <https://developers.google.com/android/reference/com/google/android/gms/wallet/PaymentData>.toJson() result.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.mobile_payment_method_specific_input.MobilePaymentMethodSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value):
        self.__mobile_payment_method_specific_input = value

    @property
    def order(self):
        """
        | Order object containing order related data
        | Please note that this object is required to be able to submit the amount.
        
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
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input.RedirectPaymentMethodSpecificInput`
        """
        return self.__redirect_payment_method_specific_input

    @redirect_payment_method_specific_input.setter
    def redirect_payment_method_specific_input(self, value):
        self.__redirect_payment_method_specific_input = value

    @property
    def sepa_direct_debit_payment_method_specific_input(self):
        """
        | Object containing the specific input details for SEPA direct debit payments
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_input.SepaDirectDebitPaymentMethodSpecificInput`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value):
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreatePaymentRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankTransferPaymentMethodSpecificInput', self.bank_transfer_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificInput', self.card_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'cashPaymentMethodSpecificInput', self.cash_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'directDebitPaymentMethodSpecificInput', self.direct_debit_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'eInvoicePaymentMethodSpecificInput', self.e_invoice_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'encryptedCustomerInput', self.encrypted_customer_input)
        self._add_to_dictionary(dictionary, 'fraudFields', self.fraud_fields)
        self._add_to_dictionary(dictionary, 'invoicePaymentMethodSpecificInput', self.invoice_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'mobilePaymentMethodSpecificInput', self.mobile_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'order', self.order)
        self._add_to_dictionary(dictionary, 'redirectPaymentMethodSpecificInput', self.redirect_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'sepaDirectDebitPaymentMethodSpecificInput', self.sepa_direct_debit_payment_method_specific_input)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentRequest, self).from_dictionary(dictionary)
        if 'bankTransferPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['bankTransferPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankTransferPaymentMethodSpecificInput']))
            value = BankTransferPaymentMethodSpecificInput()
            self.bank_transfer_payment_method_specific_input = value.from_dictionary(dictionary['bankTransferPaymentMethodSpecificInput'])
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'cashPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cashPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cashPaymentMethodSpecificInput']))
            value = CashPaymentMethodSpecificInput()
            self.cash_payment_method_specific_input = value.from_dictionary(dictionary['cashPaymentMethodSpecificInput'])
        if 'directDebitPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['directDebitPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['directDebitPaymentMethodSpecificInput']))
            value = NonSepaDirectDebitPaymentMethodSpecificInput()
            self.direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['directDebitPaymentMethodSpecificInput'])
        if 'eInvoicePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['eInvoicePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eInvoicePaymentMethodSpecificInput']))
            value = EInvoicePaymentMethodSpecificInput()
            self.e_invoice_payment_method_specific_input = value.from_dictionary(dictionary['eInvoicePaymentMethodSpecificInput'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
        if 'fraudFields' in dictionary:
            if not isinstance(dictionary['fraudFields'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudFields']))
            value = FraudFields()
            self.fraud_fields = value.from_dictionary(dictionary['fraudFields'])
        if 'invoicePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['invoicePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['invoicePaymentMethodSpecificInput']))
            value = InvoicePaymentMethodSpecificInput()
            self.invoice_payment_method_specific_input = value.from_dictionary(dictionary['invoicePaymentMethodSpecificInput'])
        if 'mobilePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificInput']))
            value = MobilePaymentMethodSpecificInput()
            self.mobile_payment_method_specific_input = value.from_dictionary(dictionary['mobilePaymentMethodSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        if 'redirectPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificInput']))
            value = RedirectPaymentMethodSpecificInput()
            self.redirect_payment_method_specific_input = value.from_dictionary(dictionary['redirectPaymentMethodSpecificInput'])
        if 'sepaDirectDebitPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificInput']))
            value = SepaDirectDebitPaymentMethodSpecificInput()
            self.sepa_direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificInput'])
        return self
