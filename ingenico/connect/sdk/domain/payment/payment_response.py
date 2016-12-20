#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment


class PaymentResponse(Payment):
    """
    Class PaymentResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentResponse
    """

    def to_dictionary(self):
        dictionary = super(PaymentResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentResponse, self).from_dictionary(dictionary)
        return self
