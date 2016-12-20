#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class DirectoryEntry(DataObject):
    """
    Class DirectoryEntry
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_DirectoryEntry
    """

    __country_names = None
    __issuer_id = None
    __issuer_list = None
    __issuer_name = None

    @property
    def country_names(self):
        """
        list[str]
        """
        return self.__country_names

    @country_names.setter
    def country_names(self, value):
        self.__country_names = value

    @property
    def issuer_id(self):
        """
        str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value):
        self.__issuer_id = value

    @property
    def issuer_list(self):
        """
        str
        """
        return self.__issuer_list

    @issuer_list.setter
    def issuer_list(self, value):
        self.__issuer_list = value

    @property
    def issuer_name(self):
        """
        str
        """
        return self.__issuer_name

    @issuer_name.setter
    def issuer_name(self, value):
        self.__issuer_name = value

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
