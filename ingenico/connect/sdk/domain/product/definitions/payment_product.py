#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.account_on_file import AccountOnFile
from ingenico.connect.sdk.domain.product.definitions.payment_product_display_hints import PaymentProductDisplayHints
from ingenico.connect.sdk.domain.product.definitions.payment_product_field import PaymentProductField


class PaymentProduct(DataObject):
    """
    Class PaymentProduct
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProduct
    
    Attributes:
        accounts_on_file:              list[:class:`AccountOnFile`]
        allows_recurring:              bool
        allows_tokenization:           bool
        auto_tokenized:                bool
        display_hints:                 :class:`PaymentProductDisplayHints`
        fields:                        list[:class:`PaymentProductField`]
        id:                            int
        max_amount:                    int
        min_amount:                    int
        mobile_integration_level:      str
        payment_method:                str
        payment_product_group:         str
        uses_redirection_to3rd_party:  bool
     """

    accounts_on_file = None
    allows_recurring = None
    allows_tokenization = None
    auto_tokenized = None
    display_hints = None
    fields = None
    id = None
    max_amount = None
    min_amount = None
    mobile_integration_level = None
    payment_method = None
    payment_product_group = None
    uses_redirection_to3rd_party = None

    def to_dictionary(self):
        dictionary = super(PaymentProduct, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'accountsOnFile', self.accounts_on_file)
        self._add_to_dictionary(dictionary, 'allowsRecurring', self.allows_recurring)
        self._add_to_dictionary(dictionary, 'allowsTokenization', self.allows_tokenization)
        self._add_to_dictionary(dictionary, 'autoTokenized', self.auto_tokenized)
        self._add_to_dictionary(dictionary, 'displayHints', self.display_hints)
        self._add_to_dictionary(dictionary, 'fields', self.fields)
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'maxAmount', self.max_amount)
        self._add_to_dictionary(dictionary, 'minAmount', self.min_amount)
        self._add_to_dictionary(dictionary, 'mobileIntegrationLevel', self.mobile_integration_level)
        self._add_to_dictionary(dictionary, 'paymentMethod', self.payment_method)
        self._add_to_dictionary(dictionary, 'paymentProductGroup', self.payment_product_group)
        self._add_to_dictionary(dictionary, 'usesRedirectionTo3rdParty', self.uses_redirection_to3rd_party)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct, self).from_dictionary(dictionary)
        if 'accountsOnFile' in dictionary:
            if not isinstance(dictionary['accountsOnFile'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['accountsOnFile']))
            self.accounts_on_file = []
            for accountsOnFile_element in dictionary['accountsOnFile']:
                accountsOnFile_value = AccountOnFile()
                self.accounts_on_file.append(accountsOnFile_value.from_dictionary(accountsOnFile_element))
        if 'allowsRecurring' in dictionary:
            self.allows_recurring = dictionary['allowsRecurring']
        if 'allowsTokenization' in dictionary:
            self.allows_tokenization = dictionary['allowsTokenization']
        if 'autoTokenized' in dictionary:
            self.auto_tokenized = dictionary['autoTokenized']
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'fields' in dictionary:
            if not isinstance(dictionary['fields'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['fields']))
            self.fields = []
            for fields_element in dictionary['fields']:
                fields_value = PaymentProductField()
                self.fields.append(fields_value.from_dictionary(fields_element))
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'maxAmount' in dictionary:
            self.max_amount = dictionary['maxAmount']
        if 'minAmount' in dictionary:
            self.min_amount = dictionary['minAmount']
        if 'mobileIntegrationLevel' in dictionary:
            self.mobile_integration_level = dictionary['mobileIntegrationLevel']
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'paymentProductGroup' in dictionary:
            self.payment_product_group = dictionary['paymentProductGroup']
        if 'usesRedirectionTo3rdParty' in dictionary:
            self.uses_redirection_to3rd_party = dictionary['usesRedirectionTo3rdParty']
        return self
