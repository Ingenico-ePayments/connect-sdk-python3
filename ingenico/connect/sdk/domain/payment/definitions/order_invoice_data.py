#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class OrderInvoiceData(DataObject):
    """
    Class OrderInvoiceData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_OrderInvoiceData
    
    Attributes:
        additional_data:  str
        invoice_date:     str
        invoice_number:   str
        text_qualifiers:  list[str]
     """

    additional_data = None
    invoice_date = None
    invoice_number = None
    text_qualifiers = None

    def to_dictionary(self):
        dictionary = super(OrderInvoiceData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalData', self.additional_data)
        self._add_to_dictionary(dictionary, 'invoiceDate', self.invoice_date)
        self._add_to_dictionary(dictionary, 'invoiceNumber', self.invoice_number)
        self._add_to_dictionary(dictionary, 'textQualifiers', self.text_qualifiers)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderInvoiceData, self).from_dictionary(dictionary)
        if 'additionalData' in dictionary:
            self.additional_data = dictionary['additionalData']
        if 'invoiceDate' in dictionary:
            self.invoice_date = dictionary['invoiceDate']
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'textQualifiers' in dictionary:
            if not isinstance(dictionary['textQualifiers'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['textQualifiers']))
            self.text_qualifiers = []
            for textQualifiers_element in dictionary['textQualifiers']:
                self.text_qualifiers.append(textQualifiers_element)
        return self
