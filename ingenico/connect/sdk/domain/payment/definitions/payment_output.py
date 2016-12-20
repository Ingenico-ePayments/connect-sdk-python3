#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_output import BankTransferPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_output import CardPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_output import CashPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.invoice_payment_method_specific_output import InvoicePaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.mobile_payment_method_specific_output import MobilePaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_method_specific_output import NonSepaDirectDebitPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.order_output import OrderOutput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_output import RedirectPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_output import SepaDirectDebitPaymentMethodSpecificOutput


class PaymentOutput(OrderOutput):
    """
    Class PaymentOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentOutput
    """

    __amount_paid = None
    __bank_transfer_payment_method_specific_output = None
    __card_payment_method_specific_output = None
    __cash_payment_method_specific_output = None
    __direct_debit_payment_method_specific_output = None
    __invoice_payment_method_specific_output = None
    __mobile_payment_method_specific_output = None
    __payment_method = None
    __redirect_payment_method_specific_output = None
    __sepa_direct_debit_payment_method_specific_output = None

    @property
    def amount_paid(self):
        """
        int
        """
        return self.__amount_paid

    @amount_paid.setter
    def amount_paid(self, value):
        self.__amount_paid = value

    @property
    def bank_transfer_payment_method_specific_output(self):
        """
        :class:`BankTransferPaymentMethodSpecificOutput`
        """
        return self.__bank_transfer_payment_method_specific_output

    @bank_transfer_payment_method_specific_output.setter
    def bank_transfer_payment_method_specific_output(self, value):
        self.__bank_transfer_payment_method_specific_output = value

    @property
    def card_payment_method_specific_output(self):
        """
        :class:`CardPaymentMethodSpecificOutput`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value):
        self.__card_payment_method_specific_output = value

    @property
    def cash_payment_method_specific_output(self):
        """
        :class:`CashPaymentMethodSpecificOutput`
        """
        return self.__cash_payment_method_specific_output

    @cash_payment_method_specific_output.setter
    def cash_payment_method_specific_output(self, value):
        self.__cash_payment_method_specific_output = value

    @property
    def direct_debit_payment_method_specific_output(self):
        """
        :class:`NonSepaDirectDebitPaymentMethodSpecificOutput`
        """
        return self.__direct_debit_payment_method_specific_output

    @direct_debit_payment_method_specific_output.setter
    def direct_debit_payment_method_specific_output(self, value):
        self.__direct_debit_payment_method_specific_output = value

    @property
    def invoice_payment_method_specific_output(self):
        """
        :class:`InvoicePaymentMethodSpecificOutput`
        """
        return self.__invoice_payment_method_specific_output

    @invoice_payment_method_specific_output.setter
    def invoice_payment_method_specific_output(self, value):
        self.__invoice_payment_method_specific_output = value

    @property
    def mobile_payment_method_specific_output(self):
        """
        :class:`MobilePaymentMethodSpecificOutput`
        """
        return self.__mobile_payment_method_specific_output

    @mobile_payment_method_specific_output.setter
    def mobile_payment_method_specific_output(self, value):
        self.__mobile_payment_method_specific_output = value

    @property
    def payment_method(self):
        """
        str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    @property
    def redirect_payment_method_specific_output(self):
        """
        :class:`RedirectPaymentMethodSpecificOutput`
        """
        return self.__redirect_payment_method_specific_output

    @redirect_payment_method_specific_output.setter
    def redirect_payment_method_specific_output(self, value):
        self.__redirect_payment_method_specific_output = value

    @property
    def sepa_direct_debit_payment_method_specific_output(self):
        """
        :class:`SepaDirectDebitPaymentMethodSpecificOutput`
        """
        return self.__sepa_direct_debit_payment_method_specific_output

    @sepa_direct_debit_payment_method_specific_output.setter
    def sepa_direct_debit_payment_method_specific_output(self, value):
        self.__sepa_direct_debit_payment_method_specific_output = value

    def to_dictionary(self):
        dictionary = super(PaymentOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountPaid', self.amount_paid)
        self._add_to_dictionary(dictionary, 'bankTransferPaymentMethodSpecificOutput', self.bank_transfer_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificOutput', self.card_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'cashPaymentMethodSpecificOutput', self.cash_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'directDebitPaymentMethodSpecificOutput', self.direct_debit_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'invoicePaymentMethodSpecificOutput', self.invoice_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'mobilePaymentMethodSpecificOutput', self.mobile_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'paymentMethod', self.payment_method)
        self._add_to_dictionary(dictionary, 'redirectPaymentMethodSpecificOutput', self.redirect_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'sepaDirectDebitPaymentMethodSpecificOutput', self.sepa_direct_debit_payment_method_specific_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentOutput, self).from_dictionary(dictionary)
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'bankTransferPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['bankTransferPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankTransferPaymentMethodSpecificOutput']))
            value = BankTransferPaymentMethodSpecificOutput()
            self.bank_transfer_payment_method_specific_output = value.from_dictionary(dictionary['bankTransferPaymentMethodSpecificOutput'])
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = CardPaymentMethodSpecificOutput()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'cashPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cashPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cashPaymentMethodSpecificOutput']))
            value = CashPaymentMethodSpecificOutput()
            self.cash_payment_method_specific_output = value.from_dictionary(dictionary['cashPaymentMethodSpecificOutput'])
        if 'directDebitPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['directDebitPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['directDebitPaymentMethodSpecificOutput']))
            value = NonSepaDirectDebitPaymentMethodSpecificOutput()
            self.direct_debit_payment_method_specific_output = value.from_dictionary(dictionary['directDebitPaymentMethodSpecificOutput'])
        if 'invoicePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['invoicePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['invoicePaymentMethodSpecificOutput']))
            value = InvoicePaymentMethodSpecificOutput()
            self.invoice_payment_method_specific_output = value.from_dictionary(dictionary['invoicePaymentMethodSpecificOutput'])
        if 'mobilePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificOutput']))
            value = MobilePaymentMethodSpecificOutput()
            self.mobile_payment_method_specific_output = value.from_dictionary(dictionary['mobilePaymentMethodSpecificOutput'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'redirectPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificOutput']))
            value = RedirectPaymentMethodSpecificOutput()
            self.redirect_payment_method_specific_output = value.from_dictionary(dictionary['redirectPaymentMethodSpecificOutput'])
        if 'sepaDirectDebitPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificOutput']))
            value = SepaDirectDebitPaymentMethodSpecificOutput()
            self.sepa_direct_debit_payment_method_specific_output = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'])
        return self
