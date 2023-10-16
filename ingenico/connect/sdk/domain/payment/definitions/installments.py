# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney


class Installments(DataObject):
    """
    | Object containing data related to installments which can be used for card payments and only with some acquirers. In case you send in the details of this object, only the combination of card products and acquirers that do support installments will be shown on the MyCheckout hosted payment pages.
    """

    __amount_of_money_per_installment = None
    __amount_of_money_total = None
    __frequency_of_installments = None
    __installment_plan_code = None
    __interest_rate = None
    __number_of_installments = None

    @property
    def amount_of_money_per_installment(self):
        """
        | The amount that will be paid per installment. The total amount of amountOfMoneyPerInstallment x numberOfInstallments can not be higher than the total amount of this transaction, although we will not validate that.
        | For the payment product IDs BC Card (paymentProductId 8590), Hana Card (paymentProductId 8591), Hyundai Card (paymentProductId 8592), KB Card (paymentProductId 8593), Lotte Card (paymentProductId 8594), NH Card (paymentProductId 8595), Samsung Card (paymentProductId 8596) and Shinhan Card (paymentProductId 8597), this property is not used as the value is decided by the issuer.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money_per_installment

    @amount_of_money_per_installment.setter
    def amount_of_money_per_installment(self, value):
        self.__amount_of_money_per_installment = value

    @property
    def amount_of_money_total(self):
        """
        | Object containing the total amount and ISO currency code attributes
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money_total

    @amount_of_money_total.setter
    def amount_of_money_total(self, value):
        self.__amount_of_money_total = value

    @property
    def frequency_of_installments(self):
        """
        | The frequency in which the installments will be collected from the customer. The possible values are:
        
        * daily
        * weekly
        * monthly (default)
        * quarterly
        
        
        | For the payment product IDs BC Card (paymentProductId 8590), Hana Card (paymentProductId 8591), Hyundai Card (paymentProductId 8592), KB Card (paymentProductId 8593), Lotte Card (paymentProductId 8594), NH Card (paymentProductId 8595), Samsung Card (paymentProductId 8596) and Shinhan Card (paymentProductId 8597), only the value monthly is valid.
        
        Type: str
        """
        return self.__frequency_of_installments

    @frequency_of_installments.setter
    def frequency_of_installments(self, value):
        self.__frequency_of_installments = value

    @property
    def installment_plan_code(self):
        """
        | The code for the installment plan. The possible values are:
        
        * **43** No-interest, 3 month Installmentplan
        * **46**No-interest, 6 month Installmentplan
        * **49**No-interest, 9 month Installmentplan
        * **52**No-interest, 12 month Installmentplan
        
        Type: int
        """
        return self.__installment_plan_code

    @installment_plan_code.setter
    def installment_plan_code(self, value):
        self.__installment_plan_code = value

    @property
    def interest_rate(self):
        """
        | The interest rate paid for installments expressed in percentage. So for example 5.75 means 5.75%
        | For the payment product IDs BC Card (paymentProductId 8590), Hana Card (paymentProductId 8591), Hyundai Card (paymentProductId 8592), KB Card (paymentProductId 8593), Lotte Card (paymentProductId 8594), NH Card (paymentProductId 8595), Samsung Card (paymentProductId 8596) and Shinhan Card (paymentProductId 8597), this property is not used as the value is decided by the issuer.
        
        Type: str
        """
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = value

    @property
    def number_of_installments(self):
        """
        | The number of installments in which this transaction will be paid, which can be used for card payments at supported acquirers, or with specific payment products. Only used with some acquirers. In case you send in the details of this object, only the payment products (or  combination of card products and acquirers) that support installments will be shown on the MyCheckout hosted payment pages. If this property is not provided the customer will not see details on the installment plan in a HostedCheckout.
        | For the payment product IDs BC Card (paymentProductId 8590), Hana Card (paymentProductId 8591), Hyundai Card (paymentProductId 8592), KB Card (paymentProductId 8593), Lotte Card (paymentProductId 8594), NH Card (paymentProductId 8595), Samsung Card (paymentProductId 8596) and Shinhan Card (paymentProductId 8597), there is a maximum of 12 installments.
        
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
        if self.amount_of_money_total is not None:
            dictionary['amountOfMoneyTotal'] = self.amount_of_money_total.to_dictionary()
        if self.frequency_of_installments is not None:
            dictionary['frequencyOfInstallments'] = self.frequency_of_installments
        if self.installment_plan_code is not None:
            dictionary['installmentPlanCode'] = self.installment_plan_code
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
        if 'amountOfMoneyTotal' in dictionary:
            if not isinstance(dictionary['amountOfMoneyTotal'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoneyTotal']))
            value = AmountOfMoney()
            self.amount_of_money_total = value.from_dictionary(dictionary['amountOfMoneyTotal'])
        if 'frequencyOfInstallments' in dictionary:
            self.frequency_of_installments = dictionary['frequencyOfInstallments']
        if 'installmentPlanCode' in dictionary:
            self.installment_plan_code = dictionary['installmentPlanCode']
        if 'interestRate' in dictionary:
            self.interest_rate = dictionary['interestRate']
        if 'numberOfInstallments' in dictionary:
            self.number_of_installments = dictionary['numberOfInstallments']
        return self
