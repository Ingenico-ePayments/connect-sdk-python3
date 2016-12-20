#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PayoutReferences(DataObject):
    """
    Class PayoutReferences
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PayoutReferences
    """

    __invoice_number = None
    __merchant_order_id = None
    __merchant_reference = None

    @property
    def invoice_number(self):
        """
        str
        """
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self.__invoice_number = value

    @property
    def merchant_order_id(self):
        """
        int
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self.__merchant_order_id = value

    @property
    def merchant_reference(self):
        """
        str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value):
        self.__merchant_reference = value

    def to_dictionary(self):
        dictionary = super(PayoutReferences, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'invoiceNumber', self.invoice_number)
        self._add_to_dictionary(dictionary, 'merchantOrderId', self.merchant_order_id)
        self._add_to_dictionary(dictionary, 'merchantReference', self.merchant_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutReferences, self).from_dictionary(dictionary)
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
