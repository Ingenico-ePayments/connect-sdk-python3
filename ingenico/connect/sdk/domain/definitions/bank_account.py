#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class BankAccount(DataObject):
    """
    Class BankAccount
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankAccount
    
    Attributes:
        account_holder_name:  str
     """

    account_holder_name = None

    def to_dictionary(self):
        dictionary = super(BankAccount, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'accountHolderName', self.account_holder_name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccount, self).from_dictionary(dictionary)
        if 'accountHolderName' in dictionary:
            self.account_holder_name = dictionary['accountHolderName']
        return self
