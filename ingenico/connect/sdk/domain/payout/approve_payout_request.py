#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ApprovePayoutRequest(DataObject):
    """
    Class ApprovePayoutRequest
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApprovePayoutRequest
    
    Attributes:
        date_payout:  str
     """

    date_payout = None

    def to_dictionary(self):
        dictionary = super(ApprovePayoutRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'datePayout', self.date_payout)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePayoutRequest, self).from_dictionary(dictionary)
        if 'datePayout' in dictionary:
            self.date_payout = dictionary['datePayout']
        return self
