#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RefundReferences(DataObject):
    """
    Class RefundReferences
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundReferences
    """

    __merchant_reference = None

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
        dictionary = super(RefundReferences, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'merchantReference', self.merchant_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundReferences, self).from_dictionary(dictionary)
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
