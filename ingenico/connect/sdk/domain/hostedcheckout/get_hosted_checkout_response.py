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
        * CANCELLED_BY_CONSUMER - If a customer cancels the payment on the payment product detail page of the MyCheckout hosted payment pages, the status will change to IN_PROGRESS. Since we understand you want to be aware of a customer cancelling the payment on the page we host for you, you can choose to receive the status CANCELLED_BY_CONSUMER instead of the status IN_PROGRESS. In order to receive the status CANCELLED_BY_CONSUMER, you need to have the returnCancelState flag enabled in the Create hosted checkout <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/hostedcheckouts/create.html> call.
        * CLIENT_NOT_ELIGIBLE_FOR_SELECTED_PAYMENT_PRODUCT - With some payment products it might occur that the device of the user is not capable to complete the payment. If the Hosted Checkout Session was restricted to a single project that is not compatible to the user's device you will receive this Hosted Checkout status. This scenario applies to: Google Pay (Payment Product ID: 320).
        
        
        | Please see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html> for a full overview of possible values.
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def to_dictionary(self):
        dictionary = super(GetHostedCheckoutResponse, self).to_dictionary()
        if self.created_payment_output is not None:
            dictionary['createdPaymentOutput'] = self.created_payment_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
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
