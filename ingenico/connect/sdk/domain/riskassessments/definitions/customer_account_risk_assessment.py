# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class CustomerAccountRiskAssessment(DataObject):
    """
    | Object containing data related to the account the customer has with you
    """

    __has_forgotten_password = None
    __has_password = None

    @property
    def has_forgotten_password(self):
        """
        | Specifies if the customer (initially) had forgotten their password
        
        * true - The customer has forgotten their password
        * false - The customer has not forgotten their password
        
        Type: bool
        """
        return self.__has_forgotten_password

    @has_forgotten_password.setter
    def has_forgotten_password(self, value):
        self.__has_forgotten_password = value

    @property
    def has_password(self):
        """
        | Specifies if the customer entered a password to gain access to an account registered with the you
        
        * true - The customer has used a password to gain access
        * false - The customer has not used a password to gain access
        
        Type: bool
        """
        return self.__has_password

    @has_password.setter
    def has_password(self, value):
        self.__has_password = value

    def to_dictionary(self):
        dictionary = super(CustomerAccountRiskAssessment, self).to_dictionary()
        if self.has_forgotten_password is not None:
            dictionary['hasForgottenPassword'] = self.has_forgotten_password
        if self.has_password is not None:
            dictionary['hasPassword'] = self.has_password
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerAccountRiskAssessment, self).from_dictionary(dictionary)
        if 'hasForgottenPassword' in dictionary:
            self.has_forgotten_password = dictionary['hasForgottenPassword']
        if 'hasPassword' in dictionary:
            self.has_password = dictionary['hasPassword']
        return self
