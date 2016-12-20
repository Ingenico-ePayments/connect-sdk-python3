#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.abstract_order_status import AbstractOrderStatus
from ingenico.connect.sdk.domain.payment.definitions.payment_output import PaymentOutput
from ingenico.connect.sdk.domain.payment.definitions.payment_status_output import PaymentStatusOutput


class Payment(AbstractOrderStatus):
    """
    Class Payment
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Payment
    """

    __payment_output = None
    __status = None
    __status_output = None

    @property
    def payment_output(self):
        """
        :class:`PaymentOutput`
        """
        return self.__payment_output

    @payment_output.setter
    def payment_output(self, value):
        self.__payment_output = value

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
        :class:`PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value):
        self.__status_output = value

    def to_dictionary(self):
        dictionary = super(Payment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentOutput', self.payment_output)
        self._add_to_dictionary(dictionary, 'status', self.status)
        self._add_to_dictionary(dictionary, 'statusOutput', self.status_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Payment, self).from_dictionary(dictionary)
        if 'paymentOutput' in dictionary:
            if not isinstance(dictionary['paymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentOutput']))
            value = PaymentOutput()
            self.payment_output = value.from_dictionary(dictionary['paymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PaymentStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
