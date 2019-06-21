# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class MerchantRiskAssessment(DataObject):

    __website_url = None

    @property
    def website_url(self):
        """
        | The website from which the purchase was made
        
        Type: str
        """
        return self.__website_url

    @website_url.setter
    def website_url(self, value):
        self.__website_url = value

    def to_dictionary(self):
        dictionary = super(MerchantRiskAssessment, self).to_dictionary()
        if self.website_url is not None:
            dictionary['websiteUrl'] = self.website_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(MerchantRiskAssessment, self).from_dictionary(dictionary)
        if 'websiteUrl' in dictionary:
            self.website_url = dictionary['websiteUrl']
        return self
