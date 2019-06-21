# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ProtectionEligibility(DataObject):

    __eligibility = None
    __type = None

    @property
    def eligibility(self):
        """
        | Possible values: 
        |  
        *  Eligible 
        *  PartiallyEligible 
        *  Ineligible
        
        Type: str
        """
        return self.__eligibility

    @eligibility.setter
    def eligibility(self, value):
        self.__eligibility = value

    @property
    def type(self):
        """
        | Possible values: 
        |  
        *  ItemNotReceivedEligible 
        *  UnauthorizedPaymentEligible 
        *  Ineligible
        
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(ProtectionEligibility, self).to_dictionary()
        if self.eligibility is not None:
            dictionary['eligibility'] = self.eligibility
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary):
        super(ProtectionEligibility, self).from_dictionary(dictionary)
        if 'eligibility' in dictionary:
            self.eligibility = dictionary['eligibility']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
