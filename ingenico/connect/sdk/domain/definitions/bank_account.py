#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class BankAccount(DataObject):
    """
    Class BankAccount
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankAccount
    """

    __account_holder_name = None

    @property
    def account_holder_name(self):
        """
        str
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self.__account_holder_name = value

    def to_dictionary(self):
        dictionary = super(BankAccount, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'accountHolderName', self.account_holder_name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccount, self).from_dictionary(dictionary)
        if 'accountHolderName' in dictionary:
            self.account_holder_name = dictionary['accountHolderName']
        return self
