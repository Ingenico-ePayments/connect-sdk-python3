#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class OrderTypeInformation(DataObject):
    """
    Class OrderTypeInformation
    See also https://developer.globalcollect.com/documentation/api/server/#schema_OrderTypeInformation
    
    Attributes:
        purchase_type:  str
        usage_type:     str
     """

    purchase_type = None
    usage_type = None

    def to_dictionary(self):
        dictionary = super(OrderTypeInformation, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'purchaseType', self.purchase_type)
        self._add_to_dictionary(dictionary, 'usageType', self.usage_type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderTypeInformation, self).from_dictionary(dictionary)
        if 'purchaseType' in dictionary:
            self.purchase_type = dictionary['purchaseType']
        if 'usageType' in dictionary:
            self.usage_type = dictionary['usageType']
        return self
