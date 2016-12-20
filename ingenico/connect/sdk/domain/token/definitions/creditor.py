#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Creditor(DataObject):
    """
    Class Creditor
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Creditor
    """

    __additional_address_info = None
    __city = None
    __country_code = None
    __house_number = None
    __iban = None
    __id = None
    __name = None
    __reference_party = None
    __reference_party_id = None
    __street = None
    __zip = None

    @property
    def additional_address_info(self):
        """
        str
        """
        return self.__additional_address_info

    @additional_address_info.setter
    def additional_address_info(self, value):
        self.__additional_address_info = value

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
    def iban(self):
        """
        str
        """
        return self.__iban

    @iban.setter
    def iban(self, value):
        self.__iban = value

    @property
    def id(self):
        """
        str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

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
    def reference_party(self):
        """
        str
        """
        return self.__reference_party

    @reference_party.setter
    def reference_party(self, value):
        self.__reference_party = value

    @property
    def reference_party_id(self):
        """
        str
        """
        return self.__reference_party_id

    @reference_party_id.setter
    def reference_party_id(self, value):
        self.__reference_party_id = value

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
