# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_three_d_secure import AbstractThreeDSecure
from ingenico.connect.sdk.domain.payment.definitions.external_cardholder_authentication_data import ExternalCardholderAuthenticationData
from ingenico.connect.sdk.domain.payment.definitions.redirection_data import RedirectionData


class ThreeDSecure(AbstractThreeDSecure):
    """
    | Object containing specific data regarding 3-D Secure
    """

    __external_cardholder_authentication_data = None
    __redirection_data = None

    @property
    def external_cardholder_authentication_data(self):
        """
        | Object containing 3D secure details.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.external_cardholder_authentication_data.ExternalCardholderAuthenticationData`
        """
        return self.__external_cardholder_authentication_data

    @external_cardholder_authentication_data.setter
    def external_cardholder_authentication_data(self, value):
        self.__external_cardholder_authentication_data = value

    @property
    def redirection_data(self):
        """
        | Object containing browser specific redirection related data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirection_data.RedirectionData`
        """
        return self.__redirection_data

    @redirection_data.setter
    def redirection_data(self, value):
        self.__redirection_data = value

    def to_dictionary(self):
        dictionary = super(ThreeDSecure, self).to_dictionary()
        if self.external_cardholder_authentication_data is not None:
            dictionary['externalCardholderAuthenticationData'] = self.external_cardholder_authentication_data.to_dictionary()
        if self.redirection_data is not None:
            dictionary['redirectionData'] = self.redirection_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSecure, self).from_dictionary(dictionary)
        if 'externalCardholderAuthenticationData' in dictionary:
            if not isinstance(dictionary['externalCardholderAuthenticationData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['externalCardholderAuthenticationData']))
            value = ExternalCardholderAuthenticationData()
            self.external_cardholder_authentication_data = value.from_dictionary(dictionary['externalCardholderAuthenticationData'])
        if 'redirectionData' in dictionary:
            if not isinstance(dictionary['redirectionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectionData']))
            value = RedirectionData()
            self.redirection_data = value.from_dictionary(dictionary['redirectionData'])
        return self
