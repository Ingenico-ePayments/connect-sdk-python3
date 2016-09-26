#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.fraud_fields import FraudFields
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input import BankTransferPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_input import CashPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.invoice_payment_method_specific_input import InvoicePaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_method_specific_input import NonSepaDirectDebitPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_input import SepaDirectDebitPaymentMethodSpecificInput


class CreatePaymentRequest(DataObject):
    """
    Class CreatePaymentRequest
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreatePaymentRequest
    
    Attributes:
        bank_transfer_payment_method_specific_input:      :class:`BankTransferPaymentMethodSpecificInput`
        card_payment_method_specific_input:               :class:`CardPaymentMethodSpecificInput`
        cash_payment_method_specific_input:               :class:`CashPaymentMethodSpecificInput`
        direct_debit_payment_method_specific_input:       :class:`NonSepaDirectDebitPaymentMethodSpecificInput`
        encrypted_customer_input:                         str
        fraud_fields:                                     :class:`FraudFields`
        invoice_payment_method_specific_input:            :class:`InvoicePaymentMethodSpecificInput`
        order:                                            :class:`Order`
        redirect_payment_method_specific_input:           :class:`RedirectPaymentMethodSpecificInput`
        sepa_direct_debit_payment_method_specific_input:  :class:`SepaDirectDebitPaymentMethodSpecificInput`
     """

    bank_transfer_payment_method_specific_input = None
    card_payment_method_specific_input = None
    cash_payment_method_specific_input = None
    direct_debit_payment_method_specific_input = None
    encrypted_customer_input = None
    fraud_fields = None
    invoice_payment_method_specific_input = None
    order = None
    redirect_payment_method_specific_input = None
    sepa_direct_debit_payment_method_specific_input = None

    def to_dictionary(self):
        dictionary = super(CreatePaymentRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankTransferPaymentMethodSpecificInput', self.bank_transfer_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'cardPaymentMethodSpecificInput', self.card_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'cashPaymentMethodSpecificInput', self.cash_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'directDebitPaymentMethodSpecificInput', self.direct_debit_payment_method_specific_input)
        self._add_to_dictionary(dictionary, 'encryptedCustomerInput', self.encrypted_customer_input)
        self._add_to_dictionary(dictionary, 'fraudFields', self.fraud_fields)
        self._add_to_dictionary(dictionary, 'invoicePaymentMethodSpecificInput', self.invoice_payment_method_specific_input)
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
