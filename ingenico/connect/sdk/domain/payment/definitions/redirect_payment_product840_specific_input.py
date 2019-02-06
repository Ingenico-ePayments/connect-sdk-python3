# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_redirect_payment_product840_specific_input import AbstractRedirectPaymentProduct840SpecificInput


class RedirectPaymentProduct840SpecificInput(AbstractRedirectPaymentProduct840SpecificInput):
    """
    | Please find below specific input fields for payment product 840 (PayPal)
    """

    __custom = None
    __is_shortcut = None

    @property
    def custom(self):
        """
        | A free text string that you can send to PayPal. With a special agreement between PayPal and you, PayPal uses the data in that field, for custom services they offer to you.
        
        Type: str
        
        Deprecated; | use order.references.descriptor instead.
        """
        return self.__custom

    @custom.setter
    def custom(self, value):
        self.__custom = value

    @property
    def is_shortcut(self):
        """
        | Deprecated: If your PayPal payments are processed by Ingenico's Ogone Payment Platform, please use the field addressSelectionAtPayPal instead.
        | Indicates whether to use PayPal Express Checkout for payments processed by Ingenico's GlobalCollect Payment Platform. 
        
        * true = PayPal Express Checkout 
        * false = Regular PayPal payment 
        
        | . For payments processed by Ingenico's Ogone Payment Platform, please see the addressSelectionAtPayPal field for more information.
        
        Type: bool
        """
        return self.__is_shortcut

    @is_shortcut.setter
    def is_shortcut(self, value):
        self.__is_shortcut = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct840SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'custom', self.custom)
        self._add_to_dictionary(dictionary, 'isShortcut', self.is_shortcut)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct840SpecificInput, self).from_dictionary(dictionary)
        if 'custom' in dictionary:
            self.custom = dictionary['custom']
        if 'isShortcut' in dictionary:
            self.is_shortcut = dictionary['isShortcut']
        return self
