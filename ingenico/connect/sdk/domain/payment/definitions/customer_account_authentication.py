# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class CustomerAccountAuthentication(DataObject):
    """
    | Object containing data on the authentication used by the customer to access their account
    """

    __method = None
    __utc_timestamp = None

    @property
    def method(self):
        """
        | Authentication used by the customer on your website
        | Possible values :
        
        * guest = no login occurred, customer is 'logged in' as guest
        * merchant-credentials = the customer logged in using credentials that are specific to you 
        * federated-id = the customer logged in using a federated ID
        * issuer-credentials = the customer logged in using credentials from the card issuer (of the card used in this transaction)
        * third-party-authentication = the customer logged in using third-party authentication
        * fido-authentication = the customer logged in using a FIDO authenticator
        
        Type: str
        """
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def utc_timestamp(self):
        """
        | Timestamp (YYYYMMDDHHmm) of the authentication of the customer to their account with you
        
        Type: str
        """
        return self.__utc_timestamp

    @utc_timestamp.setter
    def utc_timestamp(self, value):
        self.__utc_timestamp = value

    def to_dictionary(self):
        dictionary = super(CustomerAccountAuthentication, self).to_dictionary()
        if self.method is not None:
            dictionary['method'] = self.method
        if self.utc_timestamp is not None:
            dictionary['utcTimestamp'] = self.utc_timestamp
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerAccountAuthentication, self).from_dictionary(dictionary)
        if 'method' in dictionary:
            self.method = dictionary['method']
        if 'utcTimestamp' in dictionary:
            self.utc_timestamp = dictionary['utcTimestamp']
        return self
