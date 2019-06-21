# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.mandates.definitions.mandate_merchant_action import MandateMerchantAction
from ingenico.connect.sdk.domain.mandates.definitions.mandate_response import MandateResponse


class CreateMandateResponse(DataObject):

    __mandate = None
    __merchant_action = None

    @property
    def mandate(self):
        """
        | Object containing information on a mandate
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.mandate_response.MandateResponse`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    @property
    def merchant_action(self):
        """
        | Object that contains the action, including the needed data, that you should perform next, showing the redirect to a third party to complete the payment or like showing instructions
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.mandate_merchant_action.MandateMerchantAction`
        """
        return self.__merchant_action

    @merchant_action.setter
    def merchant_action(self, value):
        self.__merchant_action = value

    def to_dictionary(self):
        dictionary = super(CreateMandateResponse, self).to_dictionary()
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        if self.merchant_action is not None:
            dictionary['merchantAction'] = self.merchant_action.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateMandateResponse, self).from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateResponse()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        if 'merchantAction' in dictionary:
            if not isinstance(dictionary['merchantAction'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantAction']))
            value = MandateMerchantAction()
            self.merchant_action = value.from_dictionary(dictionary['merchantAction'])
        return self
