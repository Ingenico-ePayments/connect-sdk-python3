#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Creditor(DataObject):
    """
    Class Creditor
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Creditor
    
    Attributes:
        additional_address_info:  str
        city:                     str
        country_code:             str
        house_number:             str
        iban:                     str
        id:                       str
        name:                     str
        reference_party:          str
        reference_party_id:       str
        street:                   str
        zip:                      str
     """

    additional_address_info = None
    city = None
    country_code = None
    house_number = None
    iban = None
    id = None
    name = None
    reference_party = None
    reference_party_id = None
    street = None
    zip = None

    def to_dictionary(self):
        dictionary = super(Creditor, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalAddressInfo', self.additional_address_info)
        self._add_to_dictionary(dictionary, 'city', self.city)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        self._add_to_dictionary(dictionary, 'houseNumber', self.house_number)
        self._add_to_dictionary(dictionary, 'iban', self.iban)
        self._add_to_dictionary(dictionary, 'id', self.id)
        self._add_to_dictionary(dictionary, 'name', self.name)
        self._add_to_dictionary(dictionary, 'referenceParty', self.reference_party)
        self._add_to_dictionary(dictionary, 'referencePartyId', self.reference_party_id)
        self._add_to_dictionary(dictionary, 'street', self.street)
        self._add_to_dictionary(dictionary, 'zip', self.zip)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Creditor, self).from_dictionary(dictionary)
        if 'additionalAddressInfo' in dictionary:
            self.additional_address_info = dictionary['additionalAddressInfo']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'referenceParty' in dictionary:
            self.reference_party = dictionary['referenceParty']
        if 'referencePartyId' in dictionary:
            self.reference_party_id = dictionary['referencePartyId']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
