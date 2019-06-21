# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class DecryptedPaymentData(DataObject):

    __cardholder_name = None
    __cryptogram = None
    __dpan = None
    __eci = None
    __expiry_date = None
    __pan = None
    __payment_method = None

    @property
    def cardholder_name(self):
        """
        | Card holder's name on the card.
        
        * For Apple Pay, maps to the cardholderName property in the encrypted payment data.
        * For Google Pay this is not available in the encrypted payment data, and can be omitted.
        
        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value

    @property
    def cryptogram(self):
        """
        | The 3D secure online payment cryptogram.
        
        * For Apple Pay, maps to the paymentData.onlinePaymentCryptogram property in the encrypted payment data.
        * For Google Pay, maps to the paymentMethodDetails.3dsCryptogram property in the encrypted payment data.
        
        | Not allowed for Google Pay if the paymentMethod is CARD.
        
        Type: str
        """
        return self.__cryptogram

    @cryptogram.setter
    def cryptogram(self, value):
        self.__cryptogram = value

    @property
    def dpan(self):
        """
        | The device specific PAN.
        
        * For Apple Pay, maps to the applicationPrimaryAccountNumber property in the encrypted payment data.
        * For Google Pay, maps to the paymentMethodDetails.dpan property in the encrypted payment data.
        
        | Not allowed for Google Pay if the paymentMethod is CARD.
        
        Type: str
        """
        return self.__dpan

    @dpan.setter
    def dpan(self, value):
        self.__dpan = value

    @property
    def eci(self):
        """
        | Electronic Commerce Indicator.
        
        * For Apple Pay, maps to the paymentData.eciIndicator property in the encrypted payment data.
        * For Google Pay, maps to the paymentMethodDetails.3dsEciIndicator property in the encryted payment data.
        
        | Not allowed for Google Pay if the paymentMethod is CARD.
        
        Type: int
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def expiry_date(self):
        """
        | Expiry date of the card
        | Format: MMYY.
        
        * For Apple Pay, maps to the applicationExpirationDate property in the encrypted payment data. This property is formatted as YYMMDD, so this needs to be converted to get a correctly formatted expiry date.
        * For Google Pay, maps to the paymentMethodDetails.expirationMonth and paymentMethodDetails.expirationYear properties in the encrypted payment data. These need to be combined to get a correctly formatted expiry date.
        
        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    @property
    def pan(self):
        """
        | The non-device specific complete credit/debit card number (also know as the PAN).
        
        * For Apple Pay this is not available in the encrypted payment data, and must be omitted.
        * For Google Pay, maps to the paymentMethodDetails.pan property in the encrypted payment data.
        
        | Not allowed for Google Pay if the paymentMethod is TOKENIZED_CARD.
        
        Type: str
        """
        return self.__pan

    @pan.setter
    def pan(self, value):
        self.__pan = value

    @property
    def payment_method(self):
        """
        | The type of the payment credential: either CARD or TOKENIZED_CARD.
        
        * For Apple Pay this is not available in the encrypted payment data, and must be omitted.
        * For Google Pay, maps to the paymentMethod property in the encrypted payment data.
        
        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    def to_dictionary(self):
        dictionary = super(DecryptedPaymentData, self).to_dictionary()
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.cryptogram is not None:
            dictionary['cryptogram'] = self.cryptogram
        if self.dpan is not None:
            dictionary['dpan'] = self.dpan
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        if self.pan is not None:
            dictionary['pan'] = self.pan
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        return dictionary

    def from_dictionary(self, dictionary):
        super(DecryptedPaymentData, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'cryptogram' in dictionary:
            self.cryptogram = dictionary['cryptogram']
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        if 'pan' in dictionary:
            self.pan = dictionary['pan']
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        return self
