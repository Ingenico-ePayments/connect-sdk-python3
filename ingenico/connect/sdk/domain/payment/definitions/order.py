# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.payment.definitions.additional_order_input import AdditionalOrderInput
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.line_item import LineItem
from ingenico.connect.sdk.domain.payment.definitions.order_references import OrderReferences
from ingenico.connect.sdk.domain.payment.definitions.seller import Seller
from ingenico.connect.sdk.domain.payment.definitions.shipping import Shipping
from ingenico.connect.sdk.domain.payment.definitions.shopping_cart import ShoppingCart


class Order(DataObject):

    __additional_input = None
    __amount_of_money = None
    __customer = None
    __items = None
    __references = None
    __seller = None
    __shipping = None
    __shopping_cart = None

    @property
    def additional_input(self):
        """
        | Object containing additional input on the order
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.additional_order_input.AdditionalOrderInput`
        """
        return self.__additional_input

    @additional_input.setter
    def additional_input(self, value):
        self.__additional_input = value

    @property
    def amount_of_money(self):
        """
        | Object containing amount and ISO currency code attributes
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def customer(self):
        """
        | Object containing the details of the consumer
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.customer.Customer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def items(self):
        """
        | Shopping cart data
        
        Type: list[:class:`ingenico.connect.sdk.domain.payment.definitions.line_item.LineItem`]
        
        Deprecated; | Use ShoppingCart.items instead
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    @property
    def references(self):
        """
        | Object that holds all reference fields that are linked to this transaction
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order_references.OrderReferences`
        """
        return self.__references

    @references.setter
    def references(self, value):
        self.__references = value

    @property
    def seller(self):
        """
        | Object containing seller details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.seller.Seller`
        """
        return self.__seller

    @seller.setter
    def seller(self, value):
        self.__seller = value

    @property
    def shipping(self):
        """
        | Object containing information regarding shipping / delivery
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.shipping.Shipping`
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value):
        self.__shipping = value

    @property
    def shopping_cart(self):
        """
        | Shopping cart data, including items and specific amounts.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.shopping_cart.ShoppingCart`
        """
        return self.__shopping_cart

    @shopping_cart.setter
    def shopping_cart(self, value):
        self.__shopping_cart = value

    def to_dictionary(self):
        dictionary = super(Order, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalInput', self.additional_input)
        self._add_to_dictionary(dictionary, 'amountOfMoney', self.amount_of_money)
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'items', self.items)
        self._add_to_dictionary(dictionary, 'references', self.references)
        self._add_to_dictionary(dictionary, 'seller', self.seller)
        self._add_to_dictionary(dictionary, 'shipping', self.shipping)
        self._add_to_dictionary(dictionary, 'shoppingCart', self.shopping_cart)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Order, self).from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInput()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = Customer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'items' in dictionary:
            if not isinstance(dictionary['items'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['items']))
            self.items = []
            for items_element in dictionary['items']:
                items_value = LineItem()
                self.items.append(items_value.from_dictionary(items_element))
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = OrderReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'seller' in dictionary:
            if not isinstance(dictionary['seller'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['seller']))
            value = Seller()
            self.seller = value.from_dictionary(dictionary['seller'])
        if 'shipping' in dictionary:
            if not isinstance(dictionary['shipping'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shipping']))
            value = Shipping()
            self.shipping = value.from_dictionary(dictionary['shipping'])
        if 'shoppingCart' in dictionary:
            if not isinstance(dictionary['shoppingCart'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shoppingCart']))
            value = ShoppingCart()
            self.shopping_cart = value.from_dictionary(dictionary['shoppingCart'])
        return self
