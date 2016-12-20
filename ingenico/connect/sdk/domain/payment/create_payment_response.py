#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.create_payment_result import CreatePaymentResult


class CreatePaymentResponse(CreatePaymentResult):
    """
    Class CreatePaymentResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreatePaymentResponse
    """

    def to_dictionary(self):
        dictionary = super(CreatePaymentResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentResponse, self).from_dictionary(dictionary)
        return self
