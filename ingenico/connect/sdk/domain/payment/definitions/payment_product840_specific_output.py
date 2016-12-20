#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.payment.definitions.payment_product840_customer_account import PaymentProduct840CustomerAccount


class PaymentProduct840SpecificOutput(DataObject):
    """
    Class PaymentProduct840SpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProduct840SpecificOutput
    """

    __customer_account = None
    __customer_address = None

    @property
    def customer_account(self):
        """
        :class:`PaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value):
        self.__customer_account = value

    @property
    def customer_address(self):
        """
        :class:`Address`
        """
        return self.__customer_address

    @customer_address.setter
    def customer_address(self, value):
        self.__customer_address = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct840SpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customerAccount', self.customer_account)
        self._add_to_dictionary(dictionary, 'customerAddress', self.customer_address)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct840SpecificOutput, self).from_dictionary(dictionary)
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = PaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        if 'customerAddress' in dictionary:
            if not isinstance(dictionary['customerAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAddress']))
            value = Address()
            self.customer_address = value.from_dictionary(dictionary['customerAddress'])
        return self
