#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProductFilter(DataObject):
    """
    Class PaymentProductFilter
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductFilter
    """

    __groups = None
    __products = None

    @property
    def groups(self):
        """
        list[str]
        """
        return self.__groups

    @groups.setter
    def groups(self, value):
        self.__groups = value

    @property
    def products(self):
        """
        list[int]
        """
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFilter, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'groups', self.groups)
        self._add_to_dictionary(dictionary, 'products', self.products)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFilter, self).from_dictionary(dictionary)
        if 'groups' in dictionary:
            if not isinstance(dictionary['groups'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['groups']))
            self.groups = []
            for groups_element in dictionary['groups']:
                self.groups.append(groups_element)
        if 'products' in dictionary:
            if not isinstance(dictionary['products'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['products']))
            self.products = []
            for products_element in dictionary['products']:
                self.products.append(products_element)
        return self
