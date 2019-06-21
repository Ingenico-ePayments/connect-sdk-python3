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
    __used_for_lookup = None

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
        
        * string - Any UTF-8 chracters
        * numericstring - A string that consisting only of numbers. Note that you should strip out anything that is not a digit, but leading zeros are allowed
        * date - Date in the format DDMMYYYY
        * expirydate - Expiration date in the format MMYY
        * integer - An integer
        * boolean - A boolean
        
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def used_for_lookup(self):
        """
        | Indicates that the product can be used in a get customer details <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/customerDetails.html> call and that when that call is done the field should be supplied as (one of the) key(s) with a valid value.
        
        Type: bool
        """
        return self.__used_for_lookup

    @used_for_lookup.setter
    def used_for_lookup(self, value):
        self.__used_for_lookup = value

    def to_dictionary(self):
        dictionary = super(PaymentProductField, self).to_dictionary()
        if self.data_restrictions is not None:
            dictionary['dataRestrictions'] = self.data_restrictions.to_dictionary()
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.type is not None:
            dictionary['type'] = self.type
        if self.used_for_lookup is not None:
            dictionary['usedForLookup'] = self.used_for_lookup
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
        if 'usedForLookup' in dictionary:
            self.used_for_lookup = dictionary['usedForLookup']
        return self
