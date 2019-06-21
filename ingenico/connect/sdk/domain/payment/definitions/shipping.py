# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal


class Shipping(DataObject):
    """
    | Object containing information regarding shipping / delivery
    """

    __address = None
    __address_indicator = None
    __comments = None
    __email_address = None
    __first_usage_date = None
    __is_first_usage = None
    __tracking_number = None
    __type = None

    @property
    def address(self):
        """
        | Object containing address information
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.address_personal.AddressPersonal`
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def address_indicator(self):
        """
        | Indicates shipping method chosen for the transaction. Possible values:
        
        * same-as-billing = the shipping address is the same as the billing address
        * another-verified-address-on-file-with-merchant = the address used for shipping is another verified address of the customer that is on file with you
        * different-than-billing = shipping address is different from the billing address
        * ship-to-store = goods are shipped to a store (shipping address = store address)
        * digital-goods = electronic delivery of digital goods
        * travel-and-event-tickets-not-shipped = travel and/or event tickets that are not shipped
        * other = other means of delivery
        
        Type: str
        """
        return self.__address_indicator

    @address_indicator.setter
    def address_indicator(self, value):
        self.__address_indicator = value

    @property
    def comments(self):
        """
        | Comments included during shipping
        
        Type: str
        """
        return self.__comments

    @comments.setter
    def comments(self, value):
        self.__comments = value

    @property
    def email_address(self):
        """
        | Email address linked to the shipping
        
        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def first_usage_date(self):
        """
        | Date (YYYYMMDD) when the shipping details for this transaction were first used.
        
        Type: str
        """
        return self.__first_usage_date

    @first_usage_date.setter
    def first_usage_date(self, value):
        self.__first_usage_date = value

    @property
    def is_first_usage(self):
        """
        | Indicator if this shipping address is used for the first time to ship an order
        
        | true = the shipping details are used for the first time with this transaction
        
        | false = the shipping details have been used for other transactions in the past
        
        Type: bool
        """
        return self.__is_first_usage

    @is_first_usage.setter
    def is_first_usage(self, value):
        self.__is_first_usage = value

    @property
    def tracking_number(self):
        """
        | Shipment tracking number
        
        Type: str
        """
        return self.__tracking_number

    @tracking_number.setter
    def tracking_number(self, value):
        self.__tracking_number = value

    @property
    def type(self):
        """
        | Indicates the merchandise delivery timeframe. Possible values:
        
        * electronic = For electronic delivery (services or digital goods
        * same-day = For same day deliveries
        * overnight = For overnight deliveries
        * 2-day-or-more = For two day or more delivery time
        
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(Shipping, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.address_indicator is not None:
            dictionary['addressIndicator'] = self.address_indicator
        if self.comments is not None:
            dictionary['comments'] = self.comments
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address
        if self.first_usage_date is not None:
            dictionary['firstUsageDate'] = self.first_usage_date
        if self.is_first_usage is not None:
            dictionary['isFirstUsage'] = self.is_first_usage
        if self.tracking_number is not None:
            dictionary['trackingNumber'] = self.tracking_number
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary):
        super(Shipping, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = AddressPersonal()
            self.address = value.from_dictionary(dictionary['address'])
        if 'addressIndicator' in dictionary:
            self.address_indicator = dictionary['addressIndicator']
        if 'comments' in dictionary:
            self.comments = dictionary['comments']
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'firstUsageDate' in dictionary:
            self.first_usage_date = dictionary['firstUsageDate']
        if 'isFirstUsage' in dictionary:
            self.is_first_usage = dictionary['isFirstUsage']
        if 'trackingNumber' in dictionary:
            self.tracking_number = dictionary['trackingNumber']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
