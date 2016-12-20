#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment


class CancelApprovalPaymentResponse(DataObject):
    """
    Class CancelApprovalPaymentResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CancelApprovalPaymentResponse
    """

    __payment = None

    @property
    def payment(self):
        """
        :class:`Payment`
        """
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    def to_dictionary(self):
        dictionary = super(CancelApprovalPaymentResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'payment', self.payment)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CancelApprovalPaymentResponse, self).from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self
