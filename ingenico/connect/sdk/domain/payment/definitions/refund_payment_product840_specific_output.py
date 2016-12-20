#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.refund_payment_product840_customer_account import RefundPaymentProduct840CustomerAccount


class RefundPaymentProduct840SpecificOutput(DataObject):
    """
    Class RefundPaymentProduct840SpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundPaymentProduct840SpecificOutput
    """

    __customer_account = None

    @property
    def customer_account(self):
        """
        :class:`RefundPaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value):
        self.__customer_account = value

    def to_dictionary(self):
        dictionary = super(RefundPaymentProduct840SpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customerAccount', self.customer_account)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundPaymentProduct840SpecificOutput, self).from_dictionary(dictionary)
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = RefundPaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        return self
