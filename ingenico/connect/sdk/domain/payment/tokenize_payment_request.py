#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class TokenizePaymentRequest(DataObject):
    """
    Class TokenizePaymentRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenizePaymentRequest
    """

    __alias = None

    @property
    def alias(self):
        """
        str
        """
        return self.__alias

    @alias.setter
    def alias(self, value):
        self.__alias = value

    def to_dictionary(self):
        dictionary = super(TokenizePaymentRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'alias', self.alias)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenizePaymentRequest, self).from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        return self
