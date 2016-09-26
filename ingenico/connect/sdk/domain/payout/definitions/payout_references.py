#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PayoutReferences(DataObject):
    """
    Class PayoutReferences
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PayoutReferences
    
    Attributes:
        invoice_number:      str
        merchant_order_id:   int
        merchant_reference:  str
     """

    invoice_number = None
    merchant_order_id = None
    merchant_reference = None

    def to_dictionary(self):
        dictionary = super(PayoutReferences, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'invoiceNumber', self.invoice_number)
        self._add_to_dictionary(dictionary, 'merchantOrderId', self.merchant_order_id)
        self._add_to_dictionary(dictionary, 'merchantReference', self.merchant_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutReferences, self).from_dictionary(dictionary)
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
