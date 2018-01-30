# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.payout.definitions.bank_transfer_payout_method_specific_input import BankTransferPayoutMethodSpecificInput
from ingenico.connect.sdk.domain.payout.definitions.card_payout_method_specific_input import CardPayoutMethodSpecificInput
from ingenico.connect.sdk.domain.payout.definitions.payout_customer import PayoutCustomer
from ingenico.connect.sdk.domain.payout.definitions.payout_references import PayoutReferences


class CreatePayoutRequest(DataObject):

    __amount_of_money = None
    __bank_account_bban = None
    __bank_account_iban = None
    __bank_transfer_payout_method_specific_input = None
    __card_payout_method_specific_input = None
    __customer = None
    __payout_date = None
    __payout_text = None
    __references = None
    __swift_code = None

    @property
    def amount_of_money(self):
        """
        | Object containing amount and ISO currency code attributes
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def bank_account_bban(self):
        """
        | Object containing account holder name and bank account information. This field can only be used for payouts in the UK. Either a BBAN account or an IBAN account should be provided, but not both
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.bank_account_bban.BankAccountBban`
        
        Deprecated; | Use bankTransferPayoutMethodSpecificInput.bankAccountBban instead
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value):
        self.__bank_account_bban = value

    @property
    def bank_account_iban(self):
        """
        | Object containing account holder and IBAN information. Either a BBAN account or an IBAN account should be provided, but not both
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.bank_account_iban.BankAccountIban`
        
        Deprecated; | Use bankTransferPayoutMethodSpecificInput.bankAccountIban instead
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value):
        self.__bank_account_iban = value

    @property
    def bank_transfer_payout_method_specific_input(self):
        """
        | Object containing the specific input details for bank transfer payouts.
        
        Type: :class:`ingenico.connect.sdk.domain.payout.definitions.bank_transfer_payout_method_specific_input.BankTransferPayoutMethodSpecificInput`
        """
        return self.__bank_transfer_payout_method_specific_input

    @bank_transfer_payout_method_specific_input.setter
    def bank_transfer_payout_method_specific_input(self, value):
        self.__bank_transfer_payout_method_specific_input = value

    @property
    def card_payout_method_specific_input(self):
        """
        | Object containing the specific input details for card payouts.
        
        Type: :class:`ingenico.connect.sdk.domain.payout.definitions.card_payout_method_specific_input.CardPayoutMethodSpecificInput`
        """
        return self.__card_payout_method_specific_input

    @card_payout_method_specific_input.setter
    def card_payout_method_specific_input(self, value):
        self.__card_payout_method_specific_input = value

    @property
    def customer(self):
        """
        | Object containing the details of the consumer.
        
        Type: :class:`ingenico.connect.sdk.domain.payout.definitions.payout_customer.PayoutCustomer`
        
        Deprecated; | Use bankTransferPayoutMethodSpecificInput.customer instead
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def payout_date(self):
        """
        | Date of the payout sent to the bank by us
        | Format: YYYYMMDD
        
        Type: str
        
        Deprecated; | Use bankTransferPayoutMethodSpecificInput.payoutDate instead
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
        
        Deprecated; | Use bankTransferPayoutMethodSpecificInput.payoutText instead
        """
        return self.__payout_text

    @payout_text.setter
    def payout_text(self, value):
        self.__payout_text = value

    @property
    def references(self):
        """
        | Object that holds all reference fields that are linked to this transaction
        
        Type: :class:`ingenico.connect.sdk.domain.payout.definitions.payout_references.PayoutReferences`
        """
        return self.__references

    @references.setter
    def references(self, value):
        self.__references = value

    @property
    def swift_code(self):
        """
        | The BIC is the Business Identifier Code, also known as SWIFT or Bank Identifier code. It is a code with an internationally agreed format to Identify a specific bank. The BIC contains 8 or 11 positions: the first 4 contain the bank code, followed by the country code and location code.
        
        Type: str
        
        Deprecated; | Use bankTransferPayoutMethodSpecificInput.swiftCode instead
        """
        return self.__swift_code

    @swift_code.setter
    def swift_code(self, value):
        self.__swift_code = value

    def to_dictionary(self):
        dictionary = super(CreatePayoutRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountOfMoney', self.amount_of_money)
        self._add_to_dictionary(dictionary, 'bankAccountBban', self.bank_account_bban)
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        self._add_to_dictionary(dictionary, 'bankTransferPayoutMethodSpecificInput', self.bank_transfer_payout_method_specific_input)
        self._add_to_dictionary(dictionary, 'cardPayoutMethodSpecificInput', self.card_payout_method_specific_input)
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'payoutDate', self.payout_date)
        self._add_to_dictionary(dictionary, 'payoutText', self.payout_text)
        self._add_to_dictionary(dictionary, 'references', self.references)
        self._add_to_dictionary(dictionary, 'swiftCode', self.swift_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePayoutRequest, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
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
        if 'bankTransferPayoutMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['bankTransferPayoutMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankTransferPayoutMethodSpecificInput']))
            value = BankTransferPayoutMethodSpecificInput()
            self.bank_transfer_payout_method_specific_input = value.from_dictionary(dictionary['bankTransferPayoutMethodSpecificInput'])
        if 'cardPayoutMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPayoutMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPayoutMethodSpecificInput']))
            value = CardPayoutMethodSpecificInput()
            self.card_payout_method_specific_input = value.from_dictionary(dictionary['cardPayoutMethodSpecificInput'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = PayoutCustomer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'payoutDate' in dictionary:
            self.payout_date = dictionary['payoutDate']
        if 'payoutText' in dictionary:
            self.payout_text = dictionary['payoutText']
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PayoutReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'swiftCode' in dictionary:
            self.swift_code = dictionary['swiftCode']
        return self
