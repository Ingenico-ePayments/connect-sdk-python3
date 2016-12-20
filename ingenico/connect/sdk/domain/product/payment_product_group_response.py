#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.product.definitions.payment_product_group import PaymentProductGroup


class PaymentProductGroupResponse(PaymentProductGroup):
    """
    Class PaymentProductGroupResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductGroupResponse
    """

    def to_dictionary(self):
        dictionary = super(PaymentProductGroupResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductGroupResponse, self).from_dictionary(dictionary)
        return self
