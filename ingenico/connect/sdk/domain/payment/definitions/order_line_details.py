# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class OrderLineDetails(DataObject):

    __discount_amount = None
    __google_product_category_id = None
    __line_amount_total = None
    __product_category = None
    __product_code = None
    __product_name = None
    __product_price = None
    __product_type = None
    __quantity = None
    __tax_amount = None
    __unit = None

    @property
    def discount_amount(self):
        """
        | Discount on the line item, with the last two digits implied as decimal places
        
        Type: int
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value

    @property
    def google_product_category_id(self):
        """
        | The Google product category ID for the item.
        
        Type: int
        """
        return self.__google_product_category_id

    @google_product_category_id.setter
    def google_product_category_id(self, value):
        self.__google_product_category_id = value

    @property
    def line_amount_total(self):
        """
        | Total amount for the line item
        
        Type: int
        """
        return self.__line_amount_total

    @line_amount_total.setter
    def line_amount_total(self, value):
        self.__line_amount_total = value

    @property
    def product_category(self):
        """
        | The category of the product (i.e. home appliance). This property can be used for fraud screening on the Ogone Platform.
        
        Type: str
        """
        return self.__product_category

    @product_category.setter
    def product_category(self, value):
        self.__product_category = value

    @property
    def product_code(self):
        """
        | Product or UPC Code, left justified
        | Note: Must not be all spaces or all zeros
        
        Type: str
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = value

    @property
    def product_name(self):
        """
        | The name of the product.
        
        Type: str
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    @property
    def product_price(self):
        """
        | The price of one unit of the product, the value should be zero or greater
        
        Type: int
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        self.__product_price = value

    @property
    def product_type(self):
        """
        | Code used to classify items that are purchased
        | Note: Must not be all spaces or all zeros
        
        Type: str
        """
        return self.__product_type

    @product_type.setter
    def product_type(self, value):
        self.__product_type = value

    @property
    def quantity(self):
        """
        | Quantity of the units being purchased, should be greater than zero
        | Note: Must not be all spaces or all zeros
        
        Type: int
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def tax_amount(self):
        """
        | Tax on the line item, with the last two digits implied as decimal places
        
        Type: int
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value

    @property
    def unit(self):
        """
        | Indicates the line item unit of measure; for example: each, kit, pair, gallon, month, etc.
        
        Type: str
        """
        return self.__unit

    @unit.setter
    def unit(self, value):
        self.__unit = value

    def to_dictionary(self):
        dictionary = super(OrderLineDetails, self).to_dictionary()
        if self.discount_amount is not None:
            dictionary['discountAmount'] = self.discount_amount
        if self.google_product_category_id is not None:
            dictionary['googleProductCategoryId'] = self.google_product_category_id
        if self.line_amount_total is not None:
            dictionary['lineAmountTotal'] = self.line_amount_total
        if self.product_category is not None:
            dictionary['productCategory'] = self.product_category
        if self.product_code is not None:
            dictionary['productCode'] = self.product_code
        if self.product_name is not None:
            dictionary['productName'] = self.product_name
        if self.product_price is not None:
            dictionary['productPrice'] = self.product_price
        if self.product_type is not None:
            dictionary['productType'] = self.product_type
        if self.quantity is not None:
            dictionary['quantity'] = self.quantity
        if self.tax_amount is not None:
            dictionary['taxAmount'] = self.tax_amount
        if self.unit is not None:
            dictionary['unit'] = self.unit
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderLineDetails, self).from_dictionary(dictionary)
        if 'discountAmount' in dictionary:
            self.discount_amount = dictionary['discountAmount']
        if 'googleProductCategoryId' in dictionary:
            self.google_product_category_id = dictionary['googleProductCategoryId']
        if 'lineAmountTotal' in dictionary:
            self.line_amount_total = dictionary['lineAmountTotal']
        if 'productCategory' in dictionary:
            self.product_category = dictionary['productCategory']
        if 'productCode' in dictionary:
            self.product_code = dictionary['productCode']
        if 'productName' in dictionary:
            self.product_name = dictionary['productName']
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
