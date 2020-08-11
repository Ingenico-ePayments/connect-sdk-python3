# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney


class Installments(DataObject):
    """
    | Object containing data related to installments.
    """

    __amount_of_money_per_installment = None
    __frequency_of_installments = None
    __interest_rate = None
    __number_of_installments = None

    @property
    def amount_of_money_per_installment(self):
        """
        | The amount that will be paid per installment. The total amount of amountOfMoneyPerInstallment x numberOfInstallments can not be higher than the total amount of this transaction, although we will not validate that.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money_per_installment

    @amount_of_money_per_installment.setter
    def amount_of_money_per_installment(self, value):
        self.__amount_of_money_per_installment = value

    @property
    def frequency_of_installments(self):
        """
        | The frequency in which the installments will be collected from the customer. The possible values are:
        
        * daily
        * weekly
        * monthly (default)
        * quarterly
        
        Type: str
        """
        return self.__frequency_of_installments

    @frequency_of_installments.setter
    def frequency_of_installments(self, value):
        self.__frequency_of_installments = value

    @property
    def interest_rate(self):
        """
        | The interest rate paid for installments expressed in percentage. So for example 5.75 means 5.75%
        
        Type: str
        """
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = value

    @property
    def number_of_installments(self):
        """
        | The number of installments in which this transaction will be paid.
        
        Type: int
        """
        return self.__number_of_installments

    @number_of_installments.setter
    def number_of_installments(self, value):
        self.__number_of_installments = value

    def to_dictionary(self):
        dictionary = super(Installments, self).to_dictionary()
        if self.amount_of_money_per_installment is not None:
            dictionary['amountOfMoneyPerInstallment'] = self.amount_of_money_per_installment.to_dictionary()
        if self.frequency_of_installments is not None:
            dictionary['frequencyOfInstallments'] = self.frequency_of_installments
        if self.interest_rate is not None:
            dictionary['interestRate'] = self.interest_rate
        if self.number_of_installments is not None:
            dictionary['numberOfInstallments'] = self.number_of_installments
        return dictionary

    def from_dictionary(self, dictionary):
        super(Installments, self).from_dictionary(dictionary)
        if 'amountOfMoneyPerInstallment' in dictionary:
            if not isinstance(dictionary['amountOfMoneyPerInstallment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoneyPerInstallment']))
            value = AmountOfMoney()
            self.amount_of_money_per_installment = value.from_dictionary(dictionary['amountOfMoneyPerInstallment'])
        if 'frequencyOfInstallments' in dictionary:
            self.frequency_of_installments = dictionary['frequencyOfInstallments']
        if 'interestRate' in dictionary:
            self.interest_rate = dictionary['interestRate']
        if 'numberOfInstallments' in dictionary:
            self.number_of_installments = dictionary['numberOfInstallments']
        return self
