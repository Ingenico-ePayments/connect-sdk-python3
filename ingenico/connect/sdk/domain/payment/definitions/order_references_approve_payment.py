#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class OrderReferencesApprovePayment(DataObject):
    """
    Class OrderReferencesApprovePayment
    See also https://developer.globalcollect.com/documentation/api/server/#schema_OrderReferencesApprovePayment
    
    Attributes:
        merchant_reference:  str
     """

    merchant_reference = None

    def to_dictionary(self):
        dictionary = super(OrderReferencesApprovePayment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'merchantReference', self.merchant_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderReferencesApprovePayment, self).from_dictionary(dictionary)
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
