# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class OrderInvoiceData(DataObject):

    __additional_data = None
    __invoice_date = None
    __invoice_number = None
    __text_qualifiers = None

    @property
    def additional_data(self):
        """
        | Additional data for printed invoices
        
        Type: str
        """
        return self.__additional_data

    @additional_data.setter
    def additional_data(self, value):
        self.__additional_data = value

    @property
    def invoice_date(self):
        """
        | Date and time on invoice
        | Format: YYYYMMDDHH24MISS
        
        Type: str
        """
        return self.__invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self.__invoice_date = value

    @property
    def invoice_number(self):
        """
        | Your invoice number (on printed invoice) that is also returned in our report files
        
        Type: str
        """
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self.__invoice_number = value

    @property
    def text_qualifiers(self):
        """
        | Array of 3 text qualifiers, each with a max length of 10 characters
        
        Type: list[str]
        """
        return self.__text_qualifiers

    @text_qualifiers.setter
    def text_qualifiers(self, value):
        self.__text_qualifiers = value

    def to_dictionary(self):
        dictionary = super(OrderInvoiceData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalData', self.additional_data)
        self._add_to_dictionary(dictionary, 'invoiceDate', self.invoice_date)
        self._add_to_dictionary(dictionary, 'invoiceNumber', self.invoice_number)
        self._add_to_dictionary(dictionary, 'textQualifiers', self.text_qualifiers)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderInvoiceData, self).from_dictionary(dictionary)
        if 'additionalData' in dictionary:
            self.additional_data = dictionary['additionalData']
        if 'invoiceDate' in dictionary:
            self.invoice_date = dictionary['invoiceDate']
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'textQualifiers' in dictionary:
            if not isinstance(dictionary['textQualifiers'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['textQualifiers']))
            self.text_qualifiers = []
            for textQualifiers_element in dictionary['textQualifiers']:
                self.text_qualifiers.append(textQualifiers_element)
        return self
