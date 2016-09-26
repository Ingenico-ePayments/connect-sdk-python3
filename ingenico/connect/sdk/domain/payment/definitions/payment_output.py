#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_output import BankTransferPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_output import CardPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_output import CashPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.invoice_payment_method_specific_output import InvoicePaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_method_specific_output import NonSepaDirectDebitPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.order_output import OrderOutput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_output import RedirectPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_output import SepaDirectDebitPaymentMethodSpecificOutput


class PaymentOutput(OrderOutput):
    """
    Class PaymentOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentOutput
    
    Attributes:
        amount_paid:                                       int
        bank_transfer_payment_method_specific_output:      :class:`BankTransferPaymentMethodSpecificOutput`
        card_payment_method_specific_output:               :class:`CardPaymentMethodSpecificOutput`
        cash_payment_method_specific_output:               :class:`CashPaymentMethodSpecificOutput`
        direct_debit_payment_method_specific_output:       :class:`NonSepaDirectDebitPaymentMethodSpecificOutput`
        invoice_payment_method_specific_output:            :class:`InvoicePaymentMethodSpecificOutput`
        payment_method:                                    str
        redirect_payment_method_specific_output:           :class:`RedirectPaymentMethodSpecificOutput`
        sepa_direct_debit_payment_method_specific_output:  :class:`SepaDirectDebitPaymentMethodSpecificOutput`
     """

    amount_paid = None
    bank_transfer_payment_method_specific_output = None
    card_payment_method_specific_output = None
    cash_payment_method_specific_output = None
    direct_debit_payment_method_specific_output = None
    invoice_payment_method_specific_output = None
    payment_method = None
    redirect_payment_method_specific_output = None
    sepa_direct_debit_payment_method_specific_output = None

    def to_dictionary(self):
        dictionary = super(PaymentOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountPaid', self.amount_paid)
        self._add_to_dictionary(dictionary, 'bankTransferPaymentMethodSpecificOutput', self.bank_transfer_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificOutput', self.card_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'cashPaymentMethodSpecificOutput', self.cash_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'directDebitPaymentMethodSpecificOutput', self.direct_debit_payment_method_specific_output)
        self._add_to_dictionary(dictionary, 'invoicePaymentMethodSpecificOutput', self.invoice_payment_method_specific_output)
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
