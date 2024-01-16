# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.installments.definitions.installment_options import InstallmentOptions


class InstallmentOptionsResponse(DataObject):
    """
    | The response contains the details of the installment options
    """

    __installment_options = None

    @property
    def installment_options(self):
        """
        | Array containing installment options their details and characteristics
        
        Type: list[:class:`ingenico.connect.sdk.domain.installments.definitions.installment_options.InstallmentOptions`]
        """
        return self.__installment_options

    @installment_options.setter
    def installment_options(self, value):
        self.__installment_options = value

    def to_dictionary(self):
        dictionary = super(InstallmentOptionsResponse, self).to_dictionary()
        if self.installment_options is not None:
            dictionary['installmentOptions'] = []
            for element in self.installment_options:
                if element is not None:
                    dictionary['installmentOptions'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(InstallmentOptionsResponse, self).from_dictionary(dictionary)
        if 'installmentOptions' in dictionary:
            if not isinstance(dictionary['installmentOptions'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['installmentOptions']))
            self.installment_options = []
            for element in dictionary['installmentOptions']:
                value = InstallmentOptions()
                self.installment_options.append(value.from_dictionary(element))
        return self
