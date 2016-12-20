#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Address(DataObject):
    """
    Class Address
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Address
    """

    __additional_info = None
    __city = None
    __country_code = None
    __house_number = None
    __state = None
    __state_code = None
    __street = None
    __zip = None

    @property
    def additional_info(self):
        """
        str
        """
        return self.__additional_info

    @additional_info.setter
    def additional_info(self, value):
        self.__additional_info = value

    @property
    def city(self):
        """
        str
        """
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def country_code(self):
        """
        str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def house_number(self):
        """
        str
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, value):
        self.__house_number = value

    @property
    def state(self):
        """
        str
        """
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def state_code(self):
        """
        str
        """
        return self.__state_code

    @state_code.setter
    def state_code(self, value):
        self.__state_code = value

    @property
    def street(self):
        """
        str
        """
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def zip(self):
        """
        str
        """
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    def to_dictionary(self):
        dictionary = super(Address, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalInfo', self.additional_info)
        self._add_to_dictionary(dictionary, 'city', self.city)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        self._add_to_dictionary(dictionary, 'houseNumber', self.house_number)
        self._add_to_dictionary(dictionary, 'state', self.state)
        self._add_to_dictionary(dictionary, 'stateCode', self.state_code)
        self._add_to_dictionary(dictionary, 'street', self.street)
        self._add_to_dictionary(dictionary, 'zip', self.zip)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Address, self).from_dictionary(dictionary)
        if 'additionalInfo' in dictionary:
            self.additional_info = dictionary['additionalInfo']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'state' in dictionary:
            self.state = dictionary['state']
        if 'stateCode' in dictionary:
            self.state_code = dictionary['stateCode']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
