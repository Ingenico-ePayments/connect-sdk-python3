# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.payment_product863_third_party_data import PaymentProduct863ThirdPartyData


class ThirdPartyData(DataObject):

    __payment_product863 = None

    @property
    def payment_product863(self):
        """
        | Contains the third party data for payment product 863 (WeChat Pay).
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.payment_product863_third_party_data.PaymentProduct863ThirdPartyData`
        """
        return self.__payment_product863

    @payment_product863.setter
    def payment_product863(self, value):
        self.__payment_product863 = value

    def to_dictionary(self):
        dictionary = super(ThirdPartyData, self).to_dictionary()
        if self.payment_product863 is not None:
            dictionary['paymentProduct863'] = self.payment_product863.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThirdPartyData, self).from_dictionary(dictionary)
        if 'paymentProduct863' in dictionary:
            if not isinstance(dictionary['paymentProduct863'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct863']))
            value = PaymentProduct863ThirdPartyData()
            self.payment_product863 = value.from_dictionary(dictionary['paymentProduct863'])
        return self
