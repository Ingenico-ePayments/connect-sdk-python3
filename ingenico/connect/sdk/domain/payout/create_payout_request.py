#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.payout.definitions.payout_customer import PayoutCustomer
from ingenico.connect.sdk.domain.payout.definitions.payout_references import PayoutReferences


class CreatePayoutRequest(DataObject):
    """
    Class CreatePayoutRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreatePayoutRequest
    """

    __amount_of_money = None
    __bank_account_bban = None
    __bank_account_iban = None
    __customer = None
    __payout_date = None
    __payout_text = None
    __references = None
    __swift_code = None

    @property
    def amount_of_money(self):
        """
        :class:`AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def bank_account_bban(self):
        """
        :class:`BankAccountBban`
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value):
        self.__bank_account_bban = value

    @property
    def bank_account_iban(self):
        """
        :class:`BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value):
        self.__bank_account_iban = value

    @property
    def customer(self):
        """
        :class:`PayoutCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def payout_date(self):
        """
        str
        """
        return self.__payout_date

    @payout_date.setter
    def payout_date(self, value):
        self.__payout_date = value

    @property
    def payout_text(self):
        """
        str
        """
        return self.__payout_text

    @payout_text.setter
    def payout_text(self, value):
        self.__payout_text = value

    @property
    def references(self):
        """
        :class:`PayoutReferences`
        """
        return self.__references

    @references.setter
    def references(self, value):
        self.__references = value

    @property
    def swift_code(self):
        """
        str
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
