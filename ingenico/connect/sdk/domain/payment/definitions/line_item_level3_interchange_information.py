#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class LineItemLevel3InterchangeInformation(DataObject):
    """
    Class LineItemLevel3InterchangeInformation
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_LineItemLevel3InterchangeInformation
    """

    __discount_amount = None
    __line_amount_total = None
    __product_code = None
    __product_price = None
    __product_type = None
    __quantity = None
    __tax_amount = None
    __unit = None

    @property
    def discount_amount(self):
        """
        int
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value

    @property
    def line_amount_total(self):
        """
        int
        """
        return self.__line_amount_total

    @line_amount_total.setter
    def line_amount_total(self, value):
        self.__line_amount_total = value

    @property
    def product_code(self):
        """
        str
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value

    @property
    def product_price(self):
        """
        int
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        self.__product_price = value

    @property
    def product_type(self):
        """
        str
        """
        return self.__product_type

    @product_type.setter
    def product_type(self, value):
        self.__product_type = value

    @property
    def quantity(self):
        """
        int
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def tax_amount(self):
        """
        int
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value

    @property
    def unit(self):
        """
        str
        """
        return self.__unit

    @unit.setter
    def unit(self, value):
        self.__unit = value

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
