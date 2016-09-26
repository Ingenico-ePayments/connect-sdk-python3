#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentReferences(DataObject):
    """
    Class PaymentReferences
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentReferences
    
    Attributes:
        merchant_order_id:       int
        merchant_reference:      str
        payment_reference:       str
        provider_id:             str
        provider_reference:      str
        reference_orig_payment:  str
     """

    merchant_order_id = None
    merchant_reference = None
    payment_reference = None
    provider_id = None
    provider_reference = None
    reference_orig_payment = None

    def to_dictionary(self):
        dictionary = super(PaymentReferences, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'merchantOrderId', self.merchant_order_id)
        self._add_to_dictionary(dictionary, 'merchantReference', self.merchant_reference)
        self._add_to_dictionary(dictionary, 'paymentReference', self.payment_reference)
        self._add_to_dictionary(dictionary, 'providerId', self.provider_id)
        self._add_to_dictionary(dictionary, 'providerReference', self.provider_reference)
        self._add_to_dictionary(dictionary, 'referenceOrigPayment', self.reference_orig_payment)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentReferences, self).from_dictionary(dictionary)
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'providerId' in dictionary:
            self.provider_id = dictionary['providerId']
        if 'providerReference' in dictionary:
            self.provider_reference = dictionary['providerReference']
        if 'referenceOrigPayment' in dictionary:
            self.reference_orig_payment = dictionary['referenceOrigPayment']
        return self
