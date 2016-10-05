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
    
    Attributes:
        is_recurring:             bool
        locale:                   str
        payment_product_filters:  :class:`PaymentProductFiltersHostedCheckout`
        return_url:               str
        show_result_page:         bool
        tokens:                   str
        variant:                  str
     """

    is_recurring = None
    locale = None
    payment_product_filters = None
    return_url = None
    show_result_page = None
    tokens = None
    variant = None

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
