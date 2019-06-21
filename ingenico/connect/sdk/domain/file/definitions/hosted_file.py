# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class HostedFile(DataObject):
    """
    | File items.
    """

    __file_name = None
    __file_size = None
    __file_type = None
    __id = None

    @property
    def file_name(self):
        """
        | The name of the file.
        
        Type: str
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def file_size(self):
        """
        | The size of the file in bytes.
        
        Type: str
        """
        return self.__file_size

    @file_size.setter
    def file_size(self, value):
        self.__file_size = value

    @property
    def file_type(self):
        """
        | The type of the file.
        
        Type: str
        """
        return self.__file_type

    @file_type.setter
    def file_type(self, value):
        self.__file_type = value

    @property
    def id(self):
        """
        | The numeric identifier of the file.
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def to_dictionary(self):
        dictionary = super(HostedFile, self).to_dictionary()
        if self.file_name is not None:
            dictionary['fileName'] = self.file_name
        if self.file_size is not None:
            dictionary['fileSize'] = self.file_size
        if self.file_type is not None:
            dictionary['fileType'] = self.file_type
        if self.id is not None:
            dictionary['id'] = self.id
        return dictionary

    def from_dictionary(self, dictionary):
        super(HostedFile, self).from_dictionary(dictionary)
        if 'fileName' in dictionary:
            self.file_name = dictionary['fileName']
        if 'fileSize' in dictionary:
            self.file_size = dictionary['fileSize']
        if 'fileType' in dictionary:
            self.file_type = dictionary['fileType']
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self
