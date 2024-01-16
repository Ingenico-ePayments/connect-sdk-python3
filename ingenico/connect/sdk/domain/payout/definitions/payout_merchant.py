# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject


class PayoutMerchant(DataObject):

    __configuration_id = None

    @property
    def configuration_id(self):
        """
        | In case your account has been setup with multiple configurations you can use this property to identify the one you would like to use for the transaction. Note that you can only submit preconfigured values in combination with the Worldline Online Payments Acceptance platform. In case no value is supplied a default value of 0 will be submitted to the Worldline Online Payments Acceptance platform. The Worldline Online Payments Acceptance platform internally refers to this as a PosId.
        
        Type: str
        """
        return self.__configuration_id

    @configuration_id.setter
    def configuration_id(self, value):
        self.__configuration_id = value

    def to_dictionary(self):
        dictionary = super(PayoutMerchant, self).to_dictionary()
        if self.configuration_id is not None:
            dictionary['configurationId'] = self.configuration_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutMerchant, self).from_dictionary(dictionary)
        if 'configurationId' in dictionary:
            self.configuration_id = dictionary['configurationId']
        return self
