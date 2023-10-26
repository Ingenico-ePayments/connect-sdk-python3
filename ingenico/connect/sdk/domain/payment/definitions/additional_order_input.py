# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.airline_data import AirlineData
from ingenico.connect.sdk.domain.definitions.lodging_data import LodgingData
from ingenico.connect.sdk.domain.payment.definitions.account_funding_recipient import AccountFundingRecipient
from ingenico.connect.sdk.domain.payment.definitions.installments import Installments
from ingenico.connect.sdk.domain.payment.definitions.level3_summary_data import Level3SummaryData
from ingenico.connect.sdk.domain.payment.definitions.loan_recipient import LoanRecipient
from ingenico.connect.sdk.domain.payment.definitions.order_type_information import OrderTypeInformation


class AdditionalOrderInput(DataObject):

    __account_funding_recipient = None
    __airline_data = None
    __installments = None
    __level3_summary_data = None
    __loan_recipient = None
    __lodging_data = None
    __number_of_installments = None
    __order_date = None
    __type_information = None

    @property
    def account_funding_recipient(self):
        """
        | Object containing specific data regarding the recipient of an account funding transaction
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.account_funding_recipient.AccountFundingRecipient`
        """
        return self.__account_funding_recipient

    @account_funding_recipient.setter
    def account_funding_recipient(self, value):
        self.__account_funding_recipient = value

    @property
    def airline_data(self):
        """
        | Object that holds airline specific data
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.airline_data.AirlineData`
        """
        return self.__airline_data

    @airline_data.setter
    def airline_data(self, value):
        self.__airline_data = value

    @property
    def installments(self):
        """
        | Object containing data related to installments which can be used for card payments and only with some acquirers. In case you send in the details of this object, only the combination of card products and acquirers that do support installments will be shown on the MyCheckout hosted payment pages.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.installments.Installments`
        """
        return self.__installments

    @installments.setter
    def installments(self, value):
        self.__installments = value

    @property
    def level3_summary_data(self):
        """
        | Object that holds Level3 summary data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.level3_summary_data.Level3SummaryData`
        
        Deprecated; Use Order.shoppingCart.amountBreakdown instead
        """
        return self.__level3_summary_data

    @level3_summary_data.setter
    def level3_summary_data(self, value):
        self.__level3_summary_data = value

    @property
    def loan_recipient(self):
        """
        | Object containing specific data regarding the recipient of a loan in the UK
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.loan_recipient.LoanRecipient`
        
        Deprecated; No replacement
        """
        return self.__loan_recipient

    @loan_recipient.setter
    def loan_recipient(self, value):
        self.__loan_recipient = value

    @property
    def lodging_data(self):
        """
        | Object that holds lodging specific data
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.lodging_data.LodgingData`
        """
        return self.__lodging_data

    @lodging_data.setter
    def lodging_data(self, value):
        self.__lodging_data = value

    @property
    def number_of_installments(self):
        """
        | The number of installments in which this transaction will be paid, which can be used for card payments. Only used with some acquirers. In case you send in the details of this object, only the combination of card products and acquirers that do support installments will be shown on the MyCheckout hosted payment pages.
        
        Type: int
        
        Deprecated; Use installments.numberOfInstallments instead
        """
        return self.__number_of_installments

    @number_of_installments.setter
    def number_of_installments(self, value):
        self.__number_of_installments = value

    @property
    def order_date(self):
        """
        | Date and time of order
        | Format: YYYYMMDDHH24MISS
        
        Type: str
        """
        return self.__order_date

    @order_date.setter
    def order_date(self, value):
        self.__order_date = value

    @property
    def type_information(self):
        """
        | Object that holds the purchase and usage type indicators
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.order_type_information.OrderTypeInformation`
        """
        return self.__type_information

    @type_information.setter
    def type_information(self, value):
        self.__type_information = value

    def to_dictionary(self):
        dictionary = super(AdditionalOrderInput, self).to_dictionary()
        if self.account_funding_recipient is not None:
            dictionary['accountFundingRecipient'] = self.account_funding_recipient.to_dictionary()
        if self.airline_data is not None:
            dictionary['airlineData'] = self.airline_data.to_dictionary()
        if self.installments is not None:
            dictionary['installments'] = self.installments.to_dictionary()
        if self.level3_summary_data is not None:
            dictionary['level3SummaryData'] = self.level3_summary_data.to_dictionary()
        if self.loan_recipient is not None:
            dictionary['loanRecipient'] = self.loan_recipient.to_dictionary()
        if self.lodging_data is not None:
            dictionary['lodgingData'] = self.lodging_data.to_dictionary()
        if self.number_of_installments is not None:
            dictionary['numberOfInstallments'] = self.number_of_installments
        if self.order_date is not None:
            dictionary['orderDate'] = self.order_date
        if self.type_information is not None:
            dictionary['typeInformation'] = self.type_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(AdditionalOrderInput, self).from_dictionary(dictionary)
        if 'accountFundingRecipient' in dictionary:
            if not isinstance(dictionary['accountFundingRecipient'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['accountFundingRecipient']))
            value = AccountFundingRecipient()
            self.account_funding_recipient = value.from_dictionary(dictionary['accountFundingRecipient'])
        if 'airlineData' in dictionary:
            if not isinstance(dictionary['airlineData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['airlineData']))
            value = AirlineData()
            self.airline_data = value.from_dictionary(dictionary['airlineData'])
        if 'installments' in dictionary:
            if not isinstance(dictionary['installments'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['installments']))
            value = Installments()
            self.installments = value.from_dictionary(dictionary['installments'])
        if 'level3SummaryData' in dictionary:
            if not isinstance(dictionary['level3SummaryData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['level3SummaryData']))
            value = Level3SummaryData()
            self.level3_summary_data = value.from_dictionary(dictionary['level3SummaryData'])
        if 'loanRecipient' in dictionary:
            if not isinstance(dictionary['loanRecipient'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['loanRecipient']))
            value = LoanRecipient()
            self.loan_recipient = value.from_dictionary(dictionary['loanRecipient'])
        if 'lodgingData' in dictionary:
            if not isinstance(dictionary['lodgingData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['lodgingData']))
            value = LodgingData()
            self.lodging_data = value.from_dictionary(dictionary['lodgingData'])
        if 'numberOfInstallments' in dictionary:
            self.number_of_installments = dictionary['numberOfInstallments']
        if 'orderDate' in dictionary:
            self.order_date = dictionary['orderDate']
        if 'typeInformation' in dictionary:
            if not isinstance(dictionary['typeInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['typeInformation']))
            value = OrderTypeInformation()
            self.type_information = value.from_dictionary(dictionary['typeInformation'])
        return self
