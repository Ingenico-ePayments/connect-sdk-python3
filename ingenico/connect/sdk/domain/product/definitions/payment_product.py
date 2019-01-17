# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.account_on_file import AccountOnFile
from ingenico.connect.sdk.domain.product.definitions.authentication_indicator import AuthenticationIndicator
from ingenico.connect.sdk.domain.product.definitions.payment_product302_specific_data import PaymentProduct302SpecificData
from ingenico.connect.sdk.domain.product.definitions.payment_product320_specific_data import PaymentProduct320SpecificData
from ingenico.connect.sdk.domain.product.definitions.payment_product863_specific_data import PaymentProduct863SpecificData
from ingenico.connect.sdk.domain.product.definitions.payment_product_display_hints import PaymentProductDisplayHints
from ingenico.connect.sdk.domain.product.definitions.payment_product_field import PaymentProductField


class PaymentProduct(DataObject):

    __accounts_on_file = None
    __allows_recurring = None
    __allows_tokenization = None
    __authentication_indicator = None
    __auto_tokenized = None
    __can_be_iframed = None
    __device_fingerprint_enabled = None
    __display_hints = None
    __fields = None
    __fields_warning = None
    __id = None
    __is_java_script_required = None
    __max_amount = None
    __min_amount = None
    __mobile_integration_level = None
    __payment_method = None
    __payment_product302_specific_data = None
    __payment_product320_specific_data = None
    __payment_product863_specific_data = None
    __payment_product_group = None
    __uses_redirection_to3rd_party = None

    @property
    def accounts_on_file(self):
        """
        | List of tokens for that payment product
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.account_on_file.AccountOnFile`]
        """
        return self.__accounts_on_file

    @accounts_on_file.setter
    def accounts_on_file(self, value):
        self.__accounts_on_file = value

    @property
    def allows_recurring(self):
        """
        | Indicates if the product supports recurring payments
        
        * true - This payment product supports recurring payments
        * false - This payment product does not support recurring transactions and can only be used for one-off payments
        
        Type: bool
        """
        return self.__allows_recurring

    @allows_recurring.setter
    def allows_recurring(self, value):
        self.__allows_recurring = value

    @property
    def allows_tokenization(self):
        """
        | Indicates if the payment details can be tokenized for future re-use
        
        * true - Payment details from payments done with this payment product can be tokenized for future re-use
        * false - Payment details from payments done with this payment product can not be tokenized
        
        Type: bool
        """
        return self.__allows_tokenization

    @allows_tokenization.setter
    def allows_tokenization(self, value):
        self.__allows_tokenization = value

    @property
    def authentication_indicator(self):
        """
        | Indicates if the payment product supports 3D Security (mandatory, optional or not needed).
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.authentication_indicator.AuthenticationIndicator`
        """
        return self.__authentication_indicator

    @authentication_indicator.setter
    def authentication_indicator(self, value):
        self.__authentication_indicator = value

    @property
    def auto_tokenized(self):
        """
        | Indicates if the payment details can be automatically tokenized for future re-use
        
        * true - Payment details from payments done with this payment product can be automatically tokenized for future re-use
        * false - Payment details from payments done with this payment product can not be automatically tokenized
        
        Type: bool
        """
        return self.__auto_tokenized

    @auto_tokenized.setter
    def auto_tokenized(self, value):
        self.__auto_tokenized = value

    @property
    def can_be_iframed(self):
        """
        | This field is only relevant for payment products that use third party redirects. This field indicates if the third party disallows their payment pages to be embedded in an iframe using the X-Frame-Options header.
        
        * true - the third party allows their payment pages to be embedded in an iframe.
        * false - the third party disallows their payment pages to be embedded in an iframe.
        
        Type: bool
        """
        return self.__can_be_iframed

    @can_be_iframed.setter
    def can_be_iframed(self, value):
        self.__can_be_iframed = value

    @property
    def device_fingerprint_enabled(self):
        """
        | Indicates if device fingerprint is enabled for the product
        
        * true
        * false
        
        Type: bool
        """
        return self.__device_fingerprint_enabled

    @device_fingerprint_enabled.setter
    def device_fingerprint_enabled(self, value):
        self.__device_fingerprint_enabled = value

    @property
    def display_hints(self):
        """
        | Object containing display hints like the order in which the product should be shown, the name of the product and the logo
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product_display_hints.PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def fields(self):
        """
        | Object containing all the fields and their details that are associated with this payment product. If you are not interested in the data on the fields you should have us filter them our (using filter=fields in the query-string)
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.payment_product_field.PaymentProductField`]
        """
        return self.__fields

    @fields.setter
    def fields(self, value):
        self.__fields = value

    @property
    def fields_warning(self):
        """
        | If one or more of the payment product fields could not be constructed, no payment product fields will be returned and a message will be present in this field stating why.
        
        Type: str
        """
        return self.__fields_warning

    @fields_warning.setter
    def fields_warning(self, value):
        self.__fields_warning = value

    @property
    def id(self):
        """
        | The ID of the payment product in our system
        
        Type: int
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def is_java_script_required(self):
        """
        | This fields indicates if the payment product requires JavaScript to be enabled on the customer's browser. This is usually only true if the payment product depends on a third party JavaScript integration.
        
        * true - the payment product requires JavaScript to be enabled.
        * false - the payment product does not require JavaScript to be enabled. This is the default value if the field is not present.
        
        Type: bool
        """
        return self.__is_java_script_required

    @is_java_script_required.setter
    def is_java_script_required(self, value):
        self.__is_java_script_required = value

    @property
    def max_amount(self):
        """
        | Maximum amount in EUR cents (using 2 decimals, so 1 EUR becomes 100 cents) for transactions done with this payment product
        
        Type: int
        """
        return self.__max_amount

    @max_amount.setter
    def max_amount(self, value):
        self.__max_amount = value

    @property
    def min_amount(self):
        """
        | Minimum amount in EUR cents (using 2 decimals, so 1 EUR becomes 100 cents) for transactions done with this payment product
        
        Type: int
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value):
        self.__min_amount = value

    @property
    def mobile_integration_level(self):
        """
        | This provides insight into the level of support for payments using a device with a smaller screen size. You can for instance use this to rank payment products differently on devices with a smaller screen. Possible values are:
        
        * NO_SUPPORT - The payment product does not work at all on a mobile device
        * BASIC_SUPPORT - The payment product has not optimized its user experience for devices with smaller screens
        * OPTIMISED_SUPPORT - The payment product offers a user experience that has been optimized for devices with smaller screens
        
        Type: str
        """
        return self.__mobile_integration_level

    @mobile_integration_level.setter
    def mobile_integration_level(self, value):
        self.__mobile_integration_level = value

    @property
    def payment_method(self):
        """
        | Indicates which payment method will be used for this payment product. Payment method is one of:
        
        * bankTransfer
        * card
        * cash
        * directDebit
        * eInvoice
        * invoice
        * redirect
        
        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    @property
    def payment_product302_specific_data(self):
        """
        | Apple Pay (payment product 302) specific details.
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product302_specific_data.PaymentProduct302SpecificData`
        """
        return self.__payment_product302_specific_data

    @payment_product302_specific_data.setter
    def payment_product302_specific_data(self, value):
        self.__payment_product302_specific_data = value

    @property
    def payment_product320_specific_data(self):
        """
        | Google Pay (payment product 320) specific details.
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product320_specific_data.PaymentProduct320SpecificData`
        """
        return self.__payment_product320_specific_data

    @payment_product320_specific_data.setter
    def payment_product320_specific_data(self, value):
        self.__payment_product320_specific_data = value

    @property
    def payment_product863_specific_data(self):
        """
        | WeChat Pay (payment product 863) specific details.
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product863_specific_data.PaymentProduct863SpecificData`
        """
        return self.__payment_product863_specific_data

    @payment_product863_specific_data.setter
    def payment_product863_specific_data(self, value):
        self.__payment_product863_specific_data = value

    @property
    def payment_product_group(self):
        """
        | The payment product group that has this payment product, if there is any. Not populated otherwise. Currently only one payment product group is supported:
        
        * cards
        
        Type: str
        """
        return self.__payment_product_group

    @payment_product_group.setter
    def payment_product_group(self, value):
        self.__payment_product_group = value

    @property
    def uses_redirection_to3rd_party(self):
        """
        | Indicates whether the payment product requires redirection to a third party to complete the payment. You can use this to filter out products that require a redirect if you don't want to support that.
        
        * true - Redirection is required
        * false - No redirection is required
        
        Type: bool
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
        self._add_to_dictionary(dictionary, 'authenticationIndicator', self.authentication_indicator)
        self._add_to_dictionary(dictionary, 'autoTokenized', self.auto_tokenized)
        self._add_to_dictionary(dictionary, 'canBeIframed', self.can_be_iframed)
        self._add_to_dictionary(dictionary, 'deviceFingerprintEnabled', self.device_fingerprint_enabled)
        self._add_to_dictionary(dictionary, 'displayHints', self.display_hints)
        self._add_to_dictionary(dictionary, 'fields', self.fields)
        self._add_to_dictionary(dictionary, 'fieldsWarning', self.fields_warning)
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'isJavaScriptRequired', self.is_java_script_required)
        self._add_to_dictionary(dictionary, 'maxAmount', self.max_amount)
        self._add_to_dictionary(dictionary, 'minAmount', self.min_amount)
        self._add_to_dictionary(dictionary, 'mobileIntegrationLevel', self.mobile_integration_level)
        self._add_to_dictionary(dictionary, 'paymentMethod', self.payment_method)
        self._add_to_dictionary(dictionary, 'paymentProduct302SpecificData', self.payment_product302_specific_data)
        self._add_to_dictionary(dictionary, 'paymentProduct320SpecificData', self.payment_product320_specific_data)
        self._add_to_dictionary(dictionary, 'paymentProduct863SpecificData', self.payment_product863_specific_data)
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
        if 'authenticationIndicator' in dictionary:
            if not isinstance(dictionary['authenticationIndicator'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['authenticationIndicator']))
            value = AuthenticationIndicator()
            self.authentication_indicator = value.from_dictionary(dictionary['authenticationIndicator'])
        if 'autoTokenized' in dictionary:
            self.auto_tokenized = dictionary['autoTokenized']
        if 'canBeIframed' in dictionary:
            self.can_be_iframed = dictionary['canBeIframed']
        if 'deviceFingerprintEnabled' in dictionary:
            self.device_fingerprint_enabled = dictionary['deviceFingerprintEnabled']
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
        if 'fieldsWarning' in dictionary:
            self.fields_warning = dictionary['fieldsWarning']
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'isJavaScriptRequired' in dictionary:
            self.is_java_script_required = dictionary['isJavaScriptRequired']
        if 'maxAmount' in dictionary:
            self.max_amount = dictionary['maxAmount']
        if 'minAmount' in dictionary:
            self.min_amount = dictionary['minAmount']
        if 'mobileIntegrationLevel' in dictionary:
            self.mobile_integration_level = dictionary['mobileIntegrationLevel']
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'paymentProduct302SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct302SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct302SpecificData']))
            value = PaymentProduct302SpecificData()
            self.payment_product302_specific_data = value.from_dictionary(dictionary['paymentProduct302SpecificData'])
        if 'paymentProduct320SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificData']))
            value = PaymentProduct320SpecificData()
            self.payment_product320_specific_data = value.from_dictionary(dictionary['paymentProduct320SpecificData'])
        if 'paymentProduct863SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct863SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct863SpecificData']))
            value = PaymentProduct863SpecificData()
            self.payment_product863_specific_data = value.from_dictionary(dictionary['paymentProduct863SpecificData'])
        if 'paymentProductGroup' in dictionary:
            self.payment_product_group = dictionary['paymentProductGroup']
        if 'usesRedirectionTo3rdParty' in dictionary:
            self.uses_redirection_to3rd_party = dictionary['usesRedirectionTo3rdParty']
        return self
