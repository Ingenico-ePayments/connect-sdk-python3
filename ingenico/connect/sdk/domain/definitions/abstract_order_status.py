#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class AbstractOrderStatus(DataObject):
    """
    Class AbstractOrderStatus
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AbstractOrderStatus
    """

    __id = None

    @property
    def id(self):
        """
        str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def to_dictionary(self):
        dictionary = super(AbstractOrderStatus, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'id', self.id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractOrderStatus, self).from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self
