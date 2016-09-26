#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Address(DataObject):
    """
    Class Address
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Address
    
    Attributes:
        additional_info:  str
        city:             str
        country_code:     str
        house_number:     str
        state:            str
        state_code:       str
        street:           str
        zip:              str
     """

    additional_info = None
    city = None
    country_code = None
    house_number = None
    state = None
    state_code = None
    street = None
    zip = None

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
