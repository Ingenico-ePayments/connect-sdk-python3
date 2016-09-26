#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Level3SummaryData(DataObject):
    """
    Class Level3SummaryData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Level3SummaryData
    
    Attributes:
        discount_amount:  int
        duty_amount:      int
        shipping_amount:  int
     """

    discount_amount = None
    duty_amount = None
    shipping_amount = None

    def to_dictionary(self):
        dictionary = super(Level3SummaryData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'discountAmount', self.discount_amount)
        self._add_to_dictionary(dictionary, 'dutyAmount', self.duty_amount)
        self._add_to_dictionary(dictionary, 'shippingAmount', self.shipping_amount)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Level3SummaryData, self).from_dictionary(dictionary)
        if 'discountAmount' in dictionary:
            self.discount_amount = dictionary['discountAmount']
        if 'dutyAmount' in dictionary:
            self.duty_amount = dictionary['dutyAmount']
        if 'shippingAmount' in dictionary:
            self.shipping_amount = dictionary['shippingAmount']
        return self
