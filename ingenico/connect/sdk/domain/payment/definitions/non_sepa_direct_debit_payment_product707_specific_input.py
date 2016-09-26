#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban


class NonSepaDirectDebitPaymentProduct707SpecificInput(DataObject):
    """
    Class NonSepaDirectDebitPaymentProduct707SpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_NonSepaDirectDebitPaymentProduct707SpecificInput
    
    Attributes:
        address_line1:         str
        address_line2:         str
        address_line3:         str
        address_line4:         str
        bank_account_iban:     :class:`BankAccountIban`
        customer_bank_city:    str
        customer_bank_number:  str
        customer_bank_street:  str
        customer_bank_zip:     str
     """

    address_line1 = None
    address_line2 = None
    address_line3 = None
    address_line4 = None
    bank_account_iban = None
    customer_bank_city = None
    customer_bank_number = None
    customer_bank_street = None
    customer_bank_zip = None

    def to_dictionary(self):
        dictionary = super(NonSepaDirectDebitPaymentProduct707SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'addressLine1', self.address_line1)
        self._add_to_dictionary(dictionary, 'addressLine2', self.address_line2)
        self._add_to_dictionary(dictionary, 'addressLine3', self.address_line3)
        self._add_to_dictionary(dictionary, 'addressLine4', self.address_line4)
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        self._add_to_dictionary(dictionary, 'customerBankCity', self.customer_bank_city)
        self._add_to_dictionary(dictionary, 'customerBankNumber', self.customer_bank_number)
        self._add_to_dictionary(dictionary, 'customerBankStreet', self.customer_bank_street)
        self._add_to_dictionary(dictionary, 'customerBankZip', self.customer_bank_zip)
        return dictionary

    def from_dictionary(self, dictionary):
        super(NonSepaDirectDebitPaymentProduct707SpecificInput, self).from_dictionary(dictionary)
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
        if 'customerBankCity' in dictionary:
            self.customer_bank_city = dictionary['customerBankCity']
        if 'customerBankNumber' in dictionary:
            self.customer_bank_number = dictionary['customerBankNumber']
        if 'customerBankStreet' in dictionary:
            self.customer_bank_street = dictionary['customerBankStreet']
        if 'customerBankZip' in dictionary:
            self.customer_bank_zip = dictionary['customerBankZip']
        return self
