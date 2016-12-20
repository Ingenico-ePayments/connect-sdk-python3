#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class AbstractPaymentMethodSpecificInput(DataObject):
    """
    Class AbstractPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AbstractPaymentMethodSpecificInput
    """

    __payment_product_id = None

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
        dictionary = super(AbstractPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
