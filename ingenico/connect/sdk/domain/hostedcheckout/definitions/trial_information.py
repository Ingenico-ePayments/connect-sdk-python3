# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.hostedcheckout.definitions.frequency import Frequency
from ingenico.connect.sdk.domain.hostedcheckout.definitions.trial_period import TrialPeriod


class TrialInformation(DataObject):
    """
    | The object containing data of the trial period: no-cost or discounted time-constrained trial subscription period.
    """

    __amount_of_money_after_trial = None
    __end_date = None
    __is_recurring = None
    __trial_period = None
    __trial_period_recurring = None

    @property
    def amount_of_money_after_trial(self):
        """
        | The object containing the amount and ISO currency code attributes of money to be paid after the trial period ends.
        
        | Note:
        
        | The property order.amountOfMoney should be populated with the amount to be paid during or for the trial period (no-cost or discounted time-constrained trial subscription period).
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money_after_trial

    @amount_of_money_after_trial.setter
    def amount_of_money_after_trial(self, value):
        self.__amount_of_money_after_trial = value

    @property
    def end_date(self):
        """
        | The date that the trial period ends in YYYYMMDD format.
        
        Type: str
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value

    @property
    def is_recurring(self):
        """
        | The property specifying if there will be recurring charges throughout the trial period (when the trial period involves a temporary discounted rate).
        | True = there will be recurring charges during the trial period
        | False = there will not be recurring charges during the trial period
        
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def trial_period(self):
        """
        | The object containing information on the trial period duration and the interval between payments during that period.
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.trial_period.TrialPeriod`
        """
        return self.__trial_period

    @trial_period.setter
    def trial_period(self, value):
        self.__trial_period = value

    @property
    def trial_period_recurring(self):
        """
        | The object containing the frequency and interval between recurring payments.
        
        | Note:
        
        | This object should only be populated if the frequency of recurring payments between the trial and regular periods is different.
        
        | If you do not populated this object, then the same interval frequency and interval of recurringPaymentsData.recurringInterval will be used
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.frequency.Frequency`
        """
        return self.__trial_period_recurring

    @trial_period_recurring.setter
    def trial_period_recurring(self, value):
        self.__trial_period_recurring = value

    def to_dictionary(self):
        dictionary = super(TrialInformation, self).to_dictionary()
        if self.amount_of_money_after_trial is not None:
            dictionary['amountOfMoneyAfterTrial'] = self.amount_of_money_after_trial.to_dictionary()
        if self.end_date is not None:
            dictionary['endDate'] = self.end_date
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.trial_period is not None:
            dictionary['trialPeriod'] = self.trial_period.to_dictionary()
        if self.trial_period_recurring is not None:
            dictionary['trialPeriodRecurring'] = self.trial_period_recurring.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(TrialInformation, self).from_dictionary(dictionary)
        if 'amountOfMoneyAfterTrial' in dictionary:
            if not isinstance(dictionary['amountOfMoneyAfterTrial'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoneyAfterTrial']))
            value = AmountOfMoney()
            self.amount_of_money_after_trial = value.from_dictionary(dictionary['amountOfMoneyAfterTrial'])
        if 'endDate' in dictionary:
            self.end_date = dictionary['endDate']
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'trialPeriod' in dictionary:
            if not isinstance(dictionary['trialPeriod'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['trialPeriod']))
            value = TrialPeriod()
            self.trial_period = value.from_dictionary(dictionary['trialPeriod'])
        if 'trialPeriodRecurring' in dictionary:
            if not isinstance(dictionary['trialPeriodRecurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['trialPeriodRecurring']))
            value = Frequency()
            self.trial_period_recurring = value.from_dictionary(dictionary['trialPeriodRecurring'])
        return self
