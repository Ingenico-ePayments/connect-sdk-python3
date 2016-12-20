#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_data_restrictions import PaymentProductFieldDataRestrictions
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_display_hints import PaymentProductFieldDisplayHints


class PaymentProductField(DataObject):
    """
    Class PaymentProductField
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductField
    """

    __data_restrictions = None
    __display_hints = None
    __id = None
    __type = None

    @property
    def data_restrictions(self):
        """
        :class:`PaymentProductFieldDataRestrictions`
        """
        return self.__data_restrictions

    @data_restrictions.setter
    def data_restrictions(self, value):
        self.__data_restrictions = value

    @property
    def display_hints(self):
        """
        :class:`PaymentProductFieldDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def id(self):
        """
        str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def type(self):
        """
        str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(PaymentProductField, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dataRestrictions', self.data_restrictions)
        self._add_to_dictionary(dictionary, 'displayHints', self.display_hints)
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'type', self.type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductField, self).from_dictionary(dictionary)
        if 'dataRestrictions' in dictionary:
            if not isinstance(dictionary['dataRestrictions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['dataRestrictions']))
            value = PaymentProductFieldDataRestrictions()
            self.data_restrictions = value.from_dictionary(dictionary['dataRestrictions'])
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductFieldDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
