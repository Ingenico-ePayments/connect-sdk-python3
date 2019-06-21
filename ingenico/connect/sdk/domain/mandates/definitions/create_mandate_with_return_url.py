# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.mandates.definitions.create_mandate_base import CreateMandateBase


class CreateMandateWithReturnUrl(CreateMandateBase):

    __return_url = None

    @property
    def return_url(self):
        """
        | Return URL to use if the mandate signing requires redirection.
        
        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    def to_dictionary(self):
        dictionary = super(CreateMandateWithReturnUrl, self).to_dictionary()
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateMandateWithReturnUrl, self).from_dictionary(dictionary)
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        return self
