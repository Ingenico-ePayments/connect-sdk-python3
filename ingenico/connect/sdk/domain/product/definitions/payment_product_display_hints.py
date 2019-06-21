# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProductDisplayHints(DataObject):

    __display_order = None
    __label = None
    __logo = None

    @property
    def display_order(self):
        """
        | Determines the order in which the payment products and groups should be shown (sorted ascending)
        
        Type: int
        """
        return self.__display_order

    @display_order.setter
    def display_order(self, value):
        self.__display_order = value

    @property
    def label(self):
        """
        | Name of the field based on the locale that was included in the request
        
        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value

    @property
    def logo(self):
        """
        | Partial URL that you can reference for the image of this payment product. You can use our server-side resize functionality by appending '?size={{width}}x{{height}}' to the full URL, where width and height are specified in pixels. The resized image will always keep its correct aspect ratio.
        
        Type: str
        """
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value

    def to_dictionary(self):
        dictionary = super(PaymentProductDisplayHints, self).to_dictionary()
        if self.display_order is not None:
            dictionary['displayOrder'] = self.display_order
        if self.label is not None:
            dictionary['label'] = self.label
        if self.logo is not None:
            dictionary['logo'] = self.logo
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductDisplayHints, self).from_dictionary(dictionary)
        if 'displayOrder' in dictionary:
            self.display_order = dictionary['displayOrder']
        if 'label' in dictionary:
            self.label = dictionary['label']
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
