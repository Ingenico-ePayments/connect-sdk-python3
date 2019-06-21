# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.payment.definitions.line_item_invoice_data import LineItemInvoiceData
from ingenico.connect.sdk.domain.payment.definitions.line_item_level3_interchange_information import LineItemLevel3InterchangeInformation
from ingenico.connect.sdk.domain.payment.definitions.order_line_details import OrderLineDetails


class LineItem(DataObject):

    __amount_of_money = None
    __invoice_data = None
    __level3_interchange_information = None
    __order_line_details = None

    @property
    def amount_of_money(self):
        """
        | Object containing amount and ISO currency code attributes
        | Note: make sure you submit the amount and currency code for each line item
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def invoice_data(self):
        """
        | Object containing the line items of the invoice or shopping cart
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.line_item_invoice_data.LineItemInvoiceData`
        """
        return self.__invoice_data

    @invoice_data.setter
    def invoice_data(self, value):
        self.__invoice_data = value

    @property
    def level3_interchange_information(self):
        """
        | Object containing additional information that when supplied can have a beneficial effect on the discountrates
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.line_item_level3_interchange_information.LineItemLevel3InterchangeInformation`
        
        Deprecated; Use orderLineDetails instead
        """
        return self.__level3_interchange_information

    @level3_interchange_information.setter
    def level3_interchange_information(self, value):
        self.__level3_interchange_information = value

    @property
    def order_line_details(self):
        """
        | Object containing additional information that when supplied can have a beneficial effect on the discountrates
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order_line_details.OrderLineDetails`
        """
        return self.__order_line_details

    @order_line_details.setter
    def order_line_details(self, value):
        self.__order_line_details = value

    def to_dictionary(self):
        dictionary = super(LineItem, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.invoice_data is not None:
            dictionary['invoiceData'] = self.invoice_data.to_dictionary()
        if self.level3_interchange_information is not None:
            dictionary['level3InterchangeInformation'] = self.level3_interchange_information.to_dictionary()
        if self.order_line_details is not None:
            dictionary['orderLineDetails'] = self.order_line_details.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(LineItem, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'invoiceData' in dictionary:
            if not isinstance(dictionary['invoiceData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['invoiceData']))
            value = LineItemInvoiceData()
            self.invoice_data = value.from_dictionary(dictionary['invoiceData'])
        if 'level3InterchangeInformation' in dictionary:
            if not isinstance(dictionary['level3InterchangeInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['level3InterchangeInformation']))
            value = LineItemLevel3InterchangeInformation()
            self.level3_interchange_information = value.from_dictionary(dictionary['level3InterchangeInformation'])
        if 'orderLineDetails' in dictionary:
            if not isinstance(dictionary['orderLineDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['orderLineDetails']))
            value = OrderLineDetails()
            self.order_line_details = value.from_dictionary(dictionary['orderLineDetails'])
        return self
