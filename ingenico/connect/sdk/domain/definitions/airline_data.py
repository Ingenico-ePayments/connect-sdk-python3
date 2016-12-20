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
    """

    __agent_numeric_code = None
    __code = None
    __flight_date = None
    __flight_legs = None
    __invoice_number = None
    __is_e_ticket = None
    __is_registered_customer = None
    __is_restricted_ticket = None
    __is_third_party = None
    __issue_date = None
    __merchant_customer_id = None
    __name = None
    __passenger_name = None
    __place_of_issue = None
    __pnr = None
    __point_of_sale = None
    __pos_city_code = None
    __ticket_delivery_method = None
    __ticket_number = None

    @property
    def agent_numeric_code(self):
        """
        str
        """
        return self.__agent_numeric_code

    @agent_numeric_code.setter
    def agent_numeric_code(self, value):
        self.__agent_numeric_code = value

    @property
    def code(self):
        """
        str
        """
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def flight_date(self):
        """
        str
        """
        return self.__flight_date

    @flight_date.setter
    def flight_date(self, value):
        self.__flight_date = value

    @property
    def flight_legs(self):
        """
        list[:class:`AirlineFlightLeg`]
        """
        return self.__flight_legs

    @flight_legs.setter
    def flight_legs(self, value):
        self.__flight_legs = value

    @property
    def invoice_number(self):
        """
        str
        """
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self.__invoice_number = value

    @property
    def is_e_ticket(self):
        """
        bool
        """
        return self.__is_e_ticket

    @is_e_ticket.setter
    def is_e_ticket(self, value):
        self.__is_e_ticket = value

    @property
    def is_registered_customer(self):
        """
        bool
        """
        return self.__is_registered_customer

    @is_registered_customer.setter
    def is_registered_customer(self, value):
        self.__is_registered_customer = value

    @property
    def is_restricted_ticket(self):
        """
        bool
        """
        return self.__is_restricted_ticket

    @is_restricted_ticket.setter
    def is_restricted_ticket(self, value):
        self.__is_restricted_ticket = value

    @property
    def is_third_party(self):
        """
        bool
        """
        return self.__is_third_party

    @is_third_party.setter
    def is_third_party(self, value):
        self.__is_third_party = value

    @property
    def issue_date(self):
        """
        str
        """
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, value):
        self.__issue_date = value

    @property
    def merchant_customer_id(self):
        """
        str
        """
        return self.__merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, value):
        self.__merchant_customer_id = value

    @property
    def name(self):
        """
        str
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def passenger_name(self):
        """
        str
        """
        return self.__passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self.__passenger_name = value

    @property
    def place_of_issue(self):
        """
        str
        """
        return self.__place_of_issue

    @place_of_issue.setter
    def place_of_issue(self, value):
        self.__place_of_issue = value

    @property
    def pnr(self):
        """
        str
        """
        return self.__pnr

    @pnr.setter
    def pnr(self, value):
        self.__pnr = value

    @property
    def point_of_sale(self):
        """
        str
        """
        return self.__point_of_sale

    @point_of_sale.setter
    def point_of_sale(self, value):
        self.__point_of_sale = value

    @property
    def pos_city_code(self):
        """
        str
        """
        return self.__pos_city_code

    @pos_city_code.setter
    def pos_city_code(self, value):
        self.__pos_city_code = value

    @property
    def ticket_delivery_method(self):
        """
        str
        """
        return self.__ticket_delivery_method

    @ticket_delivery_method.setter
    def ticket_delivery_method(self, value):
        self.__ticket_delivery_method = value

    @property
    def ticket_number(self):
        """
        str
        """
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, value):
        self.__ticket_number = value

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
