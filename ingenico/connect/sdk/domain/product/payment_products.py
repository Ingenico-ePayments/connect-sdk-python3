#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product import PaymentProduct


class PaymentProducts(DataObject):
    """
    Class PaymentProducts
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProducts
    
    Attributes:
        payment_products:  list[:class:`PaymentProduct`]
     """

    payment_products = None

    def to_dictionary(self):
        dictionary = super(PaymentProducts, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProducts', self.payment_products)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProducts, self).from_dictionary(dictionary)
        if 'paymentProducts' in dictionary:
            if not isinstance(dictionary['paymentProducts'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProducts']))
            self.payment_products = []
            for paymentProducts_element in dictionary['paymentProducts']:
                paymentProducts_value = PaymentProduct()
                self.payment_products.append(paymentProducts_value.from_dictionary(paymentProducts_element))
        return self
