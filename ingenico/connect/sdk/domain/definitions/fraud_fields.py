# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.fraud_fields_shipping_details import FraudFieldsShippingDetails


class FraudFields(DataObject):

    __addresses_are_identical = None
    __black_list_data = None
    __card_owner_address = None
    __customer_ip_address = None
    __default_form_fill = None
    __device_fingerprint_activated = None
    __device_fingerprint_transaction_id = None
    __gift_card_type = None
    __gift_message = None
    __has_forgotten_pwd = None
    __has_password = None
    __is_previous_customer = None
    __order_timezone = None
    __ship_comments = None
    __shipment_tracking_number = None
    __shipping_details = None
    __user_data = None
    __website = None

    @property
    def addresses_are_identical(self):
        """
        | Indicates that invoice and shipping addresses are equal.
        
        Type: bool
        
        Deprecated; For risk assessments there is no replacement. For other calls, use Order.shipping.addressIndicator instead
        """
        return self.__addresses_are_identical

    @addresses_are_identical.setter
    def addresses_are_identical(self, value):
        self.__addresses_are_identical = value

    @property
    def black_list_data(self):
        """
        | Additional black list input
        
        Type: str
        """
        return self.__black_list_data

    @black_list_data.setter
    def black_list_data(self, value):
        self.__black_list_data = value

    @property
    def card_owner_address(self):
        """
        | The address that belongs to the owner of the card
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        
        Deprecated; This should be the same as Order.customer.billingAddress
        """
        return self.__card_owner_address

    @card_owner_address.setter
    def card_owner_address(self, value):
        self.__card_owner_address = value

    @property
    def customer_ip_address(self):
        """
        | The IP Address of the customer that is making the payment
        
        Type: str
        """
        return self.__customer_ip_address

    @customer_ip_address.setter
    def customer_ip_address(self, value):
        self.__customer_ip_address = value

    @property
    def default_form_fill(self):
        """
        | Degree of default form fill, with the following possible values:
        
        * automatically - All fields filled automatically
        * automatically-but-modified - All fields filled automatically, but some fields were modified manually
        * manually - All fields were entered manually
        
        Type: str
        
        Deprecated; Use Order.customer.device.defaultFormFill instead
        """
        return self.__default_form_fill

    @default_form_fill.setter
    def default_form_fill(self, value):
        self.__default_form_fill = value

    @property
    def device_fingerprint_activated(self):
        """
        | Indicates that the device fingerprint has been used while processing the order.
        
        Type: bool
        
        Deprecated; No replacement
        """
        return self.__device_fingerprint_activated

    @device_fingerprint_activated.setter
    def device_fingerprint_activated(self, value):
        self.__device_fingerprint_activated = value

    @property
    def device_fingerprint_transaction_id(self):
        """
        | One must set the deviceFingerprintTransactionId received by the response of the endpoint /{merchant}/products/{paymentProductId}/deviceFingerprint
        
        Type: str
        
        Deprecated; Use Order.customer.device.deviceFingerprintTransactionId instead
        """
        return self.__device_fingerprint_transaction_id

    @device_fingerprint_transaction_id.setter
    def device_fingerprint_transaction_id(self, value):
        self.__device_fingerprint_transaction_id = value

    @property
    def gift_card_type(self):
        """
        | One of the following gift card types:
        
        * celebrate-fall - Celebrate Fall
        * grandparents-day - Grandparent's Day
        * independence-day - Independence Day
        * anniversary - Anniversary
        * birthday - Birthday
        * congratulations - Congratulations
        * april-fools-day - April Fool's Day
        * easter - Easter
        * fathers-day - Father's Day
        * graduation - Graduation
        * holiday - Holiday
        * seasons-greetings - Season's Greetings
        * passover - Passover
        * kwanzaa - Kwanzaa
        * halloween - Halloween
        * mothers-day - Mother's Day
        * new-years-day - New Year's Day
        * bosses-day - Bosses' Day
        * st-patricks-day - St. Patrick's Day
        * sweetest-day - Sweetest Day
        * christmas - Christmas
        * baby-shower - Baby Shower
        * thanksgiving - Thanksgiving
        * other - Other
        * valentines-day - Valentine's Day
        * wedding - Wedding
        * secretarys-day - Secretary's Day
        * chinese-new-year - Chinese New Year
        * hanukkah - Hanukkah
        
        Type: str
        """
        return self.__gift_card_type

    @gift_card_type.setter
    def gift_card_type(self, value):
        self.__gift_card_type = value

    @property
    def gift_message(self):
        """
        | Gift message
        
        Type: str
        """
        return self.__gift_message

    @gift_message.setter
    def gift_message(self, value):
        self.__gift_message = value

    @property
    def has_forgotten_pwd(self):
        """
        | Specifies if the customer (initially) had forgotten their password
        
        * true - The customer has forgotten their password
        * false - The customer has not forgotten their password
        
        Type: bool
        
        Deprecated; Use Order.customer.account.hasForgottenPassword instead
        """
        return self.__has_forgotten_pwd

    @has_forgotten_pwd.setter
    def has_forgotten_pwd(self, value):
        self.__has_forgotten_pwd = value

    @property
    def has_password(self):
        """
        | Specifies if the customer entered a password to gain access to an account registered with the you
        
        * true - The customer has used a password to gain access
        * false - The customer has not used a password to gain access
        
        Type: bool
        
        Deprecated; Use Order.customer.account.hasPassword instead
        """
        return self.__has_password

    @has_password.setter
    def has_password(self, value):
        self.__has_password = value

    @property
    def is_previous_customer(self):
        """
        | Specifies if the customer has a history of online shopping with the merchant
        
        * true - The customer is a known returning customer
        * false - The customer is new/unknown customer
        
        Type: bool
        
        Deprecated; Use Order.customer.isPreviousCustomer instead
        """
        return self.__is_previous_customer

    @is_previous_customer.setter
    def is_previous_customer(self, value):
        self.__is_previous_customer = value

    @property
    def order_timezone(self):
        """
        | Timezone in which the order was placed
        
        Type: str
        """
        return self.__order_timezone

    @order_timezone.setter
    def order_timezone(self, value):
        self.__order_timezone = value

    @property
    def ship_comments(self):
        """
        | Comments included during shipping
        
        Type: str
        
        Deprecated; Use Order.shipping.comments instead
        """
        return self.__ship_comments

    @ship_comments.setter
    def ship_comments(self, value):
        self.__ship_comments = value

    @property
    def shipment_tracking_number(self):
        """
        | Shipment tracking number
        
        Type: str
        
        Deprecated; Use Order.shipping.trackingNumber instead
        """
        return self.__shipment_tracking_number

    @shipment_tracking_number.setter
    def shipment_tracking_number(self, value):
        self.__shipment_tracking_number = value

    @property
    def shipping_details(self):
        """
        | Details on how the order is shipped to the customer
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.fraud_fields_shipping_details.FraudFieldsShippingDetails`
        
        Deprecated; No replacement
        """
        return self.__shipping_details

    @shipping_details.setter
    def shipping_details(self, value):
        self.__shipping_details = value

    @property
    def user_data(self):
        """
        | Array of up to 16 userData properties, each with a max length of 256 characters, that can be used for fraudscreening
        
        Type: list[str]
        """
        return self.__user_data

    @user_data.setter
    def user_data(self, value):
        self.__user_data = value

    @property
    def website(self):
        """
        | The website from which the purchase was made
        
        Type: str
        
        Deprecated; Use Merchant.websiteUrl instead
        """
        return self.__website

    @website.setter
    def website(self, value):
        self.__website = value

    def to_dictionary(self):
        dictionary = super(FraudFields, self).to_dictionary()
        if self.addresses_are_identical is not None:
            dictionary['addressesAreIdentical'] = self.addresses_are_identical
        if self.black_list_data is not None:
            dictionary['blackListData'] = self.black_list_data
        if self.card_owner_address is not None:
            dictionary['cardOwnerAddress'] = self.card_owner_address.to_dictionary()
        if self.customer_ip_address is not None:
            dictionary['customerIpAddress'] = self.customer_ip_address
        if self.default_form_fill is not None:
            dictionary['defaultFormFill'] = self.default_form_fill
        if self.device_fingerprint_activated is not None:
            dictionary['deviceFingerprintActivated'] = self.device_fingerprint_activated
        if self.device_fingerprint_transaction_id is not None:
            dictionary['deviceFingerprintTransactionId'] = self.device_fingerprint_transaction_id
        if self.gift_card_type is not None:
            dictionary['giftCardType'] = self.gift_card_type
        if self.gift_message is not None:
            dictionary['giftMessage'] = self.gift_message
        if self.has_forgotten_pwd is not None:
            dictionary['hasForgottenPwd'] = self.has_forgotten_pwd
        if self.has_password is not None:
            dictionary['hasPassword'] = self.has_password
        if self.is_previous_customer is not None:
            dictionary['isPreviousCustomer'] = self.is_previous_customer
        if self.order_timezone is not None:
            dictionary['orderTimezone'] = self.order_timezone
        if self.ship_comments is not None:
            dictionary['shipComments'] = self.ship_comments
        if self.shipment_tracking_number is not None:
            dictionary['shipmentTrackingNumber'] = self.shipment_tracking_number
        if self.shipping_details is not None:
            dictionary['shippingDetails'] = self.shipping_details.to_dictionary()
        if self.user_data is not None:
            dictionary['userData'] = []
            for element in self.user_data:
                if element is not None:
                    dictionary['userData'].append(element)
        if self.website is not None:
            dictionary['website'] = self.website
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudFields, self).from_dictionary(dictionary)
        if 'addressesAreIdentical' in dictionary:
            self.addresses_are_identical = dictionary['addressesAreIdentical']
        if 'blackListData' in dictionary:
            self.black_list_data = dictionary['blackListData']
        if 'cardOwnerAddress' in dictionary:
            if not isinstance(dictionary['cardOwnerAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardOwnerAddress']))
            value = Address()
            self.card_owner_address = value.from_dictionary(dictionary['cardOwnerAddress'])
        if 'customerIpAddress' in dictionary:
            self.customer_ip_address = dictionary['customerIpAddress']
        if 'defaultFormFill' in dictionary:
            self.default_form_fill = dictionary['defaultFormFill']
        if 'deviceFingerprintActivated' in dictionary:
            self.device_fingerprint_activated = dictionary['deviceFingerprintActivated']
        if 'deviceFingerprintTransactionId' in dictionary:
            self.device_fingerprint_transaction_id = dictionary['deviceFingerprintTransactionId']
        if 'giftCardType' in dictionary:
            self.gift_card_type = dictionary['giftCardType']
        if 'giftMessage' in dictionary:
            self.gift_message = dictionary['giftMessage']
        if 'hasForgottenPwd' in dictionary:
            self.has_forgotten_pwd = dictionary['hasForgottenPwd']
        if 'hasPassword' in dictionary:
            self.has_password = dictionary['hasPassword']
        if 'isPreviousCustomer' in dictionary:
            self.is_previous_customer = dictionary['isPreviousCustomer']
        if 'orderTimezone' in dictionary:
            self.order_timezone = dictionary['orderTimezone']
        if 'shipComments' in dictionary:
            self.ship_comments = dictionary['shipComments']
        if 'shipmentTrackingNumber' in dictionary:
            self.shipment_tracking_number = dictionary['shipmentTrackingNumber']
        if 'shippingDetails' in dictionary:
            if not isinstance(dictionary['shippingDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shippingDetails']))
            value = FraudFieldsShippingDetails()
            self.shipping_details = value.from_dictionary(dictionary['shippingDetails'])
        if 'userData' in dictionary:
            if not isinstance(dictionary['userData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['userData']))
            self.user_data = []
            for element in dictionary['userData']:
                self.user_data.append(element)
        if 'website' in dictionary:
            self.website = dictionary['website']
        return self
