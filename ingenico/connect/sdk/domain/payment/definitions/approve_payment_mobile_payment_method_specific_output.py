#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ApprovePaymentMobilePaymentMethodSpecificOutput(DataObject):
    """
    Class ApprovePaymentMobilePaymentMethodSpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApprovePaymentMobilePaymentMethodSpecificOutput
    """

    __void_response_id = None

    @property
    def void_response_id(self):
        """
        str
        """
        return self.__void_response_id

    @void_response_id.setter
    def void_response_id(self, value):
        self.__void_response_id = value

    def to_dictionary(self):
        dictionary = super(ApprovePaymentMobilePaymentMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'voidResponseId', self.void_response_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePaymentMobilePaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'voidResponseId' in dictionary:
            self.void_response_id = dictionary['voidResponseId']
        return self
