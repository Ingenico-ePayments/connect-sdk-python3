# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_redirect_payment_product840_specific_input import AbstractRedirectPaymentProduct840SpecificInput


class RedirectPaymentProduct840SpecificInputBase(AbstractRedirectPaymentProduct840SpecificInput):
    """
    | Please find below the specific input field for payment product 840 (PayPal)
    """

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct840SpecificInputBase, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct840SpecificInputBase, self).from_dictionary(dictionary)
        return self
