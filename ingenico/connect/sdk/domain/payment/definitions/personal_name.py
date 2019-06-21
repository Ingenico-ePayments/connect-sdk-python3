# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.personal_name_base import PersonalNameBase


class PersonalName(PersonalNameBase):

    __title = None

    @property
    def title(self):
        """
        | Title of customer
        
        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def to_dictionary(self):
        dictionary = super(PersonalName, self).to_dictionary()
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalName, self).from_dictionary(dictionary)
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
