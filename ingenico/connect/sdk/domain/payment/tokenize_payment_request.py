# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class TokenizePaymentRequest(DataObject):

    __alias = None

    @property
    def alias(self):
        """
        | An alias for the token. This can be used to visually represent the token.
        | If no alias is given, a payment product specific default is used, e.g. the obfuscated card number for card payment products.
        | Do not include any unobfuscated sensitive data in the alias.
        
        Type: str
        """
        return self.__alias

    @alias.setter
    def alias(self, value):
        self.__alias = value

    def to_dictionary(self):
        dictionary = super(TokenizePaymentRequest, self).to_dictionary()
        if self.alias is not None:
            dictionary['alias'] = self.alias
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenizePaymentRequest, self).from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        return self
