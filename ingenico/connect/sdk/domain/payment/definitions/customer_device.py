# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.browser_data import BrowserData


class CustomerDevice(DataObject):
    """
    | Object containing information on the device and browser of the customer
    """

    __accept_header = None
    __browser_data = None
    __default_form_fill = None
    __device_fingerprint_transaction_id = None
    __ip_address = None
    __locale = None
    __timezone_offset_utc_minutes = None
    __user_agent = None

    @property
    def accept_header(self):
        """
        | The accept-header of the customer client from the HTTP Headers.
        
        Type: str
        """
        return self.__accept_header

    @accept_header.setter
    def accept_header(self, value):
        self.__accept_header = value

    @property
    def browser_data(self):
        """
        | Object containing information regarding the browser of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.browser_data.BrowserData`
        """
        return self.__browser_data

    @browser_data.setter
    def browser_data(self, value):
        self.__browser_data = value

    @property
    def default_form_fill(self):
        """
        | Degree of default form fill, with the following possible values:
        
        * automatically - All fields filled automatically
        * automatically-but-modified - All fields filled automatically, but some fields were modified manually
        * manually - All fields were entered manually
        
        Type: str
        """
        return self.__default_form_fill

    @default_form_fill.setter
    def default_form_fill(self, value):
        self.__default_form_fill = value

    @property
    def device_fingerprint_transaction_id(self):
        """
        | One must set the deviceFingerprintTransactionId received by the response of the endpoint /{merchant}/products/{paymentProductId}/deviceFingerprint
        
        Type: str
        """
        return self.__device_fingerprint_transaction_id

    @device_fingerprint_transaction_id.setter
    def device_fingerprint_transaction_id(self, value):
        self.__device_fingerprint_transaction_id = value

    @property
    def ip_address(self):
        """
        | The IP address of the customer client from the HTTP Headers.
        
        Type: str
        """
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value):
        self.__ip_address = value

    @property
    def locale(self):
        """
        | Locale of the client device/browser. Returned in the browser from the navigator.language property.
        
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.
        
        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def timezone_offset_utc_minutes(self):
        """
        | Offset in minutes of timezone of the client versus the UTC. Value is returned by the JavaScript getTimezoneOffset() Method.
        
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.
        
        Type: str
        """
        return self.__timezone_offset_utc_minutes

    @timezone_offset_utc_minutes.setter
    def timezone_offset_utc_minutes(self, value):
        self.__timezone_offset_utc_minutes = value

    @property
    def user_agent(self):
        """
        | User-Agent of the client device/browser from the HTTP Headers.
        
        | As a fall-back we will use the userAgent that might be included in the encryptedCustomerInput, but this is captured client side using JavaScript and might be different.
        
        Type: str
        """
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value):
        self.__user_agent = value

    def to_dictionary(self):
        dictionary = super(CustomerDevice, self).to_dictionary()
        if self.accept_header is not None:
            dictionary['acceptHeader'] = self.accept_header
        if self.browser_data is not None:
            dictionary['browserData'] = self.browser_data.to_dictionary()
        if self.default_form_fill is not None:
            dictionary['defaultFormFill'] = self.default_form_fill
        if self.device_fingerprint_transaction_id is not None:
            dictionary['deviceFingerprintTransactionId'] = self.device_fingerprint_transaction_id
        if self.ip_address is not None:
            dictionary['ipAddress'] = self.ip_address
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.timezone_offset_utc_minutes is not None:
            dictionary['timezoneOffsetUtcMinutes'] = self.timezone_offset_utc_minutes
        if self.user_agent is not None:
            dictionary['userAgent'] = self.user_agent
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerDevice, self).from_dictionary(dictionary)
        if 'acceptHeader' in dictionary:
            self.accept_header = dictionary['acceptHeader']
        if 'browserData' in dictionary:
            if not isinstance(dictionary['browserData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['browserData']))
            value = BrowserData()
            self.browser_data = value.from_dictionary(dictionary['browserData'])
        if 'defaultFormFill' in dictionary:
            self.default_form_fill = dictionary['defaultFormFill']
        if 'deviceFingerprintTransactionId' in dictionary:
            self.device_fingerprint_transaction_id = dictionary['deviceFingerprintTransactionId']
        if 'ipAddress' in dictionary:
            self.ip_address = dictionary['ipAddress']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'timezoneOffsetUtcMinutes' in dictionary:
            self.timezone_offset_utc_minutes = dictionary['timezoneOffsetUtcMinutes']
        if 'userAgent' in dictionary:
            self.user_agent = dictionary['userAgent']
        return self
