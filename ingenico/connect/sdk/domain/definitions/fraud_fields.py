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
    __finger_print_activated = None
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
        """
        return self.__card_owner_address

    @card_owner_address.setter
    def card_owner_address(self, value):
        self.__card_owner_address = value

    @property
    def customer_ip_address(self):
        """
        | The IP Address of the consumer that is making the payment
        
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
        """
        return self.__default_form_fill

    @default_form_fill.setter
    def default_form_fill(self, value):
        self.__default_form_fill = value

    @property
    def finger_print_activated(self):
        """
        | Indicates that the device fingerprint has been used while processing the order
        
        Type: bool
        """
        return self.__finger_print_activated

    @finger_print_activated.setter
    def finger_print_activated(self, value):
        self.__finger_print_activated = value

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
        | Specifies if the consumer (initially) had forgotten their password
        
        * true - The consumer has forgotten their password
        * false - The consumer has not forgotten their password
        
        Type: bool
        """
        return self.__has_forgotten_pwd

    @has_forgotten_pwd.setter
    def has_forgotten_pwd(self, value):
        self.__has_forgotten_pwd = value

    @property
    def has_password(self):
        """
        | Specifies if the consumer entered a password to gain access to an account registered with the you
        
        * true - The consumer has used a password to gain access
        * false - The consumer has not used a password to gain access
        
        Type: bool
        """
        return self.__has_password

    @has_password.setter
    def has_password(self, value):
        self.__has_password = value

    @property
    def is_previous_customer(self):
        """
        | Specifies if the consumer has a history of online shopping with the merchant
        
        * true - The consumer is a known returning consumer
        * false - The consumer is new/unknown consumer
        
        Type: bool
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
        """
        return self.__shipping_details

    @shipping_details.setter
    def shipping_details(self, value):
        self.__shipping_details = value

    @property
    def user_data(self):
        """
        | Array of up to 16 userData fields, each with a max length of 256 characters, that can be used for fraudscreening
        
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
        """
        return self.__website

    @website.setter
    def website(self, value):
        self.__website = value

    def to_dictionary(self):
        dictionary = super(FraudFields, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'addressesAreIdentical', self.addresses_are_identical)
        self._add_to_dictionary(dictionary, 'blackListData', self.black_list_data)
        self._add_to_dictionary(dictionary, 'cardOwnerAddress', self.card_owner_address)
        self._add_to_dictionary(dictionary, 'customerIpAddress', self.customer_ip_address)
        self._add_to_dictionary(dictionary, 'defaultFormFill', self.default_form_fill)
        self._add_to_dictionary(dictionary, 'fingerPrintActivated', self.finger_print_activated)
        self._add_to_dictionary(dictionary, 'giftCardType', self.gift_card_type)
        self._add_to_dictionary(dictionary, 'giftMessage', self.gift_message)
        self._add_to_dictionary(dictionary, 'hasForgottenPwd', self.has_forgotten_pwd)
        self._add_to_dictionary(dictionary, 'hasPassword', self.has_password)
        self._add_to_dictionary(dictionary, 'isPreviousCustomer', self.is_previous_customer)
        self._add_to_dictionary(dictionary, 'orderTimezone', self.order_timezone)
        self._add_to_dictionary(dictionary, 'shipComments', self.ship_comments)
        self._add_to_dictionary(dictionary, 'shipmentTrackingNumber', self.shipment_tracking_number)
        self._add_to_dictionary(dictionary, 'shippingDetails', self.shipping_details)
        self._add_to_dictionary(dictionary, 'userData', self.user_data)
        self._add_to_dictionary(dictionary, 'website', self.website)
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
        if 'fingerPrintActivated' in dictionary:
            self.finger_print_activated = dictionary['fingerPrintActivated']
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
            for userData_element in dictionary['userData']:
                self.user_data.append(userData_element)
        if 'website' in dictionary:
            self.website = dictionary['website']
        return self
