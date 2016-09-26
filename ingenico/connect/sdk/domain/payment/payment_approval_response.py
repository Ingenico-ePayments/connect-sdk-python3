#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_card_payment_method_specific_output import ApprovePaymentCardPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment


class PaymentApprovalResponse(DataObject):
    """
    Class PaymentApprovalResponse
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentApprovalResponse
    
    Attributes:
        payment:                         :class:`Payment`
        payment_method_specific_output:  :class:`ApprovePaymentCardPaymentMethodSpecificOutput`
     """

    payment = None
    payment_method_specific_output = None

    def to_dictionary(self):
        dictionary = super(PaymentApprovalResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'payment', self.payment)
        self._add_to_dictionary(dictionary, 'paymentMethodSpecificOutput', self.payment_method_specific_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentApprovalResponse, self).from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentMethodSpecificOutput']))
            value = ApprovePaymentCardPaymentMethodSpecificOutput()
            self.payment_method_specific_output = value.from_dictionary(dictionary['paymentMethodSpecificOutput'])
        return self
