# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney


class SettlementDetails(DataObject):

    __acquirer_reference_number = None
    __amount_of_money = None
    __payment_id = None
    __retrieval_reference_number = None

    @property
    def acquirer_reference_number(self):
        """
        | The Acquirer Reference Number (ARN) is a unique identifier assigned to a card payment as it moves through the payment network.
        
        Type: str
        """
        return self.__acquirer_reference_number

    @acquirer_reference_number.setter
    def acquirer_reference_number(self, value):
        self.__acquirer_reference_number = value

    @property
    def amount_of_money(self):
        """
        | The payment amount
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def payment_id(self):
        """
        | Our unique payment transaction identifier.
        
        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def retrieval_reference_number(self):
        """
        | The Retrieval Reference Number (RRN) provides a unique reference for a card payment, pinpointing it to a specific date.
        
        Type: str
        """
        return self.__retrieval_reference_number

    @retrieval_reference_number.setter
    def retrieval_reference_number(self, value):
        self.__retrieval_reference_number = value

    def to_dictionary(self):
        dictionary = super(SettlementDetails, self).to_dictionary()
        if self.acquirer_reference_number is not None:
            dictionary['acquirerReferenceNumber'] = self.acquirer_reference_number
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.retrieval_reference_number is not None:
            dictionary['retrievalReferenceNumber'] = self.retrieval_reference_number
        return dictionary

    def from_dictionary(self, dictionary):
        super(SettlementDetails, self).from_dictionary(dictionary)
        if 'acquirerReferenceNumber' in dictionary:
            self.acquirer_reference_number = dictionary['acquirerReferenceNumber']
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'retrievalReferenceNumber' in dictionary:
            self.retrieval_reference_number = dictionary['retrievalReferenceNumber']
        return self
