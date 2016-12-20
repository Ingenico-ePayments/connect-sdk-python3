#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.product.definitions.payment_product import PaymentProduct


class PaymentProductResponse(PaymentProduct):
    """
    Class PaymentProductResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductResponse
    """

    def to_dictionary(self):
        dictionary = super(PaymentProductResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductResponse, self).from_dictionary(dictionary)
        return self
