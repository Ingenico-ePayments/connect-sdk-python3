# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_display_element import PaymentProductFieldDisplayElement


class ValueMappingElement(DataObject):

    __display_elements = None
    __display_name = None
    __value = None

    @property
    def display_elements(self):
        """
        | List of extra data of the value.
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.payment_product_field_display_element.PaymentProductFieldDisplayElement`]
        """
        return self.__display_elements

    @display_elements.setter
    def display_elements(self, value):
        self.__display_elements = value

    @property
    def display_name(self):
        """
        | Key name
        
        Type: str
        
        Deprecated; Use displayElements instead with ID 'displayName'
        """
        return self.__display_name

    @display_name.setter
    def display_name(self, value):
        self.__display_name = value

    @property
    def value(self):
        """
        | Value corresponding to the key
        
        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(ValueMappingElement, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'displayElements', self.display_elements)
        self._add_to_dictionary(dictionary, 'displayName', self.display_name)
        self._add_to_dictionary(dictionary, 'value', self.value)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ValueMappingElement, self).from_dictionary(dictionary)
        if 'displayElements' in dictionary:
            if not isinstance(dictionary['displayElements'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['displayElements']))
            self.display_elements = []
            for displayElements_element in dictionary['displayElements']:
                displayElements_value = PaymentProductFieldDisplayElement()
                self.display_elements.append(displayElements_value.from_dictionary(displayElements_element))
        if 'displayName' in dictionary:
            self.display_name = dictionary['displayName']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
