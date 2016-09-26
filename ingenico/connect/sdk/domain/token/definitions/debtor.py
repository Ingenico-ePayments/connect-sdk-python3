#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Debtor(DataObject):
    """
    Class Debtor
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Debtor
    
    Attributes:
        additional_address_info:  str
        city:                     str
        country_code:             str
        first_name:               str
        house_number:             str
        state:                    str
        state_code:               str
        street:                   str
        surname:                  str
        surname_prefix:           str
        zip:                      str
     """

    additional_address_info = None
    city = None
    country_code = None
    first_name = None
    house_number = None
    state = None
    state_code = None
    street = None
    surname = None
    surname_prefix = None
    zip = None

    def to_dictionary(self):
        dictionary = super(Debtor, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalAddressInfo', self.additional_address_info)
        self._add_to_dictionary(dictionary, 'city', self.city)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        self._add_to_dictionary(dictionary, 'firstName', self.first_name)
        self._add_to_dictionary(dictionary, 'houseNumber', self.house_number)
        self._add_to_dictionary(dictionary, 'state', self.state)
        self._add_to_dictionary(dictionary, 'stateCode', self.state_code)
        self._add_to_dictionary(dictionary, 'street', self.street)
        self._add_to_dictionary(dictionary, 'surname', self.surname)
        self._add_to_dictionary(dictionary, 'surnamePrefix', self.surname_prefix)
        self._add_to_dictionary(dictionary, 'zip', self.zip)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Debtor, self).from_dictionary(dictionary)
        if 'additionalAddressInfo' in dictionary:
            self.additional_address_info = dictionary['additionalAddressInfo']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'state' in dictionary:
            self.state = dictionary['state']
        if 'stateCode' in dictionary:
            self.state_code = dictionary['stateCode']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'surnamePrefix' in dictionary:
            self.surname_prefix = dictionary['surnamePrefix']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
