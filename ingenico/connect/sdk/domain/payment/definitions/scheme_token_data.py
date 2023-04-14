# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class SchemeTokenData(DataObject):

    __cryptogram = None
    __eci = None
    __network_token = None
    __token_expiry_date = None

    @property
    def cryptogram(self):
        """
        | The Token Cryptogram is a dynamic one-time use value that is used to verify the authenticity of the transaction and the integrity of the data used in the generation of the Token Cryptogram. Visa calls this the Token Authentication Verification Value (TAVV) cryptogram.
        
        Type: str
        """
        return self.__cryptogram

    @cryptogram.setter
    def cryptogram(self, value):
        self.__cryptogram = value

    @property
    def eci(self):
        """
        | The Electronic Commerce Indicator you got with the Token Cryptogram
        
        Type: str
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def network_token(self):
        """
        | The network token. Note: This is called Payment Token in the EMVCo documentation
        
        Type: str
        """
        return self.__network_token

    @network_token.setter
    def network_token(self, value):
        self.__network_token = value

    @property
    def token_expiry_date(self):
        """
        | The expiry date of the network token
        
        Type: str
        """
        return self.__token_expiry_date

    @token_expiry_date.setter
    def token_expiry_date(self, value):
        self.__token_expiry_date = value

    def to_dictionary(self):
        dictionary = super(SchemeTokenData, self).to_dictionary()
        if self.cryptogram is not None:
            dictionary['cryptogram'] = self.cryptogram
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.network_token is not None:
            dictionary['networkToken'] = self.network_token
        if self.token_expiry_date is not None:
            dictionary['tokenExpiryDate'] = self.token_expiry_date
        return dictionary

    def from_dictionary(self, dictionary):
        super(SchemeTokenData, self).from_dictionary(dictionary)
        if 'cryptogram' in dictionary:
            self.cryptogram = dictionary['cryptogram']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'networkToken' in dictionary:
            self.network_token = dictionary['networkToken']
        if 'tokenExpiryDate' in dictionary:
            self.token_expiry_date = dictionary['tokenExpiryDate']
        return self
