#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.directory_entry import DirectoryEntry


class Directory(DataObject):
    """
    Class Directory
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Directory
    """

    __entries = None

    @property
    def entries(self):
        """
        list[:class:`DirectoryEntry`]
        """
        return self.__entries

    @entries.setter
    def entries(self, value):
        self.__entries = value

    def to_dictionary(self):
        dictionary = super(Directory, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'entries', self.entries)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Directory, self).from_dictionary(dictionary)
        if 'entries' in dictionary:
            if not isinstance(dictionary['entries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entries']))
            self.entries = []
            for entries_element in dictionary['entries']:
                entries_value = DirectoryEntry()
                self.entries.append(entries_value.from_dictionary(entries_element))
        return self
