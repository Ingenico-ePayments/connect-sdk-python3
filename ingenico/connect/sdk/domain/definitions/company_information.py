#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CompanyInformation(DataObject):
    """
    Class CompanyInformation
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CompanyInformation
    """

    __name = None

    @property
    def name(self):
        """
        str
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(CompanyInformation, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'name', self.name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CompanyInformation, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            self.name = dictionary['name']
        return self
