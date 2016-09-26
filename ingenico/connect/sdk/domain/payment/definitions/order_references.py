#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.order_invoice_data import OrderInvoiceData


class OrderReferences(DataObject):
    """
    Class OrderReferences
    See also https://developer.globalcollect.com/documentation/api/server/#schema_OrderReferences
    
    Attributes:
        descriptor:          str
        invoice_data:        :class:`OrderInvoiceData`
        merchant_order_id:   int
        merchant_reference:  str
     """

    descriptor = None
    invoice_data = None
    merchant_order_id = None
    merchant_reference = None

    def to_dictionary(self):
        dictionary = super(OrderReferences, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'descriptor', self.descriptor)
        self._add_to_dictionary(dictionary, 'invoiceData', self.invoice_data)
        self._add_to_dictionary(dictionary, 'merchantOrderId', self.merchant_order_id)
        self._add_to_dictionary(dictionary, 'merchantReference', self.merchant_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderReferences, self).from_dictionary(dictionary)
        if 'descriptor' in dictionary:
            self.descriptor = dictionary['descriptor']
        if 'invoiceData' in dictionary:
            if not isinstance(dictionary['invoiceData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['invoiceData']))
            value = OrderInvoiceData()
            self.invoice_data = value.from_dictionary(dictionary['invoiceData'])
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
