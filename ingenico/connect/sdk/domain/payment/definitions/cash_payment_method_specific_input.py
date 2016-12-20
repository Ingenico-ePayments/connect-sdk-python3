#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_method_specific_input_base import CashPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1503_specific_input import CashPaymentProduct1503SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.cash_payment_product1504_specific_input import CashPaymentProduct1504SpecificInput


class CashPaymentMethodSpecificInput(CashPaymentMethodSpecificInputBase):
    """
    Class CashPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CashPaymentMethodSpecificInput
    """

    __payment_product1503_specific_input = None
    __payment_product1504_specific_input = None

    @property
    def payment_product1503_specific_input(self):
        """
        :class:`CashPaymentProduct1503SpecificInput`
        """
        return self.__payment_product1503_specific_input

    @payment_product1503_specific_input.setter
    def payment_product1503_specific_input(self, value):
        self.__payment_product1503_specific_input = value

    @property
    def payment_product1504_specific_input(self):
        """
        :class:`CashPaymentProduct1504SpecificInput`
        """
        return self.__payment_product1504_specific_input

    @payment_product1504_specific_input.setter
    def payment_product1504_specific_input(self, value):
        self.__payment_product1504_specific_input = value

    def to_dictionary(self):
        dictionary = super(CashPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProduct1503SpecificInput', self.payment_product1503_specific_input)
        self._add_to_dictionary(dictionary, 'paymentProduct1504SpecificInput', self.payment_product1504_specific_input)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CashPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'paymentProduct1503SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1503SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1503SpecificInput']))
            value = CashPaymentProduct1503SpecificInput()
            self.payment_product1503_specific_input = value.from_dictionary(dictionary['paymentProduct1503SpecificInput'])
        if 'paymentProduct1504SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct1504SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct1504SpecificInput']))
            value = CashPaymentProduct1504SpecificInput()
            self.payment_product1504_specific_input = value.from_dictionary(dictionary['paymentProduct1504SpecificInput'])
        return self
