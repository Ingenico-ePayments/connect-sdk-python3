#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ThreeDSecureResults(DataObject):
    """
    Class ThreeDSecureResults
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ThreeDSecureResults
    
    Attributes:
        cavv:  str
        eci:   str
        xid:   str
     """

    cavv = None
    eci = None
    xid = None

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
