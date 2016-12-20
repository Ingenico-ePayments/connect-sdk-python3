#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.account_on_file_attribute import AccountOnFileAttribute
from ingenico.connect.sdk.domain.product.definitions.account_on_file_display_hints import AccountOnFileDisplayHints


class AccountOnFile(DataObject):
    """
    Class AccountOnFile
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AccountOnFile
    """

    __attributes = None
    __display_hints = None
    __id = None
    __payment_product_id = None

    @property
    def attributes(self):
        """
        list[:class:`AccountOnFileAttribute`]
        """
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        self.__attributes = value

    @property
    def display_hints(self):
        """
        :class:`AccountOnFileDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def id(self):
        """
        int
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def payment_product_id(self):
        """
        int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(AccountOnFile, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'attributes', self.attributes)
        self._add_to_dictionary(dictionary, 'displayHints', self.display_hints)
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFile, self).from_dictionary(dictionary)
        if 'attributes' in dictionary:
            if not isinstance(dictionary['attributes'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['attributes']))
            self.attributes = []
            for attributes_element in dictionary['attributes']:
                attributes_value = AccountOnFileAttribute()
                self.attributes.append(attributes_value.from_dictionary(attributes_element))
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = AccountOnFileDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
