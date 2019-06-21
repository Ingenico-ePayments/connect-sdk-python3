# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ApprovePayoutRequest(DataObject):

    __date_payout = None

    @property
    def date_payout(self):
        """
        | The desired date for the payout
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__date_payout

    @date_payout.setter
    def date_payout(self, value):
        self.__date_payout = value

    def to_dictionary(self):
        dictionary = super(ApprovePayoutRequest, self).to_dictionary()
        if self.date_payout is not None:
            dictionary['datePayout'] = self.date_payout
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePayoutRequest, self).from_dictionary(dictionary)
        if 'datePayout' in dictionary:
            self.date_payout = dictionary['datePayout']
        return self
