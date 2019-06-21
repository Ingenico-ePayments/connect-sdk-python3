# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.amount_breakdown import AmountBreakdown
from ingenico.connect.sdk.domain.payment.definitions.gift_card_purchase import GiftCardPurchase
from ingenico.connect.sdk.domain.payment.definitions.line_item import LineItem


class ShoppingCart(DataObject):

    __amount_breakdown = None
    __gift_card_purchase = None
    __is_pre_order = None
    __items = None
    __pre_order_item_availability_date = None
    __re_order_indicator = None

    @property
    def amount_breakdown(self):
        """
        | Determines the type of the amount.
        
        Type: list[:class:`ingenico.connect.sdk.domain.payment.definitions.amount_breakdown.AmountBreakdown`]
        """
        return self.__amount_breakdown

    @amount_breakdown.setter
    def amount_breakdown(self, value):
        self.__amount_breakdown = value

    @property
    def gift_card_purchase(self):
        """
        | Object containing information on purchased gift card(s)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.gift_card_purchase.GiftCardPurchase`
        """
        return self.__gift_card_purchase

    @gift_card_purchase.setter
    def gift_card_purchase(self, value):
        self.__gift_card_purchase = value

    @property
    def is_pre_order(self):
        """
        | The customer is pre-ordering one or more items
        
        Type: bool
        """
        return self.__is_pre_order

    @is_pre_order.setter
    def is_pre_order(self, value):
        self.__is_pre_order = value

    @property
    def items(self):
        """
        | Shopping cart data
        
        Type: list[:class:`ingenico.connect.sdk.domain.payment.definitions.line_item.LineItem`]
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    @property
    def pre_order_item_availability_date(self):
        """
        | Date (YYYYMMDD) when the preordered item becomes available
        
        Type: str
        """
        return self.__pre_order_item_availability_date

    @pre_order_item_availability_date.setter
    def pre_order_item_availability_date(self, value):
        self.__pre_order_item_availability_date = value

    @property
    def re_order_indicator(self):
        """
        | Indicates whether the cardholder is reordering previously purchased item(s)
        
        | true = the customer is re-ordering at least one of the items again
        
        | false = this is the first time the customer is ordering these items
        
        Type: bool
        """
        return self.__re_order_indicator

    @re_order_indicator.setter
    def re_order_indicator(self, value):
        self.__re_order_indicator = value

    def to_dictionary(self):
        dictionary = super(ShoppingCart, self).to_dictionary()
        if self.amount_breakdown is not None:
            dictionary['amountBreakdown'] = []
            for element in self.amount_breakdown:
                if element is not None:
                    dictionary['amountBreakdown'].append(element.to_dictionary())
        if self.gift_card_purchase is not None:
            dictionary['giftCardPurchase'] = self.gift_card_purchase.to_dictionary()
        if self.is_pre_order is not None:
            dictionary['isPreOrder'] = self.is_pre_order
        if self.items is not None:
            dictionary['items'] = []
            for element in self.items:
                if element is not None:
                    dictionary['items'].append(element.to_dictionary())
        if self.pre_order_item_availability_date is not None:
            dictionary['preOrderItemAvailabilityDate'] = self.pre_order_item_availability_date
        if self.re_order_indicator is not None:
            dictionary['reOrderIndicator'] = self.re_order_indicator
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShoppingCart, self).from_dictionary(dictionary)
        if 'amountBreakdown' in dictionary:
            if not isinstance(dictionary['amountBreakdown'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['amountBreakdown']))
            self.amount_breakdown = []
            for element in dictionary['amountBreakdown']:
                value = AmountBreakdown()
                self.amount_breakdown.append(value.from_dictionary(element))
        if 'giftCardPurchase' in dictionary:
            if not isinstance(dictionary['giftCardPurchase'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['giftCardPurchase']))
            value = GiftCardPurchase()
            self.gift_card_purchase = value.from_dictionary(dictionary['giftCardPurchase'])
        if 'isPreOrder' in dictionary:
            self.is_pre_order = dictionary['isPreOrder']
        if 'items' in dictionary:
            if not isinstance(dictionary['items'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['items']))
            self.items = []
            for element in dictionary['items']:
                value = LineItem()
                self.items.append(value.from_dictionary(element))
        if 'preOrderItemAvailabilityDate' in dictionary:
            self.pre_order_item_availability_date = dictionary['preOrderItemAvailabilityDate']
        if 'reOrderIndicator' in dictionary:
            self.re_order_indicator = dictionary['reOrderIndicator']
        return self
