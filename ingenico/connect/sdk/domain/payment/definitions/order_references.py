# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.order_invoice_data import OrderInvoiceData


class OrderReferences(DataObject):

    __descriptor = None
    __invoice_data = None
    __merchant_order_id = None
    __merchant_reference = None

    @property
    def descriptor(self):
        """
        | Descriptive text that is used towards to customer, either during an online checkout at a third party and/or on the statement of the customer. For card transactions this is usually referred to as a Soft Descriptor. The maximum allowed length varies per card acquirer:
        
        * AIB - 22 characters
        * American Express - 25 characters
        * Atos Origin BNP - 15 characters
        * Barclays - 25 characters
        * Catella - 22 characters
        * CBA - 20 characters
        * Elavon - 25 characters
        * First Data - 25 characters
        * INICIS (INIPAY) - 22-30 characters
        * JCB - 25 characters
        * Merchant Solutions - 22-25 characters
        * Payvision (EU & HK) - 25 characters
        * SEB Euroline - 22 characters
        * Sub1 Argentina - 15 characters
        * Wells Fargo - 25 characters
        
        | Note that we advise you to use 22 characters as the max length as beyond this our experience is that issuers will start to truncate. We currently also only allow per API call overrides for AIB and Barclays
        | For alternative payment products the maximum allowed length varies per payment product:
        
        * 402 e-Przelewy - 30 characters
        * 404 INICIS - 80 characters
        * 802 Nordea ePayment Finland - 234 characters
        * 809 iDeal - 32 characters
        * 836 SOFORT - 42 characters
        * 840 PayPal - 127 characters
        * 841 WebMoney - 175 characters
        * 849 Yandex - 64 characters
        * 861 Alipay - 256 characters
        * 863 WeChat Pay - 32 characters
        * 880 BOKU - 20 characters
        * 8580 Qiwi - 255 characters
        * 1504 Konbini - 80 characters
        
        | All other payment products don't support a descriptor.
        
        Type: str
        """
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, value):
        self.__descriptor = value

    @property
    def invoice_data(self):
        """
        | Object containing additional invoice data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order_invoice_data.OrderInvoiceData`
        """
        return self.__invoice_data

    @invoice_data.setter
    def invoice_data(self, value):
        self.__invoice_data = value

    @property
    def merchant_order_id(self):
        """
        | Your order identifier
        | Note: This does not need to have a unique value for each transaction. This allows your to link multiple transactions to the same logical order in your system.
        
        Type: int
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self.__merchant_order_id = value

    @property
    def merchant_reference(self):
        """
        | Note that the maximum length of this field for transactions processed on the GlobalCollect platform is 30. Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files.
        
        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value):
        self.__merchant_reference = value

    def to_dictionary(self):
        dictionary = super(OrderReferences, self).to_dictionary()
        if self.descriptor is not None:
            dictionary['descriptor'] = self.descriptor
        if self.invoice_data is not None:
            dictionary['invoiceData'] = self.invoice_data.to_dictionary()
        if self.merchant_order_id is not None:
            dictionary['merchantOrderId'] = self.merchant_order_id
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
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
