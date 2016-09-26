#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_order_status import AbstractOrderStatus
from ingenico.connect.sdk.domain.definitions.order_status_output import OrderStatusOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_output import RefundOutput


class RefundResult(AbstractOrderStatus):
    """
    Class RefundResult
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundResult
    
    Attributes:
        refund_output:  :class:`RefundOutput`
        status:         str
        status_output:  :class:`OrderStatusOutput`
     """

    refund_output = None
    status = None
    status_output = None

    def to_dictionary(self):
        dictionary = super(RefundResult, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'refundOutput', self.refund_output)
        self._add_to_dictionary(dictionary, 'status', self.status)
        self._add_to_dictionary(dictionary, 'statusOutput', self.status_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundResult, self).from_dictionary(dictionary)
        if 'refundOutput' in dictionary:
            if not isinstance(dictionary['refundOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundOutput']))
            value = RefundOutput()
            self.refund_output = value.from_dictionary(dictionary['refundOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = OrderStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
