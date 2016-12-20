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
    """

    __email_address = None
    __expiration_date = None
    __fixed_list = None
    __length = None
    __luhn = None
    __range = None
    __regular_expression = None

    @property
    def email_address(self):
        """
        :class:`EmptyValidator`
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def expiration_date(self):
        """
        :class:`EmptyValidator`
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self.__expiration_date = value

    @property
    def fixed_list(self):
        """
        :class:`FixedListValidator`
        """
        return self.__fixed_list

    @fixed_list.setter
    def fixed_list(self, value):
        self.__fixed_list = value

    @property
    def length(self):
        """
        :class:`LengthValidator`
        """
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def luhn(self):
        """
        :class:`EmptyValidator`
        """
        return self.__luhn

    @luhn.setter
    def luhn(self, value):
        self.__luhn = value

    @property
    def range(self):
        """
        :class:`RangeValidator`
        """
        return self.__range

    @range.setter
    def range(self, value):
        self.__range = value

    @property
    def regular_expression(self):
        """
        :class:`RegularExpressionValidator`
        """
        return self.__regular_expression

    @regular_expression.setter
    def regular_expression(self, value):
        self.__regular_expression = value

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
