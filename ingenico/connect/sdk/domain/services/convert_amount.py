#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ConvertAmount(DataObject):
    """
    Class ConvertAmount
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ConvertAmount
    
    Attributes:
        converted_amount:  int
     """

    converted_amount = None

    def to_dictionary(self):
        dictionary = super(ConvertAmount, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'convertedAmount', self.converted_amount)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ConvertAmount, self).from_dictionary(dictionary)
        if 'convertedAmount' in dictionary:
            self.converted_amount = dictionary['convertedAmount']
        return self
