# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class LabelTemplateElement(DataObject):

    __attribute_key = None
    __mask = None

    @property
    def attribute_key(self):
        """
        | Name of the attribute that is shown to the customer on selection pages or screens
        
        Type: str
        """
        return self.__attribute_key

    @attribute_key.setter
    def attribute_key(self, value):
        self.__attribute_key = value

    @property
    def mask(self):
        """
        | Regular mask for the attributeKey
        | Note: The mask is optional as not every field has a mask
        
        Type: str
        """
        return self.__mask

    @mask.setter
    def mask(self, value):
        self.__mask = value

    def to_dictionary(self):
        dictionary = super(LabelTemplateElement, self).to_dictionary()
        if self.attribute_key is not None:
            dictionary['attributeKey'] = self.attribute_key
        if self.mask is not None:
            dictionary['mask'] = self.mask
        return dictionary

    def from_dictionary(self, dictionary):
        super(LabelTemplateElement, self).from_dictionary(dictionary)
        if 'attributeKey' in dictionary:
            self.attribute_key = dictionary['attributeKey']
        if 'mask' in dictionary:
            self.mask = dictionary['mask']
        return self
