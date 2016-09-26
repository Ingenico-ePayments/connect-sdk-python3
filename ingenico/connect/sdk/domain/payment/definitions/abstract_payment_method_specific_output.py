#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class AbstractPaymentMethodSpecificOutput(DataObject):
    """
    Class AbstractPaymentMethodSpecificOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AbstractPaymentMethodSpecificOutput
    
    Attributes:
        payment_product_id:  int
     """

    payment_product_id = None

    def to_dictionary(self):
        dictionary = super(AbstractPaymentMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
