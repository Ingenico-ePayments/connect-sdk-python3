#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban


class BankAccountBbanRefund(BankAccountBban):
    """
    Class BankAccountBbanRefund
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankAccountBbanRefund
    
    Attributes:
        bank_city:   str
        swift_code:  str
     """

    bank_city = None
    swift_code = None

    def to_dictionary(self):
        dictionary = super(BankAccountBbanRefund, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankCity', self.bank_city)
        self._add_to_dictionary(dictionary, 'swiftCode', self.swift_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccountBbanRefund, self).from_dictionary(dictionary)
        if 'bankCity' in dictionary:
            self.bank_city = dictionary['bankCity']
        if 'swiftCode' in dictionary:
            self.swift_code = dictionary['swiftCode']
        return self
