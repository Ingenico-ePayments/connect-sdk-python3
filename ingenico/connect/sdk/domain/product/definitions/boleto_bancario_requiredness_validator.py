# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class BoletoBancarioRequirednessValidator(DataObject):

    __fiscal_number_length = None

    @property
    def fiscal_number_length(self):
        """
        | When performing a payment with Boleto Bancario, some values are only required when the fiscalnumber has a specific length. The length the fiscalnumber has to have to make the field required is defined here.
        | For example the CompanyName is required when the fiscalnumber is a CNPJ. The firstname and surname are required when the fiscalnumber is a CPF.
        
        Type: int
        """
        return self.__fiscal_number_length

    @fiscal_number_length.setter
    def fiscal_number_length(self, value):
        self.__fiscal_number_length = value

    def to_dictionary(self):
        dictionary = super(BoletoBancarioRequirednessValidator, self).to_dictionary()
        if self.fiscal_number_length is not None:
            dictionary['fiscalNumberLength'] = self.fiscal_number_length
        return dictionary

    def from_dictionary(self, dictionary):
        super(BoletoBancarioRequirednessValidator, self).from_dictionary(dictionary)
        if 'fiscalNumberLength' in dictionary:
            self.fiscal_number_length = dictionary['fiscalNumberLength']
        return self
