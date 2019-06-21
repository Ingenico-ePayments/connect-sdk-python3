# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.payout.definitions.abstract_payout_method_specific_input import AbstractPayoutMethodSpecificInput
from ingenico.connect.sdk.domain.payout.definitions.payout_customer import PayoutCustomer


class BankTransferPayoutMethodSpecificInput(AbstractPayoutMethodSpecificInput):

    __bank_account_bban = None
    __bank_account_iban = None
    __customer = None
    __payout_date = None
    __payout_text = None
    __swift_code = None

    @property
    def bank_account_bban(self):
        """
        | Object containing account holder name and bank account information. This property can only be used for payouts in the UK.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.bank_account_bban.BankAccountBban`
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value):
        self.__bank_account_bban = value

    @property
    def bank_account_iban(self):
        """
        | Object containing account holder and IBAN information.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.bank_account_iban.BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value):
        self.__bank_account_iban = value

    @property
    def customer(self):
        """
        | Object containing the details of the customer.
        
        Type: :class:`ingenico.connect.sdk.domain.payout.definitions.payout_customer.PayoutCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def payout_date(self):
        """
        | Date of the payout sent to the bank by us.
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__payout_date

    @payout_date.setter
    def payout_date(self, value):
        self.__payout_date = value

    @property
    def payout_text(self):
        """
        | Text to be printed on the bank account statement of the beneficiary. The maximum allowed length might differ per country. The data will be automatically truncated to the maximum allowed length.
        
        Type: str
        """
        return self.__payout_text

    @payout_text.setter
    def payout_text(self, value):
        self.__payout_text = value

    @property
    def swift_code(self):
        """
        | The BIC is the Business Identifier Code, also known as SWIFT or Bank Identifier code. It is a code with an internationally agreed format to Identify a specific bank. The BIC contains 8 or 11 positions: the first 4 contain the bank code, followed by the country code and location code.
        
        Type: str
        """
        return self.__swift_code

    @swift_code.setter
    def swift_code(self, value):
        self.__swift_code = value

    def to_dictionary(self):
        dictionary = super(BankTransferPayoutMethodSpecificInput, self).to_dictionary()
        if self.bank_account_bban is not None:
            dictionary['bankAccountBban'] = self.bank_account_bban.to_dictionary()
        if self.bank_account_iban is not None:
            dictionary['bankAccountIban'] = self.bank_account_iban.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.payout_date is not None:
            dictionary['payoutDate'] = self.payout_date
        if self.payout_text is not None:
            dictionary['payoutText'] = self.payout_text
        if self.swift_code is not None:
            dictionary['swiftCode'] = self.swift_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankTransferPayoutMethodSpecificInput, self).from_dictionary(dictionary)
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = PayoutCustomer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'payoutDate' in dictionary:
            self.payout_date = dictionary['payoutDate']
        if 'payoutText' in dictionary:
            self.payout_text = dictionary['payoutText']
        if 'swiftCode' in dictionary:
            self.swift_code = dictionary['swiftCode']
        return self
