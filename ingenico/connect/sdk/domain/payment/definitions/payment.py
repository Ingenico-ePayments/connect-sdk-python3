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
    
    Attributes:
        payment_output:  :class:`PaymentOutput`
        status:          str
        status_output:   :class:`PaymentStatusOutput`
     """

    payment_output = None
    status = None
    status_output = None

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
