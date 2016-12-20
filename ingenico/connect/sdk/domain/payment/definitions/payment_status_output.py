#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.order_status_output import OrderStatusOutput


class PaymentStatusOutput(OrderStatusOutput):
    """
    Class PaymentStatusOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentStatusOutput
    """

    __is_authorized = None
    __is_refundable = None

    @property
    def is_authorized(self):
        """
        bool
        """
        return self.__is_authorized

    @is_authorized.setter
    def is_authorized(self, value):
        self.__is_authorized = value

    @property
    def is_refundable(self):
        """
        bool
        """
        return self.__is_refundable

    @is_refundable.setter
    def is_refundable(self, value):
        self.__is_refundable = value

    def to_dictionary(self):
        dictionary = super(PaymentStatusOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'isAuthorized', self.is_authorized)
        self._add_to_dictionary(dictionary, 'isRefundable', self.is_refundable)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentStatusOutput, self).from_dictionary(dictionary)
        if 'isAuthorized' in dictionary:
            self.is_authorized = dictionary['isAuthorized']
        if 'isRefundable' in dictionary:
            self.is_refundable = dictionary['isRefundable']
        return self
