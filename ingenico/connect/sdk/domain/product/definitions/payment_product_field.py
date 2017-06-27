# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_data_restrictions import PaymentProductFieldDataRestrictions
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_display_hints import PaymentProductFieldDisplayHints


class PaymentProductField(DataObject):

    __data_restrictions = None
    __display_hints = None
    __id = None
    __type = None

    @property
    def data_restrictions(self):
        """
        | Object containing data restrictions that apply to this field, like minimum and/or maximum length
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product_field_data_restrictions.PaymentProductFieldDataRestrictions`
        """
        return self.__data_restrictions

    @data_restrictions.setter
    def data_restrictions(self, value):
        self.__data_restrictions = value

    @property
    def display_hints(self):
        """
        | Object containing display hints for this field, like the order, mask, preferred keyboard
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product_field_display_hints.PaymentProductFieldDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def id(self):
        """
        | The ID of the field
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def type(self):
        """
        | The type of field, possible values are:
        
        * string - Any UTF-8 chracter
        * numericstring - A string that consisting only of numbers. Note that you should strip out anything that is not a digit, but leading zeros are allowed
        * date - Date in the format DDMMYYYY
        * expirydate - Expiration date in the format MMYY
        * integer - An integer
        
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(PaymentProductField, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dataRestrictions', self.data_restrictions)
        self._add_to_dictionary(dictionary, 'displayHints', self.display_hints)
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'type', self.type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductField, self).from_dictionary(dictionary)
        if 'dataRestrictions' in dictionary:
            if not isinstance(dictionary['dataRestrictions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['dataRestrictions']))
            value = PaymentProductFieldDataRestrictions()
            self.data_restrictions = value.from_dictionary(dictionary['dataRestrictions'])
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductFieldDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
