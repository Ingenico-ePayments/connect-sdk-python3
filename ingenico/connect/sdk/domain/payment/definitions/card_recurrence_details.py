# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class CardRecurrenceDetails(DataObject):

    __end_date = None
    __min_frequency = None
    __recurring_payment_sequence_indicator = None

    @property
    def end_date(self):
        """
        | Date in YYYYMMDD after which there will be no further charges.
        
        Type: str
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value

    @property
    def min_frequency(self):
        """
        | Minimum number of days between authorizations.
        
        Type: int
        """
        return self.__min_frequency

    @min_frequency.setter
    def min_frequency(self, value):
        self.__min_frequency = value

    @property
    def recurring_payment_sequence_indicator(self):
        """
        * first = This transaction is the first of a series of recurring transactions
        * recurring = This transaction is a subsequent transaction in a series of recurring transactions
        
        
        | Note: For any first of a recurring the system will automatically create a token as you will need to use a token for any subsequent recurring transactions. In case a token already exists this is indicated in the response with a value of False for the isNewToken property in the response.
        
        Type: str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value):
        self.__recurring_payment_sequence_indicator = value

    def to_dictionary(self):
        dictionary = super(CardRecurrenceDetails, self).to_dictionary()
        if self.end_date is not None:
            dictionary['endDate'] = self.end_date
        if self.min_frequency is not None:
            dictionary['minFrequency'] = self.min_frequency
        if self.recurring_payment_sequence_indicator is not None:
            dictionary['recurringPaymentSequenceIndicator'] = self.recurring_payment_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardRecurrenceDetails, self).from_dictionary(dictionary)
        if 'endDate' in dictionary:
            self.end_date = dictionary['endDate']
        if 'minFrequency' in dictionary:
            self.min_frequency = dictionary['minFrequency']
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        return self
