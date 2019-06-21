# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class AirlineFlightLeg(DataObject):

    __airline_class = None
    __arrival_airport = None
    __arrival_time = None
    __carrier_code = None
    __conjunction_ticket = None
    __coupon_number = None
    __date = None
    __departure_time = None
    __endorsement_or_restriction = None
    __exchange_ticket = None
    __fare = None
    __fare_basis = None
    __fee = None
    __flight_number = None
    __number = None
    __origin_airport = None
    __passenger_class = None
    __service_class = None
    __stopover_code = None
    __taxes = None

    @property
    def airline_class(self):
        """
        | Reservation Booking Designator
        
        Type: str
        """
        return self.__airline_class

    @airline_class.setter
    def airline_class(self, value):
        self.__airline_class = value

    @property
    def arrival_airport(self):
        """
        | Arrival airport/city code
        
        Type: str
        """
        return self.__arrival_airport

    @arrival_airport.setter
    def arrival_airport(self, value):
        self.__arrival_airport = value

    @property
    def arrival_time(self):
        """
        | The arrival time in the local time zone 
        | Format: HH:MM
        
        Type: str
        """
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        self.__arrival_time = value

    @property
    def carrier_code(self):
        """
        | IATA carrier code
        
        Type: str
        """
        return self.__carrier_code

    @carrier_code.setter
    def carrier_code(self, value):
        self.__carrier_code = value

    @property
    def conjunction_ticket(self):
        """
        | Identifying number of a ticket issued to a passenger in conjunction with this ticket and that constitutes a single contract of carriage
        
        Type: str
        """
        return self.__conjunction_ticket

    @conjunction_ticket.setter
    def conjunction_ticket(self, value):
        self.__conjunction_ticket = value

    @property
    def coupon_number(self):
        """
        | The coupon number associated with this leg of the trip. A ticket can contain several legs of travel, and each leg of travel requires a separate coupon
        
        Type: str
        """
        return self.__coupon_number

    @coupon_number.setter
    def coupon_number(self, value):
        self.__coupon_number = value

    @property
    def date(self):
        """
        | Date of the leg
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def departure_time(self):
        """
        | The departure time in the local time at the departure airport
        | Format: HH:MM
        
        Type: str
        """
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value

    @property
    def endorsement_or_restriction(self):
        """
        | An endorsement can be an agency-added notation or a mandatory government required notation, such as value-added tax. A restriction is a limitation based on the type of fare, such as a ticket with a 3-day minimum stay
        
        Type: str
        """
        return self.__endorsement_or_restriction

    @endorsement_or_restriction.setter
    def endorsement_or_restriction(self, value):
        self.__endorsement_or_restriction = value

    @property
    def exchange_ticket(self):
        """
        | New ticket number that is issued when a ticket is exchanged
        
        Type: str
        """
        return self.__exchange_ticket

    @exchange_ticket.setter
    def exchange_ticket(self, value):
        self.__exchange_ticket = value

    @property
    def fare(self):
        """
        | Fare of this leg
        
        Type: str
        """
        return self.__fare

    @fare.setter
    def fare(self, value):
        self.__fare = value

    @property
    def fare_basis(self):
        """
        | Fare Basis/Ticket Designator
        
        Type: str
        """
        return self.__fare_basis

    @fare_basis.setter
    def fare_basis(self, value):
        self.__fare_basis = value

    @property
    def fee(self):
        """
        | Fee for this leg of the trip
        
        Type: int
        """
        return self.__fee

    @fee.setter
    def fee(self, value):
        self.__fee = value

    @property
    def flight_number(self):
        """
        | The flight number assigned by the airline carrier with no leading spaces
        | Should be a numeric string
        
        Type: str
        """
        return self.__flight_number

    @flight_number.setter
    def flight_number(self, value):
        self.__flight_number = value

    @property
    def number(self):
        """
        | Sequence number of the flight leg
        
        Type: int
        """
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def origin_airport(self):
        """
        | Origin airport/city code
        
        Type: str
        """
        return self.__origin_airport

    @origin_airport.setter
    def origin_airport(self, value):
        self.__origin_airport = value

    @property
    def passenger_class(self):
        """
        | PassengerClass if this leg
        
        Type: str
        """
        return self.__passenger_class

    @passenger_class.setter
    def passenger_class(self, value):
        self.__passenger_class = value

    @property
    def service_class(self):
        """
        | ServiceClass of this leg (this property is used for fraud screening on the Ogone Payment Platform).
        
        | Possible values are:
        
        * economy
        * premium-economy
        * business
        * first
        
        Type: str
        
        Deprecated; Use passengerClass instead
        """
        return self.__service_class

    @service_class.setter
    def service_class(self, value):
        self.__service_class = value

    @property
    def stopover_code(self):
        """
        | Possible values are:
        
        * permitted = Stopover permitted
        * non-permitted = Stopover not permitted
        
        Type: str
        """
        return self.__stopover_code

    @stopover_code.setter
    def stopover_code(self, value):
        self.__stopover_code = value

    @property
    def taxes(self):
        """
        | Taxes for this leg of the trip
        
        Type: int
        """
        return self.__taxes

    @taxes.setter
    def taxes(self, value):
        self.__taxes = value

    def to_dictionary(self):
        dictionary = super(AirlineFlightLeg, self).to_dictionary()
        if self.airline_class is not None:
            dictionary['airlineClass'] = self.airline_class
        if self.arrival_airport is not None:
            dictionary['arrivalAirport'] = self.arrival_airport
        if self.arrival_time is not None:
            dictionary['arrivalTime'] = self.arrival_time
        if self.carrier_code is not None:
            dictionary['carrierCode'] = self.carrier_code
        if self.conjunction_ticket is not None:
            dictionary['conjunctionTicket'] = self.conjunction_ticket
        if self.coupon_number is not None:
            dictionary['couponNumber'] = self.coupon_number
        if self.date is not None:
            dictionary['date'] = self.date
        if self.departure_time is not None:
            dictionary['departureTime'] = self.departure_time
        if self.endorsement_or_restriction is not None:
            dictionary['endorsementOrRestriction'] = self.endorsement_or_restriction
        if self.exchange_ticket is not None:
            dictionary['exchangeTicket'] = self.exchange_ticket
        if self.fare is not None:
            dictionary['fare'] = self.fare
        if self.fare_basis is not None:
            dictionary['fareBasis'] = self.fare_basis
        if self.fee is not None:
            dictionary['fee'] = self.fee
        if self.flight_number is not None:
            dictionary['flightNumber'] = self.flight_number
        if self.number is not None:
            dictionary['number'] = self.number
        if self.origin_airport is not None:
            dictionary['originAirport'] = self.origin_airport
        if self.passenger_class is not None:
            dictionary['passengerClass'] = self.passenger_class
        if self.service_class is not None:
            dictionary['serviceClass'] = self.service_class
        if self.stopover_code is not None:
            dictionary['stopoverCode'] = self.stopover_code
        if self.taxes is not None:
            dictionary['taxes'] = self.taxes
        return dictionary

    def from_dictionary(self, dictionary):
        super(AirlineFlightLeg, self).from_dictionary(dictionary)
        if 'airlineClass' in dictionary:
            self.airline_class = dictionary['airlineClass']
        if 'arrivalAirport' in dictionary:
            self.arrival_airport = dictionary['arrivalAirport']
        if 'arrivalTime' in dictionary:
            self.arrival_time = dictionary['arrivalTime']
        if 'carrierCode' in dictionary:
            self.carrier_code = dictionary['carrierCode']
        if 'conjunctionTicket' in dictionary:
            self.conjunction_ticket = dictionary['conjunctionTicket']
        if 'couponNumber' in dictionary:
            self.coupon_number = dictionary['couponNumber']
        if 'date' in dictionary:
            self.date = dictionary['date']
        if 'departureTime' in dictionary:
            self.departure_time = dictionary['departureTime']
        if 'endorsementOrRestriction' in dictionary:
            self.endorsement_or_restriction = dictionary['endorsementOrRestriction']
        if 'exchangeTicket' in dictionary:
            self.exchange_ticket = dictionary['exchangeTicket']
        if 'fare' in dictionary:
            self.fare = dictionary['fare']
        if 'fareBasis' in dictionary:
            self.fare_basis = dictionary['fareBasis']
        if 'fee' in dictionary:
            self.fee = dictionary['fee']
        if 'flightNumber' in dictionary:
            self.flight_number = dictionary['flightNumber']
        if 'number' in dictionary:
            self.number = dictionary['number']
        if 'originAirport' in dictionary:
            self.origin_airport = dictionary['originAirport']
        if 'passengerClass' in dictionary:
            self.passenger_class = dictionary['passengerClass']
        if 'serviceClass' in dictionary:
            self.service_class = dictionary['serviceClass']
        if 'stopoverCode' in dictionary:
            self.stopover_code = dictionary['stopoverCode']
        if 'taxes' in dictionary:
            self.taxes = dictionary['taxes']
        return self
