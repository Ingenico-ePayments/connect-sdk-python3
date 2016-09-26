#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ApproveRefundRequest(DataObject):
    """
    Class ApproveRefundRequest
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApproveRefundRequest
    
    Attributes:
        amount:  int
     """

    amount = None

    def to_dictionary(self):
        dictionary = super(ApproveRefundRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amount', self.amount)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApproveRefundRequest, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        return self
