#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_group import PaymentProductGroup


class PaymentProductGroups(DataObject):
    """
    Class PaymentProductGroups
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductGroups
    """

    __payment_product_groups = None

    @property
    def payment_product_groups(self):
        """
        list[:class:`PaymentProductGroup`]
        """
        return self.__payment_product_groups

    @payment_product_groups.setter
    def payment_product_groups(self, value):
        self.__payment_product_groups = value

    def to_dictionary(self):
        dictionary = super(PaymentProductGroups, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProductGroups', self.payment_product_groups)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductGroups, self).from_dictionary(dictionary)
        if 'paymentProductGroups' in dictionary:
            if not isinstance(dictionary['paymentProductGroups'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductGroups']))
            self.payment_product_groups = []
            for paymentProductGroups_element in dictionary['paymentProductGroups']:
                paymentProductGroups_value = PaymentProductGroup()
                self.payment_product_groups.append(paymentProductGroups_value.from_dictionary(paymentProductGroups_element))
        return self
