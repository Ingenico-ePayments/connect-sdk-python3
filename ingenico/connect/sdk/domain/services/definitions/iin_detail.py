#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class IINDetail(DataObject):
    """
    Class IINDetail
    See also https://developer.globalcollect.com/documentation/api/server/#schema_IINDetail
    
    Attributes:
        is_allowed_in_context:  bool
        payment_product_id:     int
     """

    is_allowed_in_context = None
    payment_product_id = None

    def to_dictionary(self):
        dictionary = super(IINDetail, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'isAllowedInContext', self.is_allowed_in_context)
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(IINDetail, self).from_dictionary(dictionary)
        if 'isAllowedInContext' in dictionary:
            self.is_allowed_in_context = dictionary['isAllowedInContext']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
