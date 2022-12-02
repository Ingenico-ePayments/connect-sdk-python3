# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class CardEssentials(DataObject):

    __card_number = None
    __cardholder_name = None
    __expiry_date = None

    @property
    def card_number(self):
        """
        | The complete credit/debit card number
        
        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value):
        self.__card_number = value

    @property
    def cardholder_name(self):
        """
        | The card holder's name on the card.
        
        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value

    @property
    def expiry_date(self):
        """
        | Expiry date of the card
        | Format: MMYY
        
        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    def to_dictionary(self):
        dictionary = super(CardEssentials, self).to_dictionary()
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardEssentials, self).from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
