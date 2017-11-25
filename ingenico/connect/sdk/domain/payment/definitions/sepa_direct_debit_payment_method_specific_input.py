# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.sepa_direct_debit_payment_method_specific_input_base import SepaDirectDebitPaymentMethodSpecificInputBase


class SepaDirectDebitPaymentMethodSpecificInput(SepaDirectDebitPaymentMethodSpecificInputBase):

    __date_collect = None
    __direct_debit_text = None
    __is_recurring = None
    __recurring_payment_sequence_indicator = None
    __token = None
    __tokenize = None

    @property
    def date_collect(self):
        """
        | Changed date for direct debit collection. Only relevant for legacy SEPA Direct Debit.
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__date_collect

    @date_collect.setter
    def date_collect(self, value):
        self.__date_collect = value

    @property
    def direct_debit_text(self):
        """
        | Description of the transaction that will appear on the consumer bank statement to aid the consumer in recognizing the transaction. Only relevant for legacy SEPA Direct Debit.
        
        Type: str
        """
        return self.__direct_debit_text

    @direct_debit_text.setter
    def direct_debit_text(self, value):
        self.__direct_debit_text = value

    @property
    def is_recurring(self):
        """
        | Indicates if this transaction is of a one-off or a recurring type. Only relevant for legacy SEPA Direct Debit.
        
        * true - This is recurring
        * false - This is one-off
        
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        | Only relevant for legacy SEPA Direct Debit.
        
        * first = This transaction is the first of a series of recurring transactions
        * recurring = This transaction is a subsequent transaction in a series of recurring transactions
        * last = This transaction is the last transaction of a series of recurring transactions
        
        Type: str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value):
        self.__recurring_payment_sequence_indicator = value

    @property
    def token(self):
        """
        | ID of the token that holds previously stored SEPA Direct Debit account and mandate data. Only relevant for legacy SEPA Direct Debit.
        
        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    @property
    def tokenize(self):
        """
        | Indicates if this transaction should be tokenized. Only relevant for legacy SEPA Direct Debit.
        
        * true - Tokenize the transaction
        * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.
        
        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value):
        self.__tokenize = value

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dateCollect', self.date_collect)
        self._add_to_dictionary(dictionary, 'directDebitText', self.direct_debit_text)
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        self._add_to_dictionary(dictionary, 'recurringPaymentSequenceIndicator', self.recurring_payment_sequence_indicator)
        self._add_to_dictionary(dictionary, 'token', self.token)
        self._add_to_dictionary(dictionary, 'tokenize', self.tokenize)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'dateCollect' in dictionary:
            self.date_collect = dictionary['dateCollect']
        if 'directDebitText' in dictionary:
            self.direct_debit_text = dictionary['directDebitText']
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self
