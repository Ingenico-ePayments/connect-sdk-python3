# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentAccountOnFile(DataObject):
    """
    | Object containing information on the payment account data on file (tokens)
    """

    __create_date = None
    __number_of_card_on_file_creation_attempts_last24_hours = None

    @property
    def create_date(self):
        """
        | The date (YYYYMMDD) when the payment account on file was first created.
        
        | In case a token is used for the transaction we will use the creation date of the token in our system in case you leave this property empty.
        
        Type: str
        """
        return self.__create_date

    @create_date.setter
    def create_date(self, value):
        self.__create_date = value

    @property
    def number_of_card_on_file_creation_attempts_last24_hours(self):
        """
        | Number of attempts made to add new card to the customer account in the last 24 hours
        
        Type: int
        """
        return self.__number_of_card_on_file_creation_attempts_last24_hours

    @number_of_card_on_file_creation_attempts_last24_hours.setter
    def number_of_card_on_file_creation_attempts_last24_hours(self, value):
        self.__number_of_card_on_file_creation_attempts_last24_hours = value

    def to_dictionary(self):
        dictionary = super(PaymentAccountOnFile, self).to_dictionary()
        if self.create_date is not None:
            dictionary['createDate'] = self.create_date
        if self.number_of_card_on_file_creation_attempts_last24_hours is not None:
            dictionary['numberOfCardOnFileCreationAttemptsLast24Hours'] = self.number_of_card_on_file_creation_attempts_last24_hours
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentAccountOnFile, self).from_dictionary(dictionary)
        if 'createDate' in dictionary:
            self.create_date = dictionary['createDate']
        if 'numberOfCardOnFileCreationAttemptsLast24Hours' in dictionary:
            self.number_of_card_on_file_creation_attempts_last24_hours = dictionary['numberOfCardOnFileCreationAttemptsLast24Hours']
        return self
