#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban


class TokenNonSepaDirectDebitPaymentProduct707SpecificData(DataObject):
    """
    Class TokenNonSepaDirectDebitPaymentProduct707SpecificData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenNonSepaDirectDebitPaymentProduct707SpecificData
    
    Attributes:
        address_line1:      str
        address_line2:      str
        address_line3:      str
        address_line4:      str
        bank_account_iban:  :class:`BankAccountIban`
     """

    address_line1 = None
    address_line2 = None
    address_line3 = None
    address_line4 = None
    bank_account_iban = None

    def to_dictionary(self):
        dictionary = super(TokenNonSepaDirectDebitPaymentProduct707SpecificData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'addressLine1', self.address_line1)
        self._add_to_dictionary(dictionary, 'addressLine2', self.address_line2)
        self._add_to_dictionary(dictionary, 'addressLine3', self.address_line3)
        self._add_to_dictionary(dictionary, 'addressLine4', self.address_line4)
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenNonSepaDirectDebitPaymentProduct707SpecificData, self).from_dictionary(dictionary)
        if 'addressLine1' in dictionary:
            self.address_line1 = dictionary['addressLine1']
        if 'addressLine2' in dictionary:
            self.address_line2 = dictionary['addressLine2']
        if 'addressLine3' in dictionary:
            self.address_line3 = dictionary['addressLine3']
        if 'addressLine4' in dictionary:
            self.address_line4 = dictionary['addressLine4']
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        return self
