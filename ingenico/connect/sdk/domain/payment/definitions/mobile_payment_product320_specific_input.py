#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class MobilePaymentProduct320SpecificInput(DataObject):
    """
    Class MobilePaymentProduct320SpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MobilePaymentProduct320SpecificInput
    """

    __key_id = None

    @property
    def key_id(self):
        """
        str
        """
        return self.__key_id

    @key_id.setter
    def key_id(self, value):
        self.__key_id = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentProduct320SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'keyId', self.key_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentProduct320SpecificInput, self).from_dictionary(dictionary)
        if 'keyId' in dictionary:
            self.key_id = dictionary['keyId']
        return self
