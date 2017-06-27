# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ExternalCardholderAuthenticationData(DataObject):

    __cavv = None
    __cavv_algorithm = None
    __eci = None
    __validation_result = None
    __xid = None

    @property
    def cavv(self):
        """
        | The CAVV (cardholder authentication verification value) or AAV (accountholder authentication value) provides an authentication validation value.
        
        Type: str
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value

    @property
    def cavv_algorithm(self):
        """
        | The algorithm, from your 3D Secure provider, used to generate the authentication CAVV.
        
        Type: str
        """
        return self.__cavv_algorithm

    @cavv_algorithm.setter
    def cavv_algorithm(self, value):
        self.__cavv_algorithm = value

    @property
    def eci(self):
        """
        | Electronic Commerce Indicator provides authentication validation results returned after AUTHENTICATIONVALIDATION
        
        * 0 = No authentication, Internet (no liability shift, not a 3D Secure transaction)
        * 1 = Authentication attempted (MasterCard)
        * 2 = Successful authentication (MasterCard)
        * 5 = Successful authentication (Visa, Diners Club, Amex)
        * 6 = Authentication attempted (Visa, Diners Club, Amex)
        * 7 = No authentication, Internet (no liability shift, not a 3D Secure transaction)
        * (empty) = Not checked or not enrolled
        
        Type: int
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def validation_result(self):
        """
        | The 3D Secure authentication result from your 3D Secure provider.
        
        Type: str
        """
        return self.__validation_result

    @validation_result.setter
    def validation_result(self, value):
        self.__validation_result = value

    @property
    def xid(self):
        """
        | The transaction ID that is used for the 3D Authentication
        
        Type: str
        """
        return self.__xid

    @xid.setter
    def xid(self, value):
        self.__xid = value

    def to_dictionary(self):
        dictionary = super(ExternalCardholderAuthenticationData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cavv', self.cavv)
        self._add_to_dictionary(dictionary, 'cavvAlgorithm', self.cavv_algorithm)
        self._add_to_dictionary(dictionary, 'eci', self.eci)
        self._add_to_dictionary(dictionary, 'validationResult', self.validation_result)
        self._add_to_dictionary(dictionary, 'xid', self.xid)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ExternalCardholderAuthenticationData, self).from_dictionary(dictionary)
        if 'cavv' in dictionary:
            self.cavv = dictionary['cavv']
        if 'cavvAlgorithm' in dictionary:
            self.cavv_algorithm = dictionary['cavvAlgorithm']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'validationResult' in dictionary:
            self.validation_result = dictionary['validationResult']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self
