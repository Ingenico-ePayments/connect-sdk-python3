#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class AirlineFlightLeg(DataObject):
    """
    Class AirlineFlightLeg
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AirlineFlightLeg
    
    Attributes:
        airline_class:    str
        arrival_airport:  str
        carrier_code:     str
        date:             str
        departure_time:   str
        fare:             str
        fare_basis:       str
        flight_number:    str
        number:           int
        origin_airport:   str
        stopover_code:    str
     """

    airline_class = None
    arrival_airport = None
    carrier_code = None
    date = None
    departure_time = None
    fare = None
    fare_basis = None
    flight_number = None
    number = None
    origin_airport = None
    stopover_code = None

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
