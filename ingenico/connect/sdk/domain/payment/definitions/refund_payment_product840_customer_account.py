#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RefundPaymentProduct840CustomerAccount(DataObject):
    """
    Class RefundPaymentProduct840CustomerAccount
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundPaymentProduct840CustomerAccount
    """

    __customer_account_status = None
    __customer_address_status = None
    __payer_id = None

    @property
    def customer_account_status(self):
        """
        str
        """
        return self.__customer_account_status

    @customer_account_status.setter
    def customer_account_status(self, value):
        self.__customer_account_status = value

    @property
    def customer_address_status(self):
        """
        str
        """
        return self.__customer_address_status

    @customer_address_status.setter
    def customer_address_status(self, value):
        self.__customer_address_status = value

    @property
    def payer_id(self):
        """
        str
        """
        return self.__payer_id

    @payer_id.setter
    def payer_id(self, value):
        self.__payer_id = value

    def to_dictionary(self):
        dictionary = super(RefundPaymentProduct840CustomerAccount, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customerAccountStatus', self.customer_account_status)
        self._add_to_dictionary(dictionary, 'customerAddressStatus', self.customer_address_status)
        self._add_to_dictionary(dictionary, 'payerId', self.payer_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundPaymentProduct840CustomerAccount, self).from_dictionary(dictionary)
        if 'customerAccountStatus' in dictionary:
            self.customer_account_status = dictionary['customerAccountStatus']
        if 'customerAddressStatus' in dictionary:
            self.customer_address_status = dictionary['customerAddressStatus']
        if 'payerId' in dictionary:
            self.payer_id = dictionary['payerId']
        return self
