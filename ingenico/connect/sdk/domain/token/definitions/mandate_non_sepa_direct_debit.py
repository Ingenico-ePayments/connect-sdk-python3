#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit_payment_product705_specific_data import TokenNonSepaDirectDebitPaymentProduct705SpecificData


class MandateNonSepaDirectDebit(DataObject):
    """
    Class MandateNonSepaDirectDebit
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MandateNonSepaDirectDebit
    """

    __payment_product705_specific_data = None

    @property
    def payment_product705_specific_data(self):
        """
        :class:`TokenNonSepaDirectDebitPaymentProduct705SpecificData`
        """
        return self.__payment_product705_specific_data

    @payment_product705_specific_data.setter
    def payment_product705_specific_data(self, value):
        self.__payment_product705_specific_data = value

    def to_dictionary(self):
        dictionary = super(MandateNonSepaDirectDebit, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProduct705SpecificData', self.payment_product705_specific_data)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateNonSepaDirectDebit, self).from_dictionary(dictionary)
        if 'paymentProduct705SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct705SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct705SpecificData']))
            value = TokenNonSepaDirectDebitPaymentProduct705SpecificData()
            self.payment_product705_specific_data = value.from_dictionary(dictionary['paymentProduct705SpecificData'])
        return self
