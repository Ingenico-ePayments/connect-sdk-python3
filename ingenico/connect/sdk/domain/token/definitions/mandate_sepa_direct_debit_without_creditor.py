#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.token.definitions.debtor import Debtor
from ingenico.connect.sdk.domain.token.definitions.mandate_approval import MandateApproval


class MandateSepaDirectDebitWithoutCreditor(DataObject):
    """
    Class MandateSepaDirectDebitWithoutCreditor
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MandateSepaDirectDebitWithoutCreditor
    """

    __bank_account_iban = None
    __customer_contract_identifier = None
    __debtor = None
    __is_recurring = None
    __mandate_approval = None
    __pre_notification = None

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
    def customer_contract_identifier(self):
        """
        str
        """
        return self.__customer_contract_identifier

    @customer_contract_identifier.setter
    def customer_contract_identifier(self, value):
        self.__customer_contract_identifier = value

    @property
    def debtor(self):
        """
        :class:`Debtor`
        """
        return self.__debtor

    @debtor.setter
    def debtor(self, value):
        self.__debtor = value

    @property
    def is_recurring(self):
        """
        bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def mandate_approval(self):
        """
        :class:`MandateApproval`
        """
        return self.__mandate_approval

    @mandate_approval.setter
    def mandate_approval(self, value):
        self.__mandate_approval = value

    @property
    def pre_notification(self):
        """
        str
        """
        return self.__pre_notification

    @pre_notification.setter
    def pre_notification(self, value):
        self.__pre_notification = value

    def to_dictionary(self):
        dictionary = super(MandateSepaDirectDebitWithoutCreditor, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        self._add_to_dictionary(dictionary, 'customerContractIdentifier', self.customer_contract_identifier)
        self._add_to_dictionary(dictionary, 'debtor', self.debtor)
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        self._add_to_dictionary(dictionary, 'mandateApproval', self.mandate_approval)
        self._add_to_dictionary(dictionary, 'preNotification', self.pre_notification)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateSepaDirectDebitWithoutCreditor, self).from_dictionary(dictionary)
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'customerContractIdentifier' in dictionary:
            self.customer_contract_identifier = dictionary['customerContractIdentifier']
        if 'debtor' in dictionary:
            if not isinstance(dictionary['debtor'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['debtor']))
            value = Debtor()
            self.debtor = value.from_dictionary(dictionary['debtor'])
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'mandateApproval' in dictionary:
            if not isinstance(dictionary['mandateApproval'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandateApproval']))
            value = MandateApproval()
            self.mandate_approval = value.from_dictionary(dictionary['mandateApproval'])
        if 'preNotification' in dictionary:
            self.pre_notification = dictionary['preNotification']
        return self
