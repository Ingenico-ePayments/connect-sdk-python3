# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_group import PaymentProductGroup


class PaymentProductGroups(DataObject):

    __payment_product_groups = None

    @property
    def payment_product_groups(self):
        """
        | Array containing payment product groups and their characteristics
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.payment_product_group.PaymentProductGroup`]
        """
        return self.__payment_product_groups

    @payment_product_groups.setter
    def payment_product_groups(self, value):
        self.__payment_product_groups = value

    def to_dictionary(self):
        dictionary = super(PaymentProductGroups, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProductGroups', self.payment_product_groups)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductGroups, self).from_dictionary(dictionary)
        if 'paymentProductGroups' in dictionary:
            if not isinstance(dictionary['paymentProductGroups'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductGroups']))
            self.payment_product_groups = []
            for paymentProductGroups_element in dictionary['paymentProductGroups']:
                paymentProductGroups_value = PaymentProductGroup()
                self.payment_product_groups.append(paymentProductGroups_value.from_dictionary(paymentProductGroups_element))
        return self
