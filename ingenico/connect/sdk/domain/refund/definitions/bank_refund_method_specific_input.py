#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.refund.definitions.bank_account_bban_refund import BankAccountBbanRefund


class BankRefundMethodSpecificInput(DataObject):
    """
    Class BankRefundMethodSpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankRefundMethodSpecificInput
    
    Attributes:
        bank_account_bban:  :class:`BankAccountBbanRefund`
        bank_account_iban:  :class:`BankAccountIban`
        country_code:       str
     """

    bank_account_bban = None
    bank_account_iban = None
    country_code = None

    def to_dictionary(self):
        dictionary = super(BankRefundMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankAccountBban', self.bank_account_bban)
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankRefundMethodSpecificInput, self).from_dictionary(dictionary)
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBbanRefund()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        return self
