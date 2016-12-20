#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.sessions.definitions.payment_product_filters_client_session import PaymentProductFiltersClientSession


class SessionRequest(DataObject):
    """
    Class SessionRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_SessionRequest
    """

    __payment_product_filters = None
    __tokens = None

    @property
    def payment_product_filters(self):
        """
        :class:`PaymentProductFiltersClientSession`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value):
        self.__payment_product_filters = value

    @property
    def tokens(self):
        """
        list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value):
        self.__tokens = value

    def to_dictionary(self):
        dictionary = super(SessionRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProductFilters', self.payment_product_filters)
        self._add_to_dictionary(dictionary, 'tokens', self.tokens)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SessionRequest, self).from_dictionary(dictionary)
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersClientSession()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for tokens_element in dictionary['tokens']:
                self.tokens.append(tokens_element)
        return self
