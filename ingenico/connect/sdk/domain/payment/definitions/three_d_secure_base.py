# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_three_d_secure import AbstractThreeDSecure


class ThreeDSecureBase(AbstractThreeDSecure):
    """
    | Object containing specific data regarding 3-D Secure
    """

    def to_dictionary(self):
        dictionary = super(ThreeDSecureBase, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSecureBase, self).from_dictionary(dictionary)
        return self
