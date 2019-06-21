# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.refund.definitions.refund_result import RefundResult


class RefundsResponse(DataObject):

    __refunds = None

    @property
    def refunds(self):
        """
        | The list of all refunds performed on the requested payment.
        
        Type: list[:class:`ingenico.connect.sdk.domain.refund.definitions.refund_result.RefundResult`]
        """
        return self.__refunds

    @refunds.setter
    def refunds(self, value):
        self.__refunds = value

    def to_dictionary(self):
        dictionary = super(RefundsResponse, self).to_dictionary()
        if self.refunds is not None:
            dictionary['refunds'] = []
            for element in self.refunds:
                if element is not None:
                    dictionary['refunds'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundsResponse, self).from_dictionary(dictionary)
        if 'refunds' in dictionary:
            if not isinstance(dictionary['refunds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['refunds']))
            self.refunds = []
            for element in dictionary['refunds']:
                value = RefundResult()
                self.refunds.append(value.from_dictionary(element))
        return self
