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
    """

    __refund_output = None
    __status = None
    __status_output = None

    @property
    def refund_output(self):
        """
        :class:`RefundOutput`
        """
        return self.__refund_output

    @refund_output.setter
    def refund_output(self, value):
        self.__refund_output = value

    @property
    def status(self):
        """
        str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def status_output(self):
        """
        :class:`OrderStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value):
        self.__status_output = value

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
