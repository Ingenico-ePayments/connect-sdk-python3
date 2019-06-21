# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.seller import Seller


class Merchant(DataObject):

    __contact_website_url = None
    __seller = None
    __website_url = None

    @property
    def contact_website_url(self):
        """
        | URL to find contact or support details to contact in case of questions.
        
        Type: str
        """
        return self.__contact_website_url

    @contact_website_url.setter
    def contact_website_url(self, value):
        self.__contact_website_url = value

    @property
    def seller(self):
        """
        | Object containing seller details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.seller.Seller`
        """
        return self.__seller

    @seller.setter
    def seller(self, value):
        self.__seller = value

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
        dictionary = super(Merchant, self).to_dictionary()
        if self.contact_website_url is not None:
            dictionary['contactWebsiteUrl'] = self.contact_website_url
        if self.seller is not None:
            dictionary['seller'] = self.seller.to_dictionary()
        if self.website_url is not None:
            dictionary['websiteUrl'] = self.website_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(Merchant, self).from_dictionary(dictionary)
        if 'contactWebsiteUrl' in dictionary:
            self.contact_website_url = dictionary['contactWebsiteUrl']
        if 'seller' in dictionary:
            if not isinstance(dictionary['seller'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['seller']))
            value = Seller()
            self.seller = value.from_dictionary(dictionary['seller'])
        if 'websiteUrl' in dictionary:
            self.website_url = dictionary['websiteUrl']
        return self
