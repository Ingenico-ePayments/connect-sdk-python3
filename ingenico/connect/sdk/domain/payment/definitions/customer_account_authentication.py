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

    __data = None
    __method = None
    __utc_timestamp = None

    @property
    def data(self):
        """
        | Data that documents and supports a specific authentication process submitted using the order.customer.account.authentication.method property. The data submitted using this property will be used by the issuer to validate the used authentication method.
        | For example, if the order.customer.account.authentication.method is:
        
        * federated-id, then this element can carry information about the provider of the federated ID and related information.
        * fido-authentication, then this element can carry the FIDO attestation data (including the signature).
        * fido-authentication-with-signed-assurance-data, then this element can carry FIDO Attestation data with the FIDO assurance data signed.
        * src-assurance-data, then this element can carry the SRC assurance data
        
        Type: str
        """
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def method(self):
        """
        | Authentication used by the customer on your website or app
        | Possible values :
        
        * guest = no login occurred, customer is 'logged in' as guest
        * merchant-credentials = the customer logged in using credentials that are specific to you 
        * federated-id = the customer logged in using a federated ID
        * issuer-credentials = the customer logged in using credentials from the card issuer (of the card used in this transaction)
        * third-party-authentication = the customer logged in using third-party authentication
        * fido-authentication = the customer logged in using a FIDO authenticator
        * fido-authentication-with-signed-assurance-data = the customer logged in using a FIDO authenticator which also provides signed assurance data
        * src-assurance-data = the customer authenticated themselves during a Secure Remote Commerce session
        
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
        if self.data is not None:
            dictionary['data'] = self.data
        if self.method is not None:
            dictionary['method'] = self.method
        if self.utc_timestamp is not None:
            dictionary['utcTimestamp'] = self.utc_timestamp
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerAccountAuthentication, self).from_dictionary(dictionary)
        if 'data' in dictionary:
            self.data = dictionary['data']
        if 'method' in dictionary:
            self.method = dictionary['method']
        if 'utcTimestamp' in dictionary:
            self.utc_timestamp = dictionary['utcTimestamp']
        return self
