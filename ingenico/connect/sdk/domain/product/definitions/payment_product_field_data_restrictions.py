# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_validators import PaymentProductFieldValidators


class PaymentProductFieldDataRestrictions(DataObject):

    __is_required = None
    __validators = None

    @property
    def is_required(self):
        """
        * true - Indicates that this field is required
        * false - Indicates that this field is optional
        
        Type: bool
        """
        return self.__is_required

    @is_required.setter
    def is_required(self, value):
        self.__is_required = value

    @property
    def validators(self):
        """
        | Object containing the details of the validations on the field
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product_field_validators.PaymentProductFieldValidators`
        """
        return self.__validators

    @validators.setter
    def validators(self, value):
        self.__validators = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldDataRestrictions, self).to_dictionary()
        if self.is_required is not None:
            dictionary['isRequired'] = self.is_required
        if self.validators is not None:
            dictionary['validators'] = self.validators.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldDataRestrictions, self).from_dictionary(dictionary)
        if 'isRequired' in dictionary:
            self.is_required = dictionary['isRequired']
        if 'validators' in dictionary:
            if not isinstance(dictionary['validators'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['validators']))
            value = PaymentProductFieldValidators()
            self.validators = value.from_dictionary(dictionary['validators'])
        return self
