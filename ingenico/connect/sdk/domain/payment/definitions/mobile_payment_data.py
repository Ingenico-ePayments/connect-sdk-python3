#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class MobilePaymentData(DataObject):
    """
    Class MobilePaymentData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MobilePaymentData
    """

    __dpan = None
    __expiry_date = None

    @property
    def dpan(self):
        """
        str
        """
        return self.__dpan

    @dpan.setter
    def dpan(self, value):
        self.__dpan = value

    @property
    def expiry_date(self):
        """
        str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dpan', self.dpan)
        self._add_to_dictionary(dictionary, 'expiryDate', self.expiry_date)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentData, self).from_dictionary(dictionary)
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
