# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.order_output import OrderOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_bank_method_specific_output import RefundBankMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_card_method_specific_output import RefundCardMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_e_invoice_method_specific_output import RefundEInvoiceMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_e_wallet_method_specific_output import RefundEWalletMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_mobile_method_specific_output import RefundMobileMethodSpecificOutput


class RefundOutput(OrderOutput):

    __amount_paid = None
    __bank_refund_method_specific_output = None
    __card_refund_method_specific_output = None
    __e_invoice_refund_method_specific_output = None
    __e_wallet_refund_method_specific_output = None
    __mobile_refund_method_specific_output = None
    __payment_method = None

    @property
    def amount_paid(self):
        """
        | Amount paid
        
        Type: int
        """
        return self.__amount_paid

    @amount_paid.setter
    def amount_paid(self, value):
        self.__amount_paid = value

    @property
    def bank_refund_method_specific_output(self):
        """
        | Object containing specific bank refund details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.refund_bank_method_specific_output.RefundBankMethodSpecificOutput`
        """
        return self.__bank_refund_method_specific_output

    @bank_refund_method_specific_output.setter
    def bank_refund_method_specific_output(self, value):
        self.__bank_refund_method_specific_output = value

    @property
    def card_refund_method_specific_output(self):
        """
        | Object containing specific card refund details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.refund_card_method_specific_output.RefundCardMethodSpecificOutput`
        """
        return self.__card_refund_method_specific_output

    @card_refund_method_specific_output.setter
    def card_refund_method_specific_output(self, value):
        self.__card_refund_method_specific_output = value

    @property
    def e_invoice_refund_method_specific_output(self):
        """
        | Object containing specific e-invoice refund details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.refund_e_invoice_method_specific_output.RefundEInvoiceMethodSpecificOutput`
        """
        return self.__e_invoice_refund_method_specific_output

    @e_invoice_refund_method_specific_output.setter
    def e_invoice_refund_method_specific_output(self, value):
        self.__e_invoice_refund_method_specific_output = value

    @property
    def e_wallet_refund_method_specific_output(self):
        """
        | Object containing specific eWallet refund details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.refund_e_wallet_method_specific_output.RefundEWalletMethodSpecificOutput`
        """
        return self.__e_wallet_refund_method_specific_output

    @e_wallet_refund_method_specific_output.setter
    def e_wallet_refund_method_specific_output(self, value):
        self.__e_wallet_refund_method_specific_output = value

    @property
    def mobile_refund_method_specific_output(self):
        """
        | Object containing specific mobile refund details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.refund_mobile_method_specific_output.RefundMobileMethodSpecificOutput`
        """
        return self.__mobile_refund_method_specific_output

    @mobile_refund_method_specific_output.setter
    def mobile_refund_method_specific_output(self, value):
        self.__mobile_refund_method_specific_output = value

    @property
    def payment_method(self):
        """
        | Payment method identifier used by the our payment engine with the following possible values:
        
        * bankRefund
        * bankTransfer
        * card
        * cash
        * directDebit
        * eInvoice
        * invoice
        * redirect
        
        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    def to_dictionary(self):
        dictionary = super(RefundOutput, self).to_dictionary()
        if self.amount_paid is not None:
            dictionary['amountPaid'] = self.amount_paid
        if self.bank_refund_method_specific_output is not None:
            dictionary['bankRefundMethodSpecificOutput'] = self.bank_refund_method_specific_output.to_dictionary()
        if self.card_refund_method_specific_output is not None:
            dictionary['cardRefundMethodSpecificOutput'] = self.card_refund_method_specific_output.to_dictionary()
        if self.e_invoice_refund_method_specific_output is not None:
            dictionary['eInvoiceRefundMethodSpecificOutput'] = self.e_invoice_refund_method_specific_output.to_dictionary()
        if self.e_wallet_refund_method_specific_output is not None:
            dictionary['eWalletRefundMethodSpecificOutput'] = self.e_wallet_refund_method_specific_output.to_dictionary()
        if self.mobile_refund_method_specific_output is not None:
            dictionary['mobileRefundMethodSpecificOutput'] = self.mobile_refund_method_specific_output.to_dictionary()
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundOutput, self).from_dictionary(dictionary)
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'bankRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['bankRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankRefundMethodSpecificOutput']))
            value = RefundBankMethodSpecificOutput()
            self.bank_refund_method_specific_output = value.from_dictionary(dictionary['bankRefundMethodSpecificOutput'])
        if 'cardRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardRefundMethodSpecificOutput']))
            value = RefundCardMethodSpecificOutput()
            self.card_refund_method_specific_output = value.from_dictionary(dictionary['cardRefundMethodSpecificOutput'])
        if 'eInvoiceRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['eInvoiceRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eInvoiceRefundMethodSpecificOutput']))
            value = RefundEInvoiceMethodSpecificOutput()
            self.e_invoice_refund_method_specific_output = value.from_dictionary(dictionary['eInvoiceRefundMethodSpecificOutput'])
        if 'eWalletRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['eWalletRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eWalletRefundMethodSpecificOutput']))
            value = RefundEWalletMethodSpecificOutput()
            self.e_wallet_refund_method_specific_output = value.from_dictionary(dictionary['eWalletRefundMethodSpecificOutput'])
        if 'mobileRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobileRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobileRefundMethodSpecificOutput']))
            value = RefundMobileMethodSpecificOutput()
            self.mobile_refund_method_specific_output = value.from_dictionary(dictionary['mobileRefundMethodSpecificOutput'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        return self
