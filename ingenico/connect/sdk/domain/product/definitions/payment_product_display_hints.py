#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProductDisplayHints(DataObject):
    """
    Class PaymentProductDisplayHints
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductDisplayHints
    """

    __display_order = None
    __label = None
    __logo = None

    @property
    def display_order(self):
        """
        int
        """
        return self.__display_order

    @display_order.setter
    def display_order(self, value):
        self.__display_order = value

    @property
    def label(self):
        """
        str
        """
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value

    @property
    def logo(self):
        """
        str
        """
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value

    def to_dictionary(self):
        dictionary = super(PaymentProductDisplayHints, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'displayOrder', self.display_order)
        self._add_to_dictionary(dictionary, 'label', self.label)
        self._add_to_dictionary(dictionary, 'logo', self.logo)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductDisplayHints, self).from_dictionary(dictionary)
        if 'displayOrder' in dictionary:
            self.display_order = dictionary['displayOrder']
        if 'label' in dictionary:
            self.label = dictionary['label']
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
