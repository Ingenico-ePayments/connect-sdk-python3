#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RefundMethodSpecificOutput(DataObject):
    """
    Class RefundMethodSpecificOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundMethodSpecificOutput
    
    Attributes:
        total_amount_paid:      int
        total_amount_refunded:  int
     """

    total_amount_paid = None
    total_amount_refunded = None

    def to_dictionary(self):
        dictionary = super(RefundMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'totalAmountPaid', self.total_amount_paid)
        self._add_to_dictionary(dictionary, 'totalAmountRefunded', self.total_amount_refunded)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
