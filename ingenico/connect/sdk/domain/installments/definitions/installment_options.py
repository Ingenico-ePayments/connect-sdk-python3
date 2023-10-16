# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.installments.definitions.installment_display_hints import InstallmentDisplayHints
from ingenico.connect.sdk.domain.payment.definitions.installments import Installments


class InstallmentOptions(DataObject):
    """
    | Array containing installment options their details and characteristics
    """

    __display_hints = None
    __id = None
    __installment_plans = None

    @property
    def display_hints(self):
        """
        | Object containing information for the client on how best to display the installment options
        
        Type: :class:`ingenico.connect.sdk.domain.installments.definitions.installment_display_hints.InstallmentDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def id(self):
        """
        | The ID of the installment option in our system
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def installment_plans(self):
        """
        | Object containing information about installment plans
        
        Type: list[:class:`ingenico.connect.sdk.domain.payment.definitions.installments.Installments`]
        """
        return self.__installment_plans

    @installment_plans.setter
    def installment_plans(self, value):
        self.__installment_plans = value

    def to_dictionary(self):
        dictionary = super(InstallmentOptions, self).to_dictionary()
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.installment_plans is not None:
            dictionary['installmentPlans'] = []
            for element in self.installment_plans:
                if element is not None:
                    dictionary['installmentPlans'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(InstallmentOptions, self).from_dictionary(dictionary)
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = InstallmentDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'installmentPlans' in dictionary:
            if not isinstance(dictionary['installmentPlans'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['installmentPlans']))
            self.installment_plans = []
            for element in dictionary['installmentPlans']:
                value = Installments()
                self.installment_plans.append(value.from_dictionary(element))
        return self
