# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban


class NonSepaDirectDebitPaymentProduct705SpecificInput(DataObject):
    """
    | UK Direct Debit specific input fields
    """

    __authorisation_id = None
    __bank_account_bban = None
    __transaction_type = None

    @property
    def authorisation_id(self):
        """
        | Core reference number for the direct debit instruction in UK
        
        Type: str
        """
        return self.__authorisation_id

    @authorisation_id.setter
    def authorisation_id(self, value):
        self.__authorisation_id = value

    @property
    def bank_account_bban(self):
        """
        | Object containing account holder name and bank account information
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.bank_account_bban.BankAccountBban`
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value):
        self.__bank_account_bban = value

    @property
    def transaction_type(self):
        """
        * first-payment - First payment direct debit
        * nth-payment - Direct Debit (n-th payment)
        * re-presented - Re-presented direct debit (after failed attempt)
        * final-payment - Final payment direct debit
        * new-or-reinstated - (zero N) New or reinstated direct debit instruction
        * cancellation - (zero C) Cancellation of direct debit instruction
        * conversion-of-paper-DDI-to-electronic-DDI - (zero S) Conversion of paper DDI to electronic DDI (only used once, when migrating from traditional direct debit to AUDDIS
        
        Type: str
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self.__transaction_type = value

    def to_dictionary(self):
        dictionary = super(NonSepaDirectDebitPaymentProduct705SpecificInput, self).to_dictionary()
        if self.authorisation_id is not None:
            dictionary['authorisationId'] = self.authorisation_id
        if self.bank_account_bban is not None:
            dictionary['bankAccountBban'] = self.bank_account_bban.to_dictionary()
        if self.transaction_type is not None:
            dictionary['transactionType'] = self.transaction_type
        return dictionary

    def from_dictionary(self, dictionary):
        super(NonSepaDirectDebitPaymentProduct705SpecificInput, self).from_dictionary(dictionary)
        if 'authorisationId' in dictionary:
            self.authorisation_id = dictionary['authorisationId']
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        if 'transactionType' in dictionary:
            self.transaction_type = dictionary['transactionType']
        return self
