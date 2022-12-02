# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.seller import Seller


class Merchant(DataObject):

    __configuration_id = None
    __contact_website_url = None
    __seller = None
    __website_url = None

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
        if self.configuration_id is not None:
            dictionary['configurationId'] = self.configuration_id
        if self.contact_website_url is not None:
            dictionary['contactWebsiteUrl'] = self.contact_website_url
        if self.seller is not None:
            dictionary['seller'] = self.seller.to_dictionary()
        if self.website_url is not None:
            dictionary['websiteUrl'] = self.website_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(Merchant, self).from_dictionary(dictionary)
        if 'configurationId' in dictionary:
            self.configuration_id = dictionary['configurationId']
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
