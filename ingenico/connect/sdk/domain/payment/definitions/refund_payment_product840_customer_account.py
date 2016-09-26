#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RefundPaymentProduct840CustomerAccount(DataObject):
    """
    Class RefundPaymentProduct840CustomerAccount
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundPaymentProduct840CustomerAccount
    
    Attributes:
        customer_account_status:  str
        customer_address_status:  str
        payer_id:                 str
     """

    customer_account_status = None
    customer_address_status = None
    payer_id = None

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
