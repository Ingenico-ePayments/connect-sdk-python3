#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ExternalCardholderAuthenticationData(DataObject):
    """
    Class ExternalCardholderAuthenticationData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ExternalCardholderAuthenticationData
    """

    __cavv = None
    __cavv_algorithm = None
    __eci = None
    __validation_result = None
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
    def cavv_algorithm(self):
        """
        str
        """
        return self.__cavv_algorithm

    @cavv_algorithm.setter
    def cavv_algorithm(self, value):
        self.__cavv_algorithm = value

    @property
    def eci(self):
        """
        int
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def validation_result(self):
        """
        str
        """
        return self.__validation_result

    @validation_result.setter
    def validation_result(self, value):
        self.__validation_result = value

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
        dictionary = super(ExternalCardholderAuthenticationData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cavv', self.cavv)
        self._add_to_dictionary(dictionary, 'cavvAlgorithm', self.cavv_algorithm)
        self._add_to_dictionary(dictionary, 'eci', self.eci)
        self._add_to_dictionary(dictionary, 'validationResult', self.validation_result)
        self._add_to_dictionary(dictionary, 'xid', self.xid)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ExternalCardholderAuthenticationData, self).from_dictionary(dictionary)
        if 'cavv' in dictionary:
            self.cavv = dictionary['cavv']
        if 'cavvAlgorithm' in dictionary:
            self.cavv_algorithm = dictionary['cavvAlgorithm']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'validationResult' in dictionary:
            self.validation_result = dictionary['validationResult']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self
