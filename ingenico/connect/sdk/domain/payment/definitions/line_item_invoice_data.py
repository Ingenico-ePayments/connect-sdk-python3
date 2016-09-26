#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class LineItemInvoiceData(DataObject):
    """
    Class LineItemInvoiceData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_LineItemInvoiceData
    
    Attributes:
        description:          str
        merchant_linenumber:  str
        merchant_pagenumber:  str
        nr_of_items:          str
        price_per_item:       int
     """

    description = None
    merchant_linenumber = None
    merchant_pagenumber = None
    nr_of_items = None
    price_per_item = None

    def to_dictionary(self):
        dictionary = super(LineItemInvoiceData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'description', self.description)
        self._add_to_dictionary(dictionary, 'merchantLinenumber', self.merchant_linenumber)
        self._add_to_dictionary(dictionary, 'merchantPagenumber', self.merchant_pagenumber)
        self._add_to_dictionary(dictionary, 'nrOfItems', self.nr_of_items)
        self._add_to_dictionary(dictionary, 'pricePerItem', self.price_per_item)
        return dictionary

    def from_dictionary(self, dictionary):
        super(LineItemInvoiceData, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'merchantLinenumber' in dictionary:
            self.merchant_linenumber = dictionary['merchantLinenumber']
        if 'merchantPagenumber' in dictionary:
            self.merchant_pagenumber = dictionary['merchantPagenumber']
        if 'nrOfItems' in dictionary:
            self.nr_of_items = dictionary['nrOfItems']
        if 'pricePerItem' in dictionary:
            self.price_per_item = dictionary['pricePerItem']
        return self
