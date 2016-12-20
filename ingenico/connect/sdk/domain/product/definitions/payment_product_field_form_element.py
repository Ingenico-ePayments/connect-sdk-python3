#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.value_mapping_element import ValueMappingElement


class PaymentProductFieldFormElement(DataObject):
    """
    Class PaymentProductFieldFormElement
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductFieldFormElement
    """

    __type = None
    __value_mapping = None

    @property
    def type(self):
        """
        str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def value_mapping(self):
        """
        list[:class:`ValueMappingElement`]
        """
        return self.__value_mapping

    @value_mapping.setter
    def value_mapping(self, value):
        self.__value_mapping = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldFormElement, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'type', self.type)
        self._add_to_dictionary(dictionary, 'valueMapping', self.value_mapping)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldFormElement, self).from_dictionary(dictionary)
        if 'type' in dictionary:
            self.type = dictionary['type']
        if 'valueMapping' in dictionary:
            if not isinstance(dictionary['valueMapping'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['valueMapping']))
            self.value_mapping = []
            for valueMapping_element in dictionary['valueMapping']:
                valueMapping_value = ValueMappingElement()
                self.value_mapping.append(valueMapping_value.from_dictionary(valueMapping_element))
        return self
