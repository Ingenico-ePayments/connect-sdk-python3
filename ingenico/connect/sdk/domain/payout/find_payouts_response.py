# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payout.definitions.payout_result import PayoutResult


class FindPayoutsResponse(DataObject):

    __limit = None
    __offset = None
    __payouts = None
    __total_count = None

    @property
    def limit(self):
        """
        | The limit you used in the request.
        
        Type: int
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value

    @property
    def offset(self):
        """
        | The offset you used in the request.
        
        Type: int
        """
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = value

    @property
    def payouts(self):
        """
        | A list of payouts that matched your filter, starting at the given offset and limited to the given limit.
        
        Type: list[:class:`ingenico.connect.sdk.domain.payout.definitions.payout_result.PayoutResult`]
        """
        return self.__payouts

    @payouts.setter
    def payouts(self, value):
        self.__payouts = value

    @property
    def total_count(self):
        """
        | The total number of payouts that matched your filter.
        
        Type: int
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value

    def to_dictionary(self):
        dictionary = super(FindPayoutsResponse, self).to_dictionary()
        if self.limit is not None:
            dictionary['limit'] = self.limit
        if self.offset is not None:
            dictionary['offset'] = self.offset
        if self.payouts is not None:
            dictionary['payouts'] = []
            for element in self.payouts:
                if element is not None:
                    dictionary['payouts'].append(element.to_dictionary())
        if self.total_count is not None:
            dictionary['totalCount'] = self.total_count
        return dictionary

    def from_dictionary(self, dictionary):
        super(FindPayoutsResponse, self).from_dictionary(dictionary)
        if 'limit' in dictionary:
            self.limit = dictionary['limit']
        if 'offset' in dictionary:
            self.offset = dictionary['offset']
        if 'payouts' in dictionary:
            if not isinstance(dictionary['payouts'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['payouts']))
            self.payouts = []
            for element in dictionary['payouts']:
                value = PayoutResult()
                self.payouts.append(value.from_dictionary(element))
        if 'totalCount' in dictionary:
            self.total_count = dictionary['totalCount']
        return self
