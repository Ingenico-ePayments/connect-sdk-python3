# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject


class TrialPeriod(DataObject):
    """
    | The object containing information on the trial period duration and the interval between payments during that period.
    """

    __duration = None
    __interval = None

    @property
    def duration(self):
        """
        | The number of days, weeks, months, or years before the trial period ends.
        
        Type: int
        """
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def interval(self):
        """
        | The interval for the trial period to finish specified as days, weeks, months, quarters, or years.
        
        Type: str
        """
        return self.__interval

    @interval.setter
    def interval(self, value):
        self.__interval = value

    def to_dictionary(self):
        dictionary = super(TrialPeriod, self).to_dictionary()
        if self.duration is not None:
            dictionary['duration'] = self.duration
        if self.interval is not None:
            dictionary['interval'] = self.interval
        return dictionary

    def from_dictionary(self, dictionary):
        super(TrialPeriod, self).from_dictionary(dictionary)
        if 'duration' in dictionary:
            self.duration = dictionary['duration']
        if 'interval' in dictionary:
            self.interval = dictionary['interval']
        return self
