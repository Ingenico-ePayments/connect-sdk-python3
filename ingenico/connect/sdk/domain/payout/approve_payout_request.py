#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ApprovePayoutRequest(DataObject):
    """
    Class ApprovePayoutRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApprovePayoutRequest
    """

    __date_payout = None

    @property
    def date_payout(self):
        """
        str
        """
        return self.__date_payout

    @date_payout.setter
    def date_payout(self, value):
        self.__date_payout = value

    def to_dictionary(self):
        dictionary = super(ApprovePayoutRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'datePayout', self.date_payout)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePayoutRequest, self).from_dictionary(dictionary)
        if 'datePayout' in dictionary:
            self.date_payout = dictionary['datePayout']
        return self
