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
    """

    __accounts_on_file = None
    __allows_recurring = None
    __allows_tokenization = None
    __auto_tokenized = None
    __can_be_iframed = None
    __display_hints = None
    __fields = None
    __id = None
    __max_amount = None
    __min_amount = None
    __mobile_integration_level = None
    __payment_method = None
    __payment_product_group = None
    __uses_redirection_to3rd_party = None

    @property
    def accounts_on_file(self):
        """
        list[:class:`AccountOnFile`]
        """
        return self.__accounts_on_file

    @accounts_on_file.setter
    def accounts_on_file(self, value):
        self.__accounts_on_file = value

    @property
    def allows_recurring(self):
        """
        bool
        """
        return self.__allows_recurring

    @allows_recurring.setter
    def allows_recurring(self, value):
        self.__allows_recurring = value

    @property
    def allows_tokenization(self):
        """
        bool
        """
        return self.__allows_tokenization

    @allows_tokenization.setter
    def allows_tokenization(self, value):
        self.__allows_tokenization = value

    @property
    def auto_tokenized(self):
        """
        bool
        """
        return self.__auto_tokenized

    @auto_tokenized.setter
    def auto_tokenized(self, value):
        self.__auto_tokenized = value

    @property
    def can_be_iframed(self):
        """
        bool
        """
        return self.__can_be_iframed

    @can_be_iframed.setter
    def can_be_iframed(self, value):
        self.__can_be_iframed = value

    @property
    def display_hints(self):
        """
        :class:`PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def fields(self):
        """
        list[:class:`PaymentProductField`]
        """
        return self.__fields

    @fields.setter
    def fields(self, value):
        self.__fields = value

    @property
    def id(self):
        """
        int
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def max_amount(self):
        """
        int
        """
        return self.__max_amount

    @max_amount.setter
    def max_amount(self, value):
        self.__max_amount = value

    @property
    def min_amount(self):
        """
        int
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value):
        self.__min_amount = value

    @property
    def mobile_integration_level(self):
        """
        str
        """
        return self.__mobile_integration_level

    @mobile_integration_level.setter
    def mobile_integration_level(self, value):
        self.__mobile_integration_level = value

    @property
    def payment_method(self):
        """
        str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    @property
    def payment_product_group(self):
        """
        str
        """
        return self.__payment_product_group

    @payment_product_group.setter
    def payment_product_group(self, value):
        self.__payment_product_group = value

    @property
    def uses_redirection_to3rd_party(self):
        """
        bool
        """
        return self.__uses_redirection_to3rd_party

    @uses_redirection_to3rd_party.setter
    def uses_redirection_to3rd_party(self, value):
        self.__uses_redirection_to3rd_party = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'accountsOnFile', self.accounts_on_file)
        self._add_to_dictionary(dictionary, 'allowsRecurring', self.allows_recurring)
        self._add_to_dictionary(dictionary, 'allowsTokenization', self.allows_tokenization)
        self._add_to_dictionary(dictionary, 'autoTokenized', self.auto_tokenized)
        self._add_to_dictionary(dictionary, 'canBeIframed', self.can_be_iframed)
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
        if 'canBeIframed' in dictionary:
            self.can_be_iframed = dictionary['canBeIframed']
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
