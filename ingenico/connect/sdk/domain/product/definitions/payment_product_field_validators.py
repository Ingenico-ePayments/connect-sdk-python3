#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.empty_validator import EmptyValidator
from ingenico.connect.sdk.domain.product.definitions.fixed_list_validator import FixedListValidator
from ingenico.connect.sdk.domain.product.definitions.length_validator import LengthValidator
from ingenico.connect.sdk.domain.product.definitions.range_validator import RangeValidator
from ingenico.connect.sdk.domain.product.definitions.regular_expression_validator import RegularExpressionValidator


class PaymentProductFieldValidators(DataObject):
    """
    Class PaymentProductFieldValidators
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductFieldValidators
    
    Attributes:
        email_address:       :class:`EmptyValidator`
        expiration_date:     :class:`EmptyValidator`
        fixed_list:          :class:`FixedListValidator`
        length:              :class:`LengthValidator`
        luhn:                :class:`EmptyValidator`
        range:               :class:`RangeValidator`
        regular_expression:  :class:`RegularExpressionValidator`
     """

    email_address = None
    expiration_date = None
    fixed_list = None
    length = None
    luhn = None
    range = None
    regular_expression = None

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldValidators, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'emailAddress', self.email_address)
        self._add_to_dictionary(dictionary, 'expirationDate', self.expiration_date)
        self._add_to_dictionary(dictionary, 'fixedList', self.fixed_list)
        self._add_to_dictionary(dictionary, 'length', self.length)
        self._add_to_dictionary(dictionary, 'luhn', self.luhn)
        self._add_to_dictionary(dictionary, 'range', self.range)
        self._add_to_dictionary(dictionary, 'regularExpression', self.regular_expression)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldValidators, self).from_dictionary(dictionary)
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
        return self
