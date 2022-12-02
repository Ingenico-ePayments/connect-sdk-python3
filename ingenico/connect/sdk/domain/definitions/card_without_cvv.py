# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card_essentials import CardEssentials


class CardWithoutCvv(CardEssentials):

    __issue_number = None

    @property
    def issue_number(self):
        """
        | Issue number on the card (if applicable)
        
        Type: str
        """
        return self.__issue_number

    @issue_number.setter
    def issue_number(self, value):
        self.__issue_number = value

    def to_dictionary(self):
        dictionary = super(CardWithoutCvv, self).to_dictionary()
        if self.issue_number is not None:
            dictionary['issueNumber'] = self.issue_number
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardWithoutCvv, self).from_dictionary(dictionary)
        if 'issueNumber' in dictionary:
            self.issue_number = dictionary['issueNumber']
        return self
