# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProductNetworksResponse(DataObject):

    __networks = None

    @property
    def networks(self):
        """
        | Array containing network entries for a payment product. The strings that represent the networks in the array are identical to the strings that the payment product vendors use in their documentation.For instance: "Visa" for Google Pay <https://developer.apple.com/reference/passkit/pkpaymentnetwork>.
        
        Type: list[str]
        """
        return self.__networks

    @networks.setter
    def networks(self, value):
        self.__networks = value

    def to_dictionary(self):
        dictionary = super(PaymentProductNetworksResponse, self).to_dictionary()
        if self.networks is not None:
            dictionary['networks'] = []
            for element in self.networks:
                if element is not None:
                    dictionary['networks'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductNetworksResponse, self).from_dictionary(dictionary)
        if 'networks' in dictionary:
            if not isinstance(dictionary['networks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['networks']))
            self.networks = []
            for element in dictionary['networks']:
                self.networks.append(element)
        return self
