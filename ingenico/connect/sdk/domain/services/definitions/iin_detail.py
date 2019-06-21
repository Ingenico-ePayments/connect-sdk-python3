# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class IINDetail(DataObject):
    """
    | Output of the retrieval of the IIN details request
    """

    __is_allowed_in_context = None
    __payment_product_id = None

    @property
    def is_allowed_in_context(self):
        """
        | Populated only if you submitted a payment context.
        
        * true - The payment product is allowed in the submitted context.
        * false - The payment product is not allowed in the submitted context. Note that in this case, none of the brands of the card will be allowed in the submitted context.
        
        Type: bool
        """
        return self.__is_allowed_in_context

    @is_allowed_in_context.setter
    def is_allowed_in_context(self, value):
        self.__is_allowed_in_context = value

    @property
    def payment_product_id(self):
        """
        | Payment product identifier
        | Please see payment products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(IINDetail, self).to_dictionary()
        if self.is_allowed_in_context is not None:
            dictionary['isAllowedInContext'] = self.is_allowed_in_context
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(IINDetail, self).from_dictionary(dictionary)
        if 'isAllowedInContext' in dictionary:
            self.is_allowed_in_context = dictionary['isAllowedInContext']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
