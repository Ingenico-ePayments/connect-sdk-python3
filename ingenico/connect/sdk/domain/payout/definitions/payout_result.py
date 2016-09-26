#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_order_status import AbstractOrderStatus
from ingenico.connect.sdk.domain.definitions.order_status_output import OrderStatusOutput
from ingenico.connect.sdk.domain.payment.definitions.order_output import OrderOutput


class PayoutResult(AbstractOrderStatus):
    """
    Class PayoutResult
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PayoutResult
    
    Attributes:
        payout_output:  :class:`OrderOutput`
        status:         str
        status_output:  :class:`OrderStatusOutput`
     """

    payout_output = None
    status = None
    status_output = None

    def to_dictionary(self):
        dictionary = super(PayoutResult, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'payoutOutput', self.payout_output)
        self._add_to_dictionary(dictionary, 'status', self.status)
        self._add_to_dictionary(dictionary, 'statusOutput', self.status_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutResult, self).from_dictionary(dictionary)
        if 'payoutOutput' in dictionary:
            if not isinstance(dictionary['payoutOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutOutput']))
            value = OrderOutput()
            self.payout_output = value.from_dictionary(dictionary['payoutOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = OrderStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
