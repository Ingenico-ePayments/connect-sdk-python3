# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class LodgingRoom(DataObject):
    """
    | Object that holds lodging related room data
    """

    __daily_room_rate = None
    __daily_room_rate_currency_code = None
    __daily_room_tax_amount = None
    __daily_room_tax_amount_currency_code = None
    __number_of_nights_at_room_rate = None
    __room_location = None
    __room_number = None
    __type_of_bed = None
    __type_of_room = None

    @property
    def daily_room_rate(self):
        """
        | Daily room rate exclusive of any taxes and fees
        | Note: The currencyCode is presumed to be identical to the order.amountOfMoney.currencyCode.
        
        Type: str
        """
        return self.__daily_room_rate

    @daily_room_rate.setter
    def daily_room_rate(self, value):
        self.__daily_room_rate = value

    @property
    def daily_room_rate_currency_code(self):
        """
        | Currency for Daily room rate. The code should be in 3 letter ISO format
        
        Type: str
        """
        return self.__daily_room_rate_currency_code

    @daily_room_rate_currency_code.setter
    def daily_room_rate_currency_code(self, value):
        self.__daily_room_rate_currency_code = value

    @property
    def daily_room_tax_amount(self):
        """
        | Daily room tax
        | Note: The currencyCode is presumed to be identical to the order.amountOfMoney.currencyCode.
        
        Type: str
        """
        return self.__daily_room_tax_amount

    @daily_room_tax_amount.setter
    def daily_room_tax_amount(self, value):
        self.__daily_room_tax_amount = value

    @property
    def daily_room_tax_amount_currency_code(self):
        """
        | Currency for Daily room tax. The code should be in 3 letter ISO format
        
        Type: str
        """
        return self.__daily_room_tax_amount_currency_code

    @daily_room_tax_amount_currency_code.setter
    def daily_room_tax_amount_currency_code(self, value):
        self.__daily_room_tax_amount_currency_code = value

    @property
    def number_of_nights_at_room_rate(self):
        """
        | Number of nights charged at the rate in the dailyRoomRate property
        
        Type: int
        """
        return self.__number_of_nights_at_room_rate

    @number_of_nights_at_room_rate.setter
    def number_of_nights_at_room_rate(self, value):
        self.__number_of_nights_at_room_rate = value

    @property
    def room_location(self):
        """
        | Location of the room within the facility, e.g. Park or Garden etc.
        
        Type: str
        """
        return self.__room_location

    @room_location.setter
    def room_location(self, value):
        self.__room_location = value

    @property
    def room_number(self):
        """
        | Room number
        
        Type: str
        """
        return self.__room_number

    @room_number.setter
    def room_number(self, value):
        self.__room_number = value

    @property
    def type_of_bed(self):
        """
        | Size of bed, e.g., king, queen, double.
        
        Type: str
        """
        return self.__type_of_bed

    @type_of_bed.setter
    def type_of_bed(self, value):
        self.__type_of_bed = value

    @property
    def type_of_room(self):
        """
        | Describes the type of room, e.g., standard, deluxe, suite.
        
        Type: str
        """
        return self.__type_of_room

    @type_of_room.setter
    def type_of_room(self, value):
        self.__type_of_room = value

    def to_dictionary(self):
        dictionary = super(LodgingRoom, self).to_dictionary()
        if self.daily_room_rate is not None:
            dictionary['dailyRoomRate'] = self.daily_room_rate
        if self.daily_room_rate_currency_code is not None:
            dictionary['dailyRoomRateCurrencyCode'] = self.daily_room_rate_currency_code
        if self.daily_room_tax_amount is not None:
            dictionary['dailyRoomTaxAmount'] = self.daily_room_tax_amount
        if self.daily_room_tax_amount_currency_code is not None:
            dictionary['dailyRoomTaxAmountCurrencyCode'] = self.daily_room_tax_amount_currency_code
        if self.number_of_nights_at_room_rate is not None:
            dictionary['numberOfNightsAtRoomRate'] = self.number_of_nights_at_room_rate
        if self.room_location is not None:
            dictionary['roomLocation'] = self.room_location
        if self.room_number is not None:
            dictionary['roomNumber'] = self.room_number
        if self.type_of_bed is not None:
            dictionary['typeOfBed'] = self.type_of_bed
        if self.type_of_room is not None:
            dictionary['typeOfRoom'] = self.type_of_room
        return dictionary

    def from_dictionary(self, dictionary):
        super(LodgingRoom, self).from_dictionary(dictionary)
        if 'dailyRoomRate' in dictionary:
            self.daily_room_rate = dictionary['dailyRoomRate']
        if 'dailyRoomRateCurrencyCode' in dictionary:
            self.daily_room_rate_currency_code = dictionary['dailyRoomRateCurrencyCode']
        if 'dailyRoomTaxAmount' in dictionary:
            self.daily_room_tax_amount = dictionary['dailyRoomTaxAmount']
        if 'dailyRoomTaxAmountCurrencyCode' in dictionary:
            self.daily_room_tax_amount_currency_code = dictionary['dailyRoomTaxAmountCurrencyCode']
        if 'numberOfNightsAtRoomRate' in dictionary:
            self.number_of_nights_at_room_rate = dictionary['numberOfNightsAtRoomRate']
        if 'roomLocation' in dictionary:
            self.room_location = dictionary['roomLocation']
        if 'roomNumber' in dictionary:
            self.room_number = dictionary['roomNumber']
        if 'typeOfBed' in dictionary:
            self.type_of_bed = dictionary['typeOfBed']
        if 'typeOfRoom' in dictionary:
            self.type_of_room = dictionary['typeOfRoom']
        return self
