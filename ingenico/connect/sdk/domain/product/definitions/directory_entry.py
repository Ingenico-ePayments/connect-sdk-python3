#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class DirectoryEntry(DataObject):
    """
    Class DirectoryEntry
    See also https://developer.globalcollect.com/documentation/api/server/#schema_DirectoryEntry
    
    Attributes:
        country_names:  list[str]
        issuer_id:      str
        issuer_list:    str
        issuer_name:    str
     """

    country_names = None
    issuer_id = None
    issuer_list = None
    issuer_name = None

    def to_dictionary(self):
        dictionary = super(DirectoryEntry, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'countryNames', self.country_names)
        self._add_to_dictionary(dictionary, 'issuerId', self.issuer_id)
        self._add_to_dictionary(dictionary, 'issuerList', self.issuer_list)
        self._add_to_dictionary(dictionary, 'issuerName', self.issuer_name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(DirectoryEntry, self).from_dictionary(dictionary)
        if 'countryNames' in dictionary:
            if not isinstance(dictionary['countryNames'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['countryNames']))
            self.country_names = []
            for countryNames_element in dictionary['countryNames']:
                self.country_names.append(countryNames_element)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        if 'issuerList' in dictionary:
            self.issuer_list = dictionary['issuerList']
        if 'issuerName' in dictionary:
            self.issuer_name = dictionary['issuerName']
        return self
