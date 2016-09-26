#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class LineItemLevel3InterchangeInformation(DataObject):
    """
    Class LineItemLevel3InterchangeInformation
    See also https://developer.globalcollect.com/documentation/api/server/#schema_LineItemLevel3InterchangeInformation
    
    Attributes:
        discount_amount:    int
        line_amount_total:  int
        product_code:       str
        product_price:      int
        product_type:       str
        quantity:           int
        tax_amount:         int
        unit:               str
     """

    discount_amount = None
    line_amount_total = None
    product_code = None
    product_price = None
    product_type = None
    quantity = None
    tax_amount = None
    unit = None

    def to_dictionary(self):
        dictionary = super(LineItemLevel3InterchangeInformation, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'discountAmount', self.discount_amount)
        self._add_to_dictionary(dictionary, 'lineAmountTotal', self.line_amount_total)
        self._add_to_dictionary(dictionary, 'productCode', self.product_code)
        self._add_to_dictionary(dictionary, 'productPrice', self.product_price)
        self._add_to_dictionary(dictionary, 'productType', self.product_type)
        self._add_to_dictionary(dictionary, 'quantity', self.quantity)
        self._add_to_dictionary(dictionary, 'taxAmount', self.tax_amount)
        self._add_to_dictionary(dictionary, 'unit', self.unit)
        return dictionary

    def from_dictionary(self, dictionary):
        super(LineItemLevel3InterchangeInformation, self).from_dictionary(dictionary)
        if 'discountAmount' in dictionary:
            self.discount_amount = dictionary['discountAmount']
        if 'lineAmountTotal' in dictionary:
            self.line_amount_total = dictionary['lineAmountTotal']
        if 'productCode' in dictionary:
            self.product_code = dictionary['productCode']
        if 'productPrice' in dictionary:
            self.product_price = dictionary['productPrice']
        if 'productType' in dictionary:
            self.product_type = dictionary['productType']
        if 'quantity' in dictionary:
            self.quantity = dictionary['quantity']
        if 'taxAmount' in dictionary:
            self.tax_amount = dictionary['taxAmount']
        if 'unit' in dictionary:
            self.unit = dictionary['unit']
        return self
