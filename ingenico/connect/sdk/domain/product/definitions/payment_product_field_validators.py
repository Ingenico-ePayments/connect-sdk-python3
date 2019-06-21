# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.boleto_bancario_requiredness_validator import BoletoBancarioRequirednessValidator
from ingenico.connect.sdk.domain.product.definitions.empty_validator import EmptyValidator
from ingenico.connect.sdk.domain.product.definitions.fixed_list_validator import FixedListValidator
from ingenico.connect.sdk.domain.product.definitions.length_validator import LengthValidator
from ingenico.connect.sdk.domain.product.definitions.range_validator import RangeValidator
from ingenico.connect.sdk.domain.product.definitions.regular_expression_validator import RegularExpressionValidator


class PaymentProductFieldValidators(DataObject):

    __boleto_bancario_requiredness = None
    __email_address = None
    __expiration_date = None
    __fixed_list = None
    __iban = None
    __length = None
    __luhn = None
    __range = None
    __regular_expression = None
    __terms_and_conditions = None

    @property
    def boleto_bancario_requiredness(self):
        """
        | Indicates the requiredness of the field based on the fiscalnumber for Boleto Bancario
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.boleto_bancario_requiredness_validator.BoletoBancarioRequirednessValidator`
        """
        return self.__boleto_bancario_requiredness

    @boleto_bancario_requiredness.setter
    def boleto_bancario_requiredness(self, value):
        self.__boleto_bancario_requiredness = value

    @property
    def email_address(self):
        """
        | Indicates that the content should be validated against the rules for an email address
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.empty_validator.EmptyValidator`
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def expiration_date(self):
        """
        | Indicates that the content should be validated against the rules for an expiration date (it should be in the future)
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.empty_validator.EmptyValidator`
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self.__expiration_date = value

    @property
    def fixed_list(self):
        """
        | Indicates that content should be one of the, in this object, listed items
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.fixed_list_validator.FixedListValidator`
        """
        return self.__fixed_list

    @fixed_list.setter
    def fixed_list(self, value):
        self.__fixed_list = value

    @property
    def iban(self):
        """
        | Indicates that the content of this (iban) field needs to validated against format checks and modulo check (as described in ISO 7064)
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.empty_validator.EmptyValidator`
        """
        return self.__iban

    @iban.setter
    def iban(self, value):
        self.__iban = value

    @property
    def length(self):
        """
        | Indicates that the content needs to be validated against length criteria defined in this object
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.length_validator.LengthValidator`
        """
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def luhn(self):
        """
        | Indicates that the content needs to be validated using a LUHN check
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.empty_validator.EmptyValidator`
        """
        return self.__luhn

    @luhn.setter
    def luhn(self, value):
        self.__luhn = value

    @property
    def range(self):
        """
        | Indicates that the content needs to be validated against a, in this object, defined range
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.range_validator.RangeValidator`
        """
        return self.__range

    @range.setter
    def range(self, value):
        self.__range = value

    @property
    def regular_expression(self):
        """
        | A string representing the regular expression to check
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.regular_expression_validator.RegularExpressionValidator`
        """
        return self.__regular_expression

    @regular_expression.setter
    def regular_expression(self, value):
        self.__regular_expression = value

    @property
    def terms_and_conditions(self):
        """
        | Indicates that the content should be validated as such that the customer has accepted the field as if they were terms and conditions of a service
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.empty_validator.EmptyValidator`
        """
        return self.__terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, value):
        self.__terms_and_conditions = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldValidators, self).to_dictionary()
        if self.boleto_bancario_requiredness is not None:
            dictionary['boletoBancarioRequiredness'] = self.boleto_bancario_requiredness.to_dictionary()
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address.to_dictionary()
        if self.expiration_date is not None:
            dictionary['expirationDate'] = self.expiration_date.to_dictionary()
        if self.fixed_list is not None:
            dictionary['fixedList'] = self.fixed_list.to_dictionary()
        if self.iban is not None:
            dictionary['iban'] = self.iban.to_dictionary()
        if self.length is not None:
            dictionary['length'] = self.length.to_dictionary()
        if self.luhn is not None:
            dictionary['luhn'] = self.luhn.to_dictionary()
        if self.range is not None:
            dictionary['range'] = self.range.to_dictionary()
        if self.regular_expression is not None:
            dictionary['regularExpression'] = self.regular_expression.to_dictionary()
        if self.terms_and_conditions is not None:
            dictionary['termsAndConditions'] = self.terms_and_conditions.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldValidators, self).from_dictionary(dictionary)
        if 'boletoBancarioRequiredness' in dictionary:
            if not isinstance(dictionary['boletoBancarioRequiredness'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['boletoBancarioRequiredness']))
            value = BoletoBancarioRequirednessValidator()
            self.boleto_bancario_requiredness = value.from_dictionary(dictionary['boletoBancarioRequiredness'])
        if 'emailAddress' in dictionary:
            if not isinstance(dictionary['emailAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['emailAddress']))
            value = EmptyValidator()
            self.email_address = value.from_dictionary(dictionary['emailAddress'])
        if 'expirationDate' in dictionary:
            if not isinstance(dictionary['expirationDate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['expirationDate']))
            value = EmptyValidator()
            self.expiration_date = value.from_dictionary(dictionary['expirationDate'])
        if 'fixedList' in dictionary:
            if not isinstance(dictionary['fixedList'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fixedList']))
            value = FixedListValidator()
            self.fixed_list = value.from_dictionary(dictionary['fixedList'])
        if 'iban' in dictionary:
            if not isinstance(dictionary['iban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['iban']))
            value = EmptyValidator()
            self.iban = value.from_dictionary(dictionary['iban'])
        if 'length' in dictionary:
            if not isinstance(dictionary['length'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['length']))
            value = LengthValidator()
            self.length = value.from_dictionary(dictionary['length'])
        if 'luhn' in dictionary:
            if not isinstance(dictionary['luhn'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['luhn']))
            value = EmptyValidator()
            self.luhn = value.from_dictionary(dictionary['luhn'])
        if 'range' in dictionary:
            if not isinstance(dictionary['range'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['range']))
            value = RangeValidator()
            self.range = value.from_dictionary(dictionary['range'])
        if 'regularExpression' in dictionary:
            if not isinstance(dictionary['regularExpression'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['regularExpression']))
            value = RegularExpressionValidator()
            self.regular_expression = value.from_dictionary(dictionary['regularExpression'])
        if 'termsAndConditions' in dictionary:
            if not isinstance(dictionary['termsAndConditions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['termsAndConditions']))
            value = EmptyValidator()
            self.terms_and_conditions = value.from_dictionary(dictionary['termsAndConditions'])
        return self
