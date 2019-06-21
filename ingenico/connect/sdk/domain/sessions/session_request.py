# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.sessions.definitions.payment_product_filters_client_session import PaymentProductFiltersClientSession


class SessionRequest(DataObject):

    __payment_product_filters = None
    __tokens = None

    @property
    def payment_product_filters(self):
        """
        | Restrict the payment products available for payment completion by restricting to and excluding certain payment products and payment product groups.
        
        Type: :class:`ingenico.connect.sdk.domain.sessions.definitions.payment_product_filters_client_session.PaymentProductFiltersClientSession`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value):
        self.__payment_product_filters = value

    @property
    def tokens(self):
        """
        | List of previously stored tokens linked to the customer that wants to checkout.
        
        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value):
        self.__tokens = value

    def to_dictionary(self):
        dictionary = super(SessionRequest, self).to_dictionary()
        if self.payment_product_filters is not None:
            dictionary['paymentProductFilters'] = self.payment_product_filters.to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SessionRequest, self).from_dictionary(dictionary)
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersClientSession()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                self.tokens.append(element)
        return self
