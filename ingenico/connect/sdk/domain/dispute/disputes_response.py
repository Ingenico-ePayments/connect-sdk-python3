# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.dispute.definitions.dispute import Dispute


class DisputesResponse(DataObject):

    __disputes = None

    @property
    def disputes(self):
        """
        | Array containing disputes and their characteristics.
        
        Type: list[:class:`ingenico.connect.sdk.domain.dispute.definitions.dispute.Dispute`]
        """
        return self.__disputes

    @disputes.setter
    def disputes(self, value):
        self.__disputes = value

    def to_dictionary(self):
        dictionary = super(DisputesResponse, self).to_dictionary()
        if self.disputes is not None:
            dictionary['disputes'] = []
            for element in self.disputes:
                if element is not None:
                    dictionary['disputes'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(DisputesResponse, self).from_dictionary(dictionary)
        if 'disputes' in dictionary:
            if not isinstance(dictionary['disputes'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['disputes']))
            self.disputes = []
            for element in dictionary['disputes']:
                value = Dispute()
                self.disputes.append(value.from_dictionary(element))
        return self
