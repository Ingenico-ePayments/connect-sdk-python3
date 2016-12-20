#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.bank_account import BankAccount


class BankAccountIban(BankAccount):
    """
    Class BankAccountIban
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankAccountIban
    """

    __iban = None

    @property
    def iban(self):
        """
        str
        """
        return self.__iban

    @iban.setter
    def iban(self, value):
        self.__iban = value

    def to_dictionary(self):
        dictionary = super(BankAccountIban, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'iban', self.iban)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccountIban, self).from_dictionary(dictionary)
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        return self
