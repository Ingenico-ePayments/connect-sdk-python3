#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.services.definitions.payment_context import PaymentContext


class GetIINDetailsRequest(DataObject):
    """
    Class GetIINDetailsRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_GetIINDetailsRequest
    """

    __bin = None
    __payment_context = None

    @property
    def bin(self):
        """
        str
        """
        return self.__bin

    @bin.setter
    def bin(self, value):
        self.__bin = value

    @property
    def payment_context(self):
        """
        :class:`PaymentContext`
        """
        return self.__payment_context

    @payment_context.setter
    def payment_context(self, value):
        self.__payment_context = value

    def to_dictionary(self):
        dictionary = super(GetIINDetailsRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bin', self.bin)
        self._add_to_dictionary(dictionary, 'paymentContext', self.payment_context)
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetIINDetailsRequest, self).from_dictionary(dictionary)
        if 'bin' in dictionary:
            self.bin = dictionary['bin']
        if 'paymentContext' in dictionary:
            if not isinstance(dictionary['paymentContext'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentContext']))
            value = PaymentContext()
            self.payment_context = value.from_dictionary(dictionary['paymentContext'])
        return self
