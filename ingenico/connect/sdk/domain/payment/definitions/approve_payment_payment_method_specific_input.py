# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ApprovePaymentPaymentMethodSpecificInput(DataObject):

    __date_collect = None
    __token = None

    @property
    def date_collect(self):
        """
        | The desired date for the collection
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__date_collect

    @date_collect.setter
    def date_collect(self, value):
        self.__date_collect = value

    @property
    def token(self):
        """
        | Token containing tokenized bank account details
        
        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    def to_dictionary(self):
        dictionary = super(ApprovePaymentPaymentMethodSpecificInput, self).to_dictionary()
        if self.date_collect is not None:
            dictionary['dateCollect'] = self.date_collect
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePaymentPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'dateCollect' in dictionary:
            self.date_collect = dictionary['dateCollect']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
