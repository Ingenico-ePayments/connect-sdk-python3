#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ThreeDSecureResults(DataObject):
    """
    Class ThreeDSecureResults
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ThreeDSecureResults
    """

    __cavv = None
    __eci = None
    __xid = None

    @property
    def cavv(self):
        """
        str
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value

    @property
    def eci(self):
        """
        str
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def xid(self):
        """
        str
        """
        return self.__xid

    @xid.setter
    def xid(self, value):
        self.__xid = value

    def to_dictionary(self):
        dictionary = super(ThreeDSecureResults, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cavv', self.cavv)
        self._add_to_dictionary(dictionary, 'eci', self.eci)
        self._add_to_dictionary(dictionary, 'xid', self.xid)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSecureResults, self).from_dictionary(dictionary)
        if 'cavv' in dictionary:
            self.cavv = dictionary['cavv']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self
