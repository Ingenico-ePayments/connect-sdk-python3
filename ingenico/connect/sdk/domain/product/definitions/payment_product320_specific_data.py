# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct320SpecificData(DataObject):

    __gateway = None
    __networks = None

    @property
    def gateway(self):
        """
        | The GlobalCollect gateway identifier. You should use this when creating a tokenization specification <https://developers.google.com/pay/api/android/reference/object#Gateway>.
        
        Type: str
        """
        return self.__gateway

    @gateway.setter
    def gateway(self, value):
        self.__gateway = value

    @property
    def networks(self):
        """
        | The networks that can be used in the current payment context. The strings that represent the networks in the array are identical to the strings that Google uses in their documentation <https://developers.google.com/pay/api/android/reference/object#CardParameters>.For instance: "VISA".
        
        Type: list[str]
        """
        return self.__networks

    @networks.setter
    def networks(self, value):
        self.__networks = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct320SpecificData, self).to_dictionary()
        if self.gateway is not None:
            dictionary['gateway'] = self.gateway
        if self.networks is not None:
            dictionary['networks'] = []
            for element in self.networks:
                if element is not None:
                    dictionary['networks'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct320SpecificData, self).from_dictionary(dictionary)
        if 'gateway' in dictionary:
            self.gateway = dictionary['gateway']
        if 'networks' in dictionary:
            if not isinstance(dictionary['networks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['networks']))
            self.networks = []
            for element in dictionary['networks']:
                self.networks.append(element)
        return self
