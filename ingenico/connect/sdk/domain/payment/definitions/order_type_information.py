# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class OrderTypeInformation(DataObject):

    __purchase_type = None
    __transaction_type = None
    __usage_type = None

    @property
    def purchase_type(self):
        """
        | Possible values are:
        
        * physical
        * digital
        
        Type: str
        """
        return self.__purchase_type

    @purchase_type.setter
    def purchase_type(self, value):
        self.__purchase_type = value

    @property
    def transaction_type(self):
        """
        | Identifies the type of transaction being authenticated.Possible values are:
        
        * purchase = The purpose of the transaction is to purchase goods or services
        * check-acceptance = The purpose of the transaction is to accept a 'check'/'cheque'
        * account-funding = The purpose of the transaction is to fund an account
        * quasi-cash = The purpose of the transaction is to buy a quasi cash type product that is representative of actual cash such as money orders, traveler's checks, foreign currency, lottery tickets or casino gaming chips
        * prepaid-activation-or-load = The purpose of the transaction is to activate or load a prepaid card
        
        Type: str
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self.__transaction_type = value

    @property
    def usage_type(self):
        """
        | Possible values are:
        
        * private
        * commercial
        
        Type: str
        """
        return self.__usage_type

    @usage_type.setter
    def usage_type(self, value):
        self.__usage_type = value

    def to_dictionary(self):
        dictionary = super(OrderTypeInformation, self).to_dictionary()
        if self.purchase_type is not None:
            dictionary['purchaseType'] = self.purchase_type
        if self.transaction_type is not None:
            dictionary['transactionType'] = self.transaction_type
        if self.usage_type is not None:
            dictionary['usageType'] = self.usage_type
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderTypeInformation, self).from_dictionary(dictionary)
        if 'purchaseType' in dictionary:
            self.purchase_type = dictionary['purchaseType']
        if 'transactionType' in dictionary:
            self.transaction_type = dictionary['transactionType']
        if 'usageType' in dictionary:
            self.usage_type = dictionary['usageType']
        return self
