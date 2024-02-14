# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.payment.definitions.afr_name import AfrName


class AccountFundingRecipient(DataObject):
    """
    | Object containing specific data regarding the recipient of an account funding transaction
    """

    __account_number = None
    __account_number_type = None
    __address = None
    __date_of_birth = None
    __name = None
    __partial_pan = None

    @property
    def account_number(self):
        """
        | Should be populated with the value of the corresponding accountNumberType of the recipient.
        
        Type: str
        """
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def account_number_type(self):
        """
        | Defines the account number type of the recipient. Possible values are:
        
        * cash = Mode of payment is cash to the recipient.
        * walletId = Digital wallet ID.
        * routingNumber = Routing Transit Number is a code used by financial institutions to identify other financial institutions.
        * iban = International Bank Account Number, is a standard international numbering system for identifying bank accounts.
        * bicNumber = Bank Identification Code is a number that is used to identify a specific bank.
        * giftCard = Gift card is a type of prepaid card that contains a specific amount of money that can be used at participating stores and marketplaces.
        
        Type: str
        """
        return self.__account_number_type

    @account_number_type.setter
    def account_number_type(self, value):
        self.__account_number_type = value

    @property
    def address(self):
        """
        | Object containing the address details of the recipient of an account funding transaction.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def date_of_birth(self):
        """
        | The date of birth of the recipient
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @property
    def name(self):
        """
        | Object containing the name details of the recipient of an account funding transaction.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.afr_name.AfrName`
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def partial_pan(self):
        """
        | Either partialPan or accountnumber is required for merchants that use Merchant Category Code (MCC) 6012 for transactions involving UK costumers.
        
        Type: str
        """
        return self.__partial_pan

    @partial_pan.setter
    def partial_pan(self, value):
        self.__partial_pan = value

    def to_dictionary(self):
        dictionary = super(AccountFundingRecipient, self).to_dictionary()
        if self.account_number is not None:
            dictionary['accountNumber'] = self.account_number
        if self.account_number_type is not None:
            dictionary['accountNumberType'] = self.account_number_type
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.date_of_birth is not None:
            dictionary['dateOfBirth'] = self.date_of_birth
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        if self.partial_pan is not None:
            dictionary['partialPan'] = self.partial_pan
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountFundingRecipient, self).from_dictionary(dictionary)
        if 'accountNumber' in dictionary:
            self.account_number = dictionary['accountNumber']
        if 'accountNumberType' in dictionary:
            self.account_number_type = dictionary['accountNumberType']
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = Address()
            self.address = value.from_dictionary(dictionary['address'])
        if 'dateOfBirth' in dictionary:
            self.date_of_birth = dictionary['dateOfBirth']
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = AfrName()
            self.name = value.from_dictionary(dictionary['name'])
        if 'partialPan' in dictionary:
            self.partial_pan = dictionary['partialPan']
        return self
