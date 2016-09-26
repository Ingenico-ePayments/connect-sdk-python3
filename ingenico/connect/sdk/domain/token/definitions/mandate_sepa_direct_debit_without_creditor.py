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
    
    Attributes:
        bank_account_iban:             :class:`BankAccountIban`
        customer_contract_identifier:  str
        debtor:                        :class:`Debtor`
        is_recurring:                  bool
        mandate_approval:              :class:`MandateApproval`
        pre_notification:              str
     """

    bank_account_iban = None
    customer_contract_identifier = None
    debtor = None
    is_recurring = None
    mandate_approval = None
    pre_notification = None

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
