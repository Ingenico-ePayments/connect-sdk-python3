#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.airline_flight_leg import AirlineFlightLeg


class AirlineData(DataObject):
    """
    Class AirlineData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AirlineData
    
    Attributes:
        agent_numeric_code:      str
        code:                    str
        flight_date:             str
        flight_legs:             list[:class:`AirlineFlightLeg`]
        invoice_number:          str
        is_e_ticket:             bool
        is_registered_customer:  bool
        is_restricted_ticket:    bool
        is_third_party:          bool
        issue_date:              str
        merchant_customer_id:    str
        name:                    str
        passenger_name:          str
        place_of_issue:          str
        pnr:                     str
        point_of_sale:           str
        pos_city_code:           str
        ticket_delivery_method:  str
        ticket_number:           str
     """

    agent_numeric_code = None
    code = None
    flight_date = None
    flight_legs = None
    invoice_number = None
    is_e_ticket = None
    is_registered_customer = None
    is_restricted_ticket = None
    is_third_party = None
    issue_date = None
    merchant_customer_id = None
    name = None
    passenger_name = None
    place_of_issue = None
    pnr = None
    point_of_sale = None
    pos_city_code = None
    ticket_delivery_method = None
    ticket_number = None

    def to_dictionary(self):
        dictionary = super(AirlineData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'agentNumericCode', self.agent_numeric_code)
        self._add_to_dictionary(dictionary, 'code', self.code)
        self._add_to_dictionary(dictionary, 'flightDate', self.flight_date)
        self._add_to_dictionary(dictionary, 'flightLegs', self.flight_legs)
        self._add_to_dictionary(dictionary, 'invoiceNumber', self.invoice_number)
        self._add_to_dictionary(dictionary, 'isETicket', self.is_e_ticket)
        self._add_to_dictionary(dictionary, 'isRegisteredCustomer', self.is_registered_customer)
        self._add_to_dictionary(dictionary, 'isRestrictedTicket', self.is_restricted_ticket)
        self._add_to_dictionary(dictionary, 'isThirdParty', self.is_third_party)
        self._add_to_dictionary(dictionary, 'issueDate', self.issue_date)
        self._add_to_dictionary(dictionary, 'merchantCustomerId', self.merchant_customer_id)
        self._add_to_dictionary(dictionary, 'name', self.name)
        self._add_to_dictionary(dictionary, 'passengerName', self.passenger_name)
        self._add_to_dictionary(dictionary, 'placeOfIssue', self.place_of_issue)
        self._add_to_dictionary(dictionary, 'pnr', self.pnr)
        self._add_to_dictionary(dictionary, 'pointOfSale', self.point_of_sale)
        self._add_to_dictionary(dictionary, 'posCityCode', self.pos_city_code)
        self._add_to_dictionary(dictionary, 'ticketDeliveryMethod', self.ticket_delivery_method)
        self._add_to_dictionary(dictionary, 'ticketNumber', self.ticket_number)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AirlineData, self).from_dictionary(dictionary)
        if 'agentNumericCode' in dictionary:
            self.agent_numeric_code = dictionary['agentNumericCode']
        if 'code' in dictionary:
            self.code = dictionary['code']
        if 'flightDate' in dictionary:
            self.flight_date = dictionary['flightDate']
        if 'flightLegs' in dictionary:
            if not isinstance(dictionary['flightLegs'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['flightLegs']))
            self.flight_legs = []
            for flightLegs_element in dictionary['flightLegs']:
                flightLegs_value = AirlineFlightLeg()
                self.flight_legs.append(flightLegs_value.from_dictionary(flightLegs_element))
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'isETicket' in dictionary:
            self.is_e_ticket = dictionary['isETicket']
        if 'isRegisteredCustomer' in dictionary:
            self.is_registered_customer = dictionary['isRegisteredCustomer']
        if 'isRestrictedTicket' in dictionary:
            self.is_restricted_ticket = dictionary['isRestrictedTicket']
        if 'isThirdParty' in dictionary:
            self.is_third_party = dictionary['isThirdParty']
        if 'issueDate' in dictionary:
            self.issue_date = dictionary['issueDate']
        if 'merchantCustomerId' in dictionary:
            self.merchant_customer_id = dictionary['merchantCustomerId']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'passengerName' in dictionary:
            self.passenger_name = dictionary['passengerName']
        if 'placeOfIssue' in dictionary:
            self.place_of_issue = dictionary['placeOfIssue']
        if 'pnr' in dictionary:
            self.pnr = dictionary['pnr']
        if 'pointOfSale' in dictionary:
            self.point_of_sale = dictionary['pointOfSale']
        if 'posCityCode' in dictionary:
            self.pos_city_code = dictionary['posCityCode']
        if 'ticketDeliveryMethod' in dictionary:
            self.ticket_delivery_method = dictionary['ticketDeliveryMethod']
        if 'ticketNumber' in dictionary:
            self.ticket_number = dictionary['ticketNumber']
        return self
