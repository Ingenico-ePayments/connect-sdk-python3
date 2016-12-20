#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class FraudFields(DataObject):
    """
    Class FraudFields
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_FraudFields
    """

    __customer_ip_address = None
    __default_form_fill = None
    __gift_card_type = None
    __gift_message = None
    __has_forgotten_pwd = None
    __has_password = None
    __is_previous_customer = None
    __order_timezone = None
    __ship_comments = None
    __shipment_tracking_number = None
    __user_data = None
    __website = None

    @property
    def customer_ip_address(self):
        """
        str
        """
        return self.__customer_ip_address

    @customer_ip_address.setter
    def customer_ip_address(self, value):
        self.__customer_ip_address = value

    @property
    def default_form_fill(self):
        """
        str
        """
        return self.__default_form_fill

    @default_form_fill.setter
    def default_form_fill(self, value):
        self.__default_form_fill = value

    @property
    def gift_card_type(self):
        """
        str
        """
        return self.__gift_card_type

    @gift_card_type.setter
    def gift_card_type(self, value):
        self.__gift_card_type = value

    @property
    def gift_message(self):
        """
        str
        """
        return self.__gift_message

    @gift_message.setter
    def gift_message(self, value):
        self.__gift_message = value

    @property
    def has_forgotten_pwd(self):
        """
        bool
        """
        return self.__has_forgotten_pwd

    @has_forgotten_pwd.setter
    def has_forgotten_pwd(self, value):
        self.__has_forgotten_pwd = value

    @property
    def has_password(self):
        """
        bool
        """
        return self.__has_password

    @has_password.setter
    def has_password(self, value):
        self.__has_password = value

    @property
    def is_previous_customer(self):
        """
        bool
        """
        return self.__is_previous_customer

    @is_previous_customer.setter
    def is_previous_customer(self, value):
        self.__is_previous_customer = value

    @property
    def order_timezone(self):
        """
        str
        """
        return self.__order_timezone

    @order_timezone.setter
    def order_timezone(self, value):
        self.__order_timezone = value

    @property
    def ship_comments(self):
        """
        str
        """
        return self.__ship_comments

    @ship_comments.setter
    def ship_comments(self, value):
        self.__ship_comments = value

    @property
    def shipment_tracking_number(self):
        """
        str
        """
        return self.__shipment_tracking_number

    @shipment_tracking_number.setter
    def shipment_tracking_number(self, value):
        self.__shipment_tracking_number = value

    @property
    def user_data(self):
        """
        list[str]
        """
        return self.__user_data

    @user_data.setter
    def user_data(self, value):
        self.__user_data = value

    @property
    def website(self):
        """
        str
        """
        return self.__website

    @website.setter
    def website(self, value):
        self.__website = value

    def to_dictionary(self):
        dictionary = super(FraudFields, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customerIpAddress', self.customer_ip_address)
        self._add_to_dictionary(dictionary, 'defaultFormFill', self.default_form_fill)
        self._add_to_dictionary(dictionary, 'giftCardType', self.gift_card_type)
        self._add_to_dictionary(dictionary, 'giftMessage', self.gift_message)
        self._add_to_dictionary(dictionary, 'hasForgottenPwd', self.has_forgotten_pwd)
        self._add_to_dictionary(dictionary, 'hasPassword', self.has_password)
        self._add_to_dictionary(dictionary, 'isPreviousCustomer', self.is_previous_customer)
        self._add_to_dictionary(dictionary, 'orderTimezone', self.order_timezone)
        self._add_to_dictionary(dictionary, 'shipComments', self.ship_comments)
        self._add_to_dictionary(dictionary, 'shipmentTrackingNumber', self.shipment_tracking_number)
        self._add_to_dictionary(dictionary, 'userData', self.user_data)
        self._add_to_dictionary(dictionary, 'website', self.website)
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudFields, self).from_dictionary(dictionary)
        if 'customerIpAddress' in dictionary:
            self.customer_ip_address = dictionary['customerIpAddress']
        if 'defaultFormFill' in dictionary:
            self.default_form_fill = dictionary['defaultFormFill']
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
        if 'userData' in dictionary:
            if not isinstance(dictionary['userData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['userData']))
            self.user_data = []
            for userData_element in dictionary['userData']:
                self.user_data.append(userData_element)
        if 'website' in dictionary:
            self.website = dictionary['website']
        return self
