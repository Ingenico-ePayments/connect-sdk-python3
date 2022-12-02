# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_redirect_payment_product4101_specific_input import AbstractRedirectPaymentProduct4101SpecificInput


class RedirectPaymentProduct4101SpecificInputBase(AbstractRedirectPaymentProduct4101SpecificInput):
    """
    | Please find below specific input fields for payment product 4101 (UPI)
    """

    __display_name = None

    @property
    def display_name(self):
        """
        | The merchant name as shown to the customer in some payment applications.
        
        Type: str
        """
        return self.__display_name

    @display_name.setter
    def display_name(self, value):
        self.__display_name = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct4101SpecificInputBase, self).to_dictionary()
        if self.display_name is not None:
            dictionary['displayName'] = self.display_name
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct4101SpecificInputBase, self).from_dictionary(dictionary)
        if 'displayName' in dictionary:
            self.display_name = dictionary['displayName']
        return self
