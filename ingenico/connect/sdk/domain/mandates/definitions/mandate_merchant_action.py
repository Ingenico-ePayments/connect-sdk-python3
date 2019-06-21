# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.mandates.definitions.mandate_redirect_data import MandateRedirectData


class MandateMerchantAction(DataObject):

    __action_type = None
    __redirect_data = None

    @property
    def action_type(self):
        """
        | Action merchants needs to take in the online mandate process. Possible values are:
        
        * REDIRECT - The customer needs to be redirected using the details found in redirectData
        
        Type: str
        """
        return self.__action_type

    @action_type.setter
    def action_type(self, value):
        self.__action_type = value

    @property
    def redirect_data(self):
        """
        | Object containing all data needed to redirect the customer
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.mandate_redirect_data.MandateRedirectData`
        """
        return self.__redirect_data

    @redirect_data.setter
    def redirect_data(self, value):
        self.__redirect_data = value

    def to_dictionary(self):
        dictionary = super(MandateMerchantAction, self).to_dictionary()
        if self.action_type is not None:
            dictionary['actionType'] = self.action_type
        if self.redirect_data is not None:
            dictionary['redirectData'] = self.redirect_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateMerchantAction, self).from_dictionary(dictionary)
        if 'actionType' in dictionary:
            self.action_type = dictionary['actionType']
        if 'redirectData' in dictionary:
            if not isinstance(dictionary['redirectData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectData']))
            value = MandateRedirectData()
            self.redirect_data = value.from_dictionary(dictionary['redirectData'])
        return self
