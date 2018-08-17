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
        self._add_to_dictionary(dictionary, 'refunds', self.refunds)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundsResponse, self).from_dictionary(dictionary)
        if 'refunds' in dictionary:
            if not isinstance(dictionary['refunds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['refunds']))
            self.refunds = []
            for refunds_element in dictionary['refunds']:
                refunds_value = RefundResult()
                self.refunds.append(refunds_value.from_dictionary(refunds_element))
        return self
