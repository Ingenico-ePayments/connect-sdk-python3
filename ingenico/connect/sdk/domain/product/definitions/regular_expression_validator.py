#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RegularExpressionValidator(DataObject):
    """
    Class RegularExpressionValidator
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RegularExpressionValidator
    
    Attributes:
        regular_expression:  str
     """

    regular_expression = None

    def to_dictionary(self):
        dictionary = super(RegularExpressionValidator, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'regularExpression', self.regular_expression)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RegularExpressionValidator, self).from_dictionary(dictionary)
        if 'regularExpression' in dictionary:
            self.regular_expression = dictionary['regularExpression']
        return self
