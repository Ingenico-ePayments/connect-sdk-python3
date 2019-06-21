# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.payment_product_filter import PaymentProductFilter


class PaymentProductFiltersClientSession(DataObject):

    __exclude = None
    __restrict_to = None

    @property
    def exclude(self):
        """
        | Contains the payment product ids and payment product groups that should be excluded from the payment products available for the payment. Note that excluding a payment product will ensure exclusion, even if the payment product is also present in the restrictTo filter, and that excluding a payment product group will exclude all payment products that are a part of that group, even if one or more of them are present in the restrictTo filters.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.payment_product_filter.PaymentProductFilter`
        """
        return self.__exclude

    @exclude.setter
    def exclude(self, value):
        self.__exclude = value

    @property
    def restrict_to(self):
        """
        | Contains the payment product ids and payment product groups that should be at most contained in the payment products available for completing the payment. Note that the list of payment products available for completing the payment will only contain payment products present in these filters, but not all payment products in these filters might be present in the list. Some of them might not be allowed in context or they might be present in the exclude filters.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.payment_product_filter.PaymentProductFilter`
        """
        return self.__restrict_to

    @restrict_to.setter
    def restrict_to(self, value):
        self.__restrict_to = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFiltersClientSession, self).to_dictionary()
        if self.exclude is not None:
            dictionary['exclude'] = self.exclude.to_dictionary()
        if self.restrict_to is not None:
            dictionary['restrictTo'] = self.restrict_to.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFiltersClientSession, self).from_dictionary(dictionary)
        if 'exclude' in dictionary:
            if not isinstance(dictionary['exclude'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['exclude']))
            value = PaymentProductFilter()
            self.exclude = value.from_dictionary(dictionary['exclude'])
        if 'restrictTo' in dictionary:
            if not isinstance(dictionary['restrictTo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['restrictTo']))
            value = PaymentProductFilter()
            self.restrict_to = value.from_dictionary(dictionary['restrictTo'])
        return self
