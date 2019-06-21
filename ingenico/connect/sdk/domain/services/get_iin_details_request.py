# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.services.definitions.payment_context import PaymentContext


class GetIINDetailsRequest(DataObject):
    """
    | Input for the retrieval of the IIN details request.
    """

    __bin = None
    __payment_context = None

    @property
    def bin(self):
        """
        | The first digits of the credit card number from left to right with a minimum of 6 digits, or the full credit card number.
        
        Type: str
        """
        return self.__bin

    @bin.setter
    def bin(self, value):
        self.__bin = value

    @property
    def payment_context(self):
        """
        | Optional payment context to refine the IIN lookup to filter out payment products not applicable to your payment.
        
        Type: :class:`ingenico.connect.sdk.domain.services.definitions.payment_context.PaymentContext`
        """
        return self.__payment_context

    @payment_context.setter
    def payment_context(self, value):
        self.__payment_context = value

    def to_dictionary(self):
        dictionary = super(GetIINDetailsRequest, self).to_dictionary()
        if self.bin is not None:
            dictionary['bin'] = self.bin
        if self.payment_context is not None:
            dictionary['paymentContext'] = self.payment_context.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetIINDetailsRequest, self).from_dictionary(dictionary)
        if 'bin' in dictionary:
            self.bin = dictionary['bin']
        if 'paymentContext' in dictionary:
            if not isinstance(dictionary['paymentContext'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentContext']))
            value = PaymentContext()
            self.payment_context = value.from_dictionary(dictionary['paymentContext'])
        return self
