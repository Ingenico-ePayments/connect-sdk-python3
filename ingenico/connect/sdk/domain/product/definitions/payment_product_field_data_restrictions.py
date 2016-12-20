#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_validators import PaymentProductFieldValidators


class PaymentProductFieldDataRestrictions(DataObject):
    """
    Class PaymentProductFieldDataRestrictions
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductFieldDataRestrictions
    """

    __is_required = None
    __validators = None

    @property
    def is_required(self):
        """
        bool
        """
        return self.__is_required

    @is_required.setter
    def is_required(self, value):
        self.__is_required = value

    @property
    def validators(self):
        """
        :class:`PaymentProductFieldValidators`
        """
        return self.__validators

    @validators.setter
    def validators(self, value):
        self.__validators = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldDataRestrictions, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'isRequired', self.is_required)
        self._add_to_dictionary(dictionary, 'validators', self.validators)
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
