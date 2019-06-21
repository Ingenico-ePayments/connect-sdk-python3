# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class AbstractRedirectPaymentProduct840SpecificInput(DataObject):

    __address_selection_at_pay_pal = None

    @property
    def address_selection_at_pay_pal(self):
        """
        Type: bool
        """
        return self.__address_selection_at_pay_pal

    @address_selection_at_pay_pal.setter
    def address_selection_at_pay_pal(self, value):
        self.__address_selection_at_pay_pal = value

    def to_dictionary(self):
        dictionary = super(AbstractRedirectPaymentProduct840SpecificInput, self).to_dictionary()
        if self.address_selection_at_pay_pal is not None:
            dictionary['addressSelectionAtPayPal'] = self.address_selection_at_pay_pal
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractRedirectPaymentProduct840SpecificInput, self).from_dictionary(dictionary)
        if 'addressSelectionAtPayPal' in dictionary:
            self.address_selection_at_pay_pal = dictionary['addressSelectionAtPayPal']
        return self
