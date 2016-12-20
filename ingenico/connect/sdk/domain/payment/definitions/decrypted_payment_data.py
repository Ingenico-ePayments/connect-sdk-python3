#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class DecryptedPaymentData(DataObject):
    """
    Class DecryptedPaymentData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_DecryptedPaymentData
    """

    __cardholder_name = None
    __cryptogram = None
    __dpan = None
    __eci = None
    __expiry_date = None

    @property
    def cardholder_name(self):
        """
        str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value):
        self.__cardholder_name = value

    @property
    def cryptogram(self):
        """
        str
        """
        return self.__cryptogram

    @cryptogram.setter
    def cryptogram(self, value):
        self.__cryptogram = value

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
    def eci(self):
        """
        int
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

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
        dictionary = super(DecryptedPaymentData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'cardholderName', self.cardholder_name)
        self._add_to_dictionary(dictionary, 'cryptogram', self.cryptogram)
        self._add_to_dictionary(dictionary, 'dpan', self.dpan)
        self._add_to_dictionary(dictionary, 'eci', self.eci)
        self._add_to_dictionary(dictionary, 'expiryDate', self.expiry_date)
        return dictionary

    def from_dictionary(self, dictionary):
        super(DecryptedPaymentData, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'cryptogram' in dictionary:
            self.cryptogram = dictionary['cryptogram']
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
