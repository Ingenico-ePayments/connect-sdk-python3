# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.abstract_order_status import AbstractOrderStatus
from ingenico.connect.sdk.domain.definitions.order_status_output import OrderStatusOutput
from ingenico.connect.sdk.domain.payment.definitions.order_output import OrderOutput


class PayoutResult(AbstractOrderStatus):

    __payout_output = None
    __status = None
    __status_output = None

    @property
    def payout_output(self):
        """
        | Object containing payout details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order_output.OrderOutput`
        """
        return self.__payout_output

    @payout_output.setter
    def payout_output(self, value):
        self.__payout_output = value

    @property
    def status(self):
        """
        | Current high-level status of the payouts in a human-readable form. Possible values are :
        
        * CREATED - The transaction has been created. This is the initial state once a new payout is created.
        * PENDING_APPROVAL - The transaction is awaiting approval from you to proceed with the paying out of the funds
        * REJECTED - The transaction has been rejected
        * PAYOUT_REQUESTED - The transaction is in the queue to be payed out to the customer
        * ACCOUNT_CREDITED - We have successfully credited the customer
        * REJECTED_CREDIT - The credit to the account of the customer was rejected by the bank
        * CANCELLED - You have cancelled the transaction
        * REVERSED - The payout has been reversed and the money is returned to your balance
        
        
        | Please see Statuses <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/statuses.html> for a full overview of possible values.
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def status_output(self):
        """
        | This object has the numeric representation of the current payout status, timestamp of last status change and performable action on the current payout resource.
        | In case of a rejected payout, detailed error information is listed.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.order_status_output.OrderStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value):
        self.__status_output = value

    def to_dictionary(self):
        dictionary = super(PayoutResult, self).to_dictionary()
        if self.payout_output is not None:
            dictionary['payoutOutput'] = self.payout_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutResult, self).from_dictionary(dictionary)
        if 'payoutOutput' in dictionary:
            if not isinstance(dictionary['payoutOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutOutput']))
            value = OrderOutput()
            self.payout_output = value.from_dictionary(dictionary['payoutOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = OrderStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
