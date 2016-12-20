#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input_base import RedirectPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product809_specific_input import RedirectPaymentProduct809SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product816_specific_input import RedirectPaymentProduct816SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product882_specific_input import RedirectPaymentProduct882SpecificInput


class RedirectPaymentMethodSpecificInput(RedirectPaymentMethodSpecificInputBase):
    """
    Class RedirectPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RedirectPaymentMethodSpecificInput
    """

    __is_recurring = None
    __payment_product809_specific_input = None
    __payment_product816_specific_input = None
    __payment_product882_specific_input = None
    __return_url = None

    @property
    def is_recurring(self):
        """
        bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def payment_product809_specific_input(self):
        """
        :class:`RedirectPaymentProduct809SpecificInput`
        """
        return self.__payment_product809_specific_input

    @payment_product809_specific_input.setter
    def payment_product809_specific_input(self, value):
        self.__payment_product809_specific_input = value

    @property
    def payment_product816_specific_input(self):
        """
        :class:`RedirectPaymentProduct816SpecificInput`
        """
        return self.__payment_product816_specific_input

    @payment_product816_specific_input.setter
    def payment_product816_specific_input(self, value):
        self.__payment_product816_specific_input = value

    @property
    def payment_product882_specific_input(self):
        """
        :class:`RedirectPaymentProduct882SpecificInput`
        """
        return self.__payment_product882_specific_input

    @payment_product882_specific_input.setter
    def payment_product882_specific_input(self, value):
        self.__payment_product882_specific_input = value

    @property
    def return_url(self):
        """
        str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        self._add_to_dictionary(dictionary, 'paymentProduct809SpecificInput', self.payment_product809_specific_input)
        self._add_to_dictionary(dictionary, 'paymentProduct816SpecificInput', self.payment_product816_specific_input)
        self._add_to_dictionary(dictionary, 'paymentProduct882SpecificInput', self.payment_product882_specific_input)
        self._add_to_dictionary(dictionary, 'returnUrl', self.return_url)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'paymentProduct809SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct809SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct809SpecificInput']))
            value = RedirectPaymentProduct809SpecificInput()
            self.payment_product809_specific_input = value.from_dictionary(dictionary['paymentProduct809SpecificInput'])
        if 'paymentProduct816SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct816SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct816SpecificInput']))
            value = RedirectPaymentProduct816SpecificInput()
            self.payment_product816_specific_input = value.from_dictionary(dictionary['paymentProduct816SpecificInput'])
        if 'paymentProduct882SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct882SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct882SpecificInput']))
            value = RedirectPaymentProduct882SpecificInput()
            self.payment_product882_specific_input = value.from_dictionary(dictionary['paymentProduct882SpecificInput'])
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        return self
