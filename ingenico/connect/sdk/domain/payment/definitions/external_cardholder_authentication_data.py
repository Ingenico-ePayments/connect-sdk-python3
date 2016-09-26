#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ExternalCardholderAuthenticationData(DataObject):
    """
    Class ExternalCardholderAuthenticationData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ExternalCardholderAuthenticationData
    
    Attributes:
        cavv:               str
        cavv_algorithm:     str
        eci:                int
        validation_result:  str
        xid:                str
     """

    cavv = None
    cavv_algorithm = None
    eci = None
    validation_result = None
    xid = None

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
