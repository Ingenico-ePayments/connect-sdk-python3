#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.hostedcheckout.definitions.payment_product_filters_hosted_checkout import PaymentProductFiltersHostedCheckout


class HostedCheckoutSpecificInput(DataObject):
    """
    Class HostedCheckoutSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_HostedCheckoutSpecificInput
    """

    __is_recurring = None
    __locale = None
    __payment_product_filters = None
    __return_url = None
    __show_result_page = None
    __tokens = None
    __variant = None

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
    def locale(self):
        """
        str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def payment_product_filters(self):
        """
        :class:`PaymentProductFiltersHostedCheckout`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value):
        self.__payment_product_filters = value

    @property
    def return_url(self):
        """
        str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    @property
    def show_result_page(self):
        """
        bool
        """
        return self.__show_result_page

    @show_result_page.setter
    def show_result_page(self, value):
        self.__show_result_page = value

    @property
    def tokens(self):
        """
        str
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value):
        self.__tokens = value

    @property
    def variant(self):
        """
        str
        """
        return self.__variant

    @variant.setter
    def variant(self, value):
        self.__variant = value

    def to_dictionary(self):
        dictionary = super(HostedCheckoutSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        self._add_to_dictionary(dictionary, 'locale', self.locale)
        self._add_to_dictionary(dictionary, 'paymentProductFilters', self.payment_product_filters)
        self._add_to_dictionary(dictionary, 'returnUrl', self.return_url)
        self._add_to_dictionary(dictionary, 'showResultPage', self.show_result_page)
        self._add_to_dictionary(dictionary, 'tokens', self.tokens)
        self._add_to_dictionary(dictionary, 'variant', self.variant)
        return dictionary

    def from_dictionary(self, dictionary):
        super(HostedCheckoutSpecificInput, self).from_dictionary(dictionary)
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersHostedCheckout()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'showResultPage' in dictionary:
            self.show_result_page = dictionary['showResultPage']
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self
