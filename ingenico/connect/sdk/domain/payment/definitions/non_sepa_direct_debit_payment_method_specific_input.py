#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_product705_specific_input import NonSepaDirectDebitPaymentProduct705SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_product707_specific_input import NonSepaDirectDebitPaymentProduct707SpecificInput


class NonSepaDirectDebitPaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):
    """
    Class NonSepaDirectDebitPaymentMethodSpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_NonSepaDirectDebitPaymentMethodSpecificInput
    
    Attributes:
        date_collect:                          str
        direct_debit_text:                     str
        is_recurring:                          bool
        payment_product705_specific_input:     :class:`NonSepaDirectDebitPaymentProduct705SpecificInput`
        payment_product707_specific_input:     :class:`NonSepaDirectDebitPaymentProduct707SpecificInput`
        recurring_payment_sequence_indicator:  str
        token:                                 str
     """

    date_collect = None
    direct_debit_text = None
    is_recurring = None
    payment_product705_specific_input = None
    payment_product707_specific_input = None
    recurring_payment_sequence_indicator = None
    token = None

    def to_dictionary(self):
        dictionary = super(NonSepaDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dateCollect', self.date_collect)
        self._add_to_dictionary(dictionary, 'directDebitText', self.direct_debit_text)
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        self._add_to_dictionary(dictionary, 'paymentProduct705SpecificInput', self.payment_product705_specific_input)
        self._add_to_dictionary(dictionary, 'paymentProduct707SpecificInput', self.payment_product707_specific_input)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'token', self.token)
        return dictionary

    def from_dictionary(self, dictionary):
        super(NonSepaDirectDebitPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'dateCollect' in dictionary:
            self.date_collect = dictionary['dateCollect']
        if 'directDebitText' in dictionary:
            self.direct_debit_text = dictionary['directDebitText']
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'paymentProduct705SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct705SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct705SpecificInput']))
            value = NonSepaDirectDebitPaymentProduct705SpecificInput()
            self.payment_product705_specific_input = value.from_dictionary(dictionary['paymentProduct705SpecificInput'])
        if 'paymentProduct707SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct707SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct707SpecificInput']))
            value = NonSepaDirectDebitPaymentProduct707SpecificInput()
            self.payment_product707_specific_input = value.from_dictionary(dictionary['paymentProduct707SpecificInput'])
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
