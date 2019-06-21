# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.directory_entry import DirectoryEntry


class Directory(DataObject):

    __entries = None

    @property
    def entries(self):
        """
        | List of entries in the directory
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.directory_entry.DirectoryEntry`]
        """
        return self.__entries

    @entries.setter
    def entries(self, value):
        self.__entries = value

    def to_dictionary(self):
        dictionary = super(Directory, self).to_dictionary()
        if self.entries is not None:
            dictionary['entries'] = []
            for element in self.entries:
                if element is not None:
                    dictionary['entries'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(Directory, self).from_dictionary(dictionary)
        if 'entries' in dictionary:
            if not isinstance(dictionary['entries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entries']))
            self.entries = []
            for element in dictionary['entries']:
                value = DirectoryEntry()
                self.entries.append(value.from_dictionary(element))
        return self
