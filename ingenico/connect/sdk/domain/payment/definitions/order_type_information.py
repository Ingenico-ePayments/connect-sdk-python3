#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class OrderTypeInformation(DataObject):
    """
    Class OrderTypeInformation
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_OrderTypeInformation
    """

    __purchase_type = None
    __usage_type = None

    @property
    def purchase_type(self):
        """
        str
        """
        return self.__purchase_type

    @purchase_type.setter
    def purchase_type(self, value):
        self.__purchase_type = value

    @property
    def usage_type(self):
        """
        str
        """
        return self.__usage_type

    @usage_type.setter
    def usage_type(self, value):
        self.__usage_type = value

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
