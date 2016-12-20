#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class AirlineFlightLeg(DataObject):
    """
    Class AirlineFlightLeg
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AirlineFlightLeg
    """

    __airline_class = None
    __arrival_airport = None
    __carrier_code = None
    __date = None
    __departure_time = None
    __fare = None
    __fare_basis = None
    __flight_number = None
    __number = None
    __origin_airport = None
    __stopover_code = None

    @property
    def airline_class(self):
        """
        str
        """
        return self.__airline_class

    @airline_class.setter
    def airline_class(self, value):
        self.__airline_class = value

    @property
    def arrival_airport(self):
        """
        str
        """
        return self.__arrival_airport

    @arrival_airport.setter
    def arrival_airport(self, value):
        self.__arrival_airport = value

    @property
    def carrier_code(self):
        """
        str
        """
        return self.__carrier_code

    @carrier_code.setter
    def carrier_code(self, value):
        self.__carrier_code = value

    @property
    def date(self):
        """
        str
        """
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def departure_time(self):
        """
        str
        """
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value

    @property
    def fare(self):
        """
        str
        """
        return self.__fare

    @fare.setter
    def fare(self, value):
        self.__fare = value

    @property
    def fare_basis(self):
        """
        str
        """
        return self.__fare_basis

    @fare_basis.setter
    def fare_basis(self, value):
        self.__fare_basis = value

    @property
    def flight_number(self):
        """
        str
        """
        return self.__flight_number

    @flight_number.setter
    def flight_number(self, value):
        self.__flight_number = value

    @property
    def number(self):
        """
        int
        """
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def origin_airport(self):
        """
        str
        """
        return self.__origin_airport

    @origin_airport.setter
    def origin_airport(self, value):
        self.__origin_airport = value

    @property
    def stopover_code(self):
        """
        str
        """
        return self.__stopover_code

    @stopover_code.setter
    def stopover_code(self, value):
        self.__stopover_code = value

    def to_dictionary(self):
        dictionary = super(AirlineFlightLeg, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'airlineClass', self.airline_class)
        self._add_to_dictionary(dictionary, 'arrivalAirport', self.arrival_airport)
        self._add_to_dictionary(dictionary, 'carrierCode', self.carrier_code)
        self._add_to_dictionary(dictionary, 'date', self.date)
        self._add_to_dictionary(dictionary, 'departureTime', self.departure_time)
        self._add_to_dictionary(dictionary, 'fare', self.fare)
        self._add_to_dictionary(dictionary, 'fareBasis', self.fare_basis)
        self._add_to_dictionary(dictionary, 'flightNumber', self.flight_number)
        self._add_to_dictionary(dictionary, 'number', self.number)
        self._add_to_dictionary(dictionary, 'originAirport', self.origin_airport)
        self._add_to_dictionary(dictionary, 'stopoverCode', self.stopover_code)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AirlineFlightLeg, self).from_dictionary(dictionary)
        if 'airlineClass' in dictionary:
            self.airline_class = dictionary['airlineClass']
        if 'arrivalAirport' in dictionary:
            self.arrival_airport = dictionary['arrivalAirport']
        if 'carrierCode' in dictionary:
            self.carrier_code = dictionary['carrierCode']
        if 'date' in dictionary:
            self.date = dictionary['date']
        if 'departureTime' in dictionary:
            self.departure_time = dictionary['departureTime']
        if 'fare' in dictionary:
            self.fare = dictionary['fare']
        if 'fareBasis' in dictionary:
            self.fare_basis = dictionary['fareBasis']
        if 'flightNumber' in dictionary:
            self.flight_number = dictionary['flightNumber']
        if 'number' in dictionary:
            self.number = dictionary['number']
        if 'originAirport' in dictionary:
            self.origin_airport = dictionary['originAirport']
        if 'stopoverCode' in dictionary:
            self.stopover_code = dictionary['stopoverCode']
        return self
