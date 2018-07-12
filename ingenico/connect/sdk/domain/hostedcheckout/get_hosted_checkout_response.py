# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.hostedcheckout.definitions.created_payment_output import CreatedPaymentOutput


class GetHostedCheckoutResponse(DataObject):

    __created_payment_output = None
    __status = None

    @property
    def created_payment_output(self):
        """
        | When a payment has been created during the hosted checkout session this object will return the details.
        
        Type: :class:`ingenico.connect.sdk.domain.hostedcheckout.definitions.created_payment_output.CreatedPaymentOutput`
        """
        return self.__created_payment_output

    @created_payment_output.setter
    def created_payment_output(self, value):
        self.__created_payment_output = value

    @property
    def status(self):
        """
        | This is the status of the hosted checkout. Possible values are:
        
        * IN_PROGRESS - The checkout is still in progress and has not finished yet
        * PAYMENT_CREATED - A payment has been created
        * CANCELLED_BY_CONSUMER - If a consumer cancels the payment on the payment product detail page of the MyCheckout hosted payment pages, the status will change to IN_PROGRESS. Since we understand you want to be aware of a consumer cancelling the payment on the page we host for you, you can choose to get the status CANCELLED_BY_CONSUMER back instead of the status IN_PROGRESS. In order to get the status CANCELLED_BY_CONSUMER back, you need to have the returnCancelState flag enabled in the Create hosted checkout <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/hostedcheckouts/create.html> call
        
        
        | Please see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html> for a full overview of possible values.
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def to_dictionary(self):
        dictionary = super(GetHostedCheckoutResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'createdPaymentOutput', self.created_payment_output)
        self._add_to_dictionary(dictionary, 'status', self.status)
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetHostedCheckoutResponse, self).from_dictionary(dictionary)
        if 'createdPaymentOutput' in dictionary:
            if not isinstance(dictionary['createdPaymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['createdPaymentOutput']))
            value = CreatedPaymentOutput()
            self.created_payment_output = value.from_dictionary(dictionary['createdPaymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
