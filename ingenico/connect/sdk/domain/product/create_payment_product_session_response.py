# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.mobile_payment_product_session302_specific_output import MobilePaymentProductSession302SpecificOutput


class CreatePaymentProductSessionResponse(DataObject):

    __payment_product_session302_specific_output = None

    @property
    def payment_product_session302_specific_output(self):
        """
        | Object containing the Apple Pay session object.
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.mobile_payment_product_session302_specific_output.MobilePaymentProductSession302SpecificOutput`
        """
        return self.__payment_product_session302_specific_output

    @payment_product_session302_specific_output.setter
    def payment_product_session302_specific_output(self, value):
        self.__payment_product_session302_specific_output = value

    def to_dictionary(self):
        dictionary = super(CreatePaymentProductSessionResponse, self).to_dictionary()
        if self.payment_product_session302_specific_output is not None:
            dictionary['paymentProductSession302SpecificOutput'] = self.payment_product_session302_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentProductSessionResponse, self).from_dictionary(dictionary)
        if 'paymentProductSession302SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProductSession302SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductSession302SpecificOutput']))
            value = MobilePaymentProductSession302SpecificOutput()
            self.payment_product_session302_specific_output = value.from_dictionary(dictionary['paymentProductSession302SpecificOutput'])
        return self
