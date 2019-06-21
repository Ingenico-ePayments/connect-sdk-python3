# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MandateApproval(DataObject):

    __mandate_signature_date = None
    __mandate_signature_place = None
    __mandate_signed = None

    @property
    def mandate_signature_date(self):
        """
        | The date when the mandate was signed
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__mandate_signature_date

    @mandate_signature_date.setter
    def mandate_signature_date(self, value):
        self.__mandate_signature_date = value

    @property
    def mandate_signature_place(self):
        """
        | The city where the mandate was signed
        
        Type: str
        """
        return self.__mandate_signature_place

    @mandate_signature_place.setter
    def mandate_signature_place(self, value):
        self.__mandate_signature_place = value

    @property
    def mandate_signed(self):
        """
        * true = Mandate is signed
        * false = Mandate is not signed
        
        Type: bool
        """
        return self.__mandate_signed

    @mandate_signed.setter
    def mandate_signed(self, value):
        self.__mandate_signed = value

    def to_dictionary(self):
        dictionary = super(MandateApproval, self).to_dictionary()
        if self.mandate_signature_date is not None:
            dictionary['mandateSignatureDate'] = self.mandate_signature_date
        if self.mandate_signature_place is not None:
            dictionary['mandateSignaturePlace'] = self.mandate_signature_place
        if self.mandate_signed is not None:
            dictionary['mandateSigned'] = self.mandate_signed
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateApproval, self).from_dictionary(dictionary)
        if 'mandateSignatureDate' in dictionary:
            self.mandate_signature_date = dictionary['mandateSignatureDate']
        if 'mandateSignaturePlace' in dictionary:
            self.mandate_signature_place = dictionary['mandateSignaturePlace']
        if 'mandateSigned' in dictionary:
            self.mandate_signed = dictionary['mandateSigned']
        return self
