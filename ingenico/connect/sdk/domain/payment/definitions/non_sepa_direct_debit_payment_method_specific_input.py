#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.non_sepa_direct_debit_payment_product705_specific_input import NonSepaDirectDebitPaymentProduct705SpecificInput


class NonSepaDirectDebitPaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):
    """
    Class NonSepaDirectDebitPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_NonSepaDirectDebitPaymentMethodSpecificInput
    """

    __date_collect = None
    __direct_debit_text = None
    __is_recurring = None
    __payment_product705_specific_input = None
    __recurring_payment_sequence_indicator = None
    __token = None
    __tokenize = None

    @property
    def date_collect(self):
        """
        str
        """
        return self.__date_collect

    @date_collect.setter
    def date_collect(self, value):
        self.__date_collect = value

    @property
    def direct_debit_text(self):
        """
        str
        """
        return self.__direct_debit_text

    @direct_debit_text.setter
    def direct_debit_text(self, value):
        self.__direct_debit_text = value

    @property
    def is_recurring(self):
        """
        bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def payment_product705_specific_input(self):
        """
        :class:`NonSepaDirectDebitPaymentProduct705SpecificInput`
        """
        return self.__payment_product705_specific_input

    @payment_product705_specific_input.setter
    def payment_product705_specific_input(self, value):
        self.__payment_product705_specific_input = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value):
        self.__recurring_payment_sequence_indicator = value

    @property
    def token(self):
        """
        str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    @property
    def tokenize(self):
        """
        bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value):
        self.__tokenize = value

    def to_dictionary(self):
        dictionary = super(NonSepaDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dateCollect', self.date_collect)
        self._add_to_dictionary(dictionary, 'directDebitText', self.direct_debit_text)
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        self._add_to_dictionary(dictionary, 'paymentProduct705SpecificInput', self.payment_product705_specific_input)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'token', self.token)
        self._add_to_dictionary(dictionary, 'tokenize', self.tokenize)
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
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self
