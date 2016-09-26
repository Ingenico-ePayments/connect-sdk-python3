#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class CancelPaymentCardPaymentMethodSpecificOutput(DataObject):
    """
    Class CancelPaymentCardPaymentMethodSpecificOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CancelPaymentCardPaymentMethodSpecificOutput
    
    Attributes:
        void_response_id:  str
     """

    void_response_id = None

    def to_dictionary(self):
        dictionary = super(CancelPaymentCardPaymentMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'voidResponseId', self.void_response_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CancelPaymentCardPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'voidResponseId' in dictionary:
            self.void_response_id = dictionary['voidResponseId']
        return self
