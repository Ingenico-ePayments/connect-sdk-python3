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
    
    Attributes:
        amount_of_money:    :class:`AmountOfMoney`
        bank_account_bban:  :class:`BankAccountBban`
        bank_account_iban:  :class:`BankAccountIban`
        customer:           :class:`PayoutCustomer`
        payout_date:        str
        payout_text:        str
        references:         :class:`PayoutReferences`
        swift_code:         str
     """

    amount_of_money = None
    bank_account_bban = None
    bank_account_iban = None
    customer = None
    payout_date = None
    payout_text = None
    references = None
    swift_code = None

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
