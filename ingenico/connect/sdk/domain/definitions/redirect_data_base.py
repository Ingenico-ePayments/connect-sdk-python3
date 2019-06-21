# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectDataBase(DataObject):

    __returnmac = None
    __redirect_url = None

    @property
    def returnmac(self):
        """
        Type: str
        """
        return self.__returnmac

    @returnmac.setter
    def returnmac(self, value):
        self.__returnmac = value

    @property
    def redirect_url(self):
        """
        Type: str
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value

    def to_dictionary(self):
        dictionary = super(RedirectDataBase, self).to_dictionary()
        if self.returnmac is not None:
            dictionary['RETURNMAC'] = self.returnmac
        if self.redirect_url is not None:
            dictionary['redirectURL'] = self.redirect_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectDataBase, self).from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'redirectURL' in dictionary:
            self.redirect_url = dictionary['redirectURL']
        return self
