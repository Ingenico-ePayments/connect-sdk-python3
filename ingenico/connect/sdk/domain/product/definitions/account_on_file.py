# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.account_on_file_attribute import AccountOnFileAttribute
from ingenico.connect.sdk.domain.product.definitions.account_on_file_display_hints import AccountOnFileDisplayHints


class AccountOnFile(DataObject):
    """
    | Elements from the AccountsOnFile array
    """

    __attributes = None
    __display_hints = None
    __id = None
    __payment_product_id = None

    @property
    def attributes(self):
        """
        | Array containing the details of the stored token
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.account_on_file_attribute.AccountOnFileAttribute`]
        """
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        self.__attributes = value

    @property
    def display_hints(self):
        """
        | Object containing information for the client on how best to display this field
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.account_on_file_display_hints.AccountOnFileDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def id(self):
        """
        | ID of the account on file record
        
        Type: int
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def payment_product_id(self):
        """
        | Payment product identifier
        | Please see payment products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(AccountOnFile, self).to_dictionary()
        if self.attributes is not None:
            dictionary['attributes'] = []
            for element in self.attributes:
                if element is not None:
                    dictionary['attributes'].append(element.to_dictionary())
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFile, self).from_dictionary(dictionary)
        if 'attributes' in dictionary:
            if not isinstance(dictionary['attributes'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['attributes']))
            self.attributes = []
            for element in dictionary['attributes']:
                value = AccountOnFileAttribute()
                self.attributes.append(value.from_dictionary(element))
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = AccountOnFileDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
