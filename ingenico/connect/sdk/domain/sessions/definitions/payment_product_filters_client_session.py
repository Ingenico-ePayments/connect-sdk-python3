#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.payment_product_filter import PaymentProductFilter


class PaymentProductFiltersClientSession(DataObject):
    """
    Class PaymentProductFiltersClientSession
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductFiltersClientSession
    
    Attributes:
        exclude:      :class:`PaymentProductFilter`
        restrict_to:  :class:`PaymentProductFilter`
     """

    exclude = None
    restrict_to = None

    def to_dictionary(self):
        dictionary = super(PaymentProductFiltersClientSession, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'exclude', self.exclude)
        self._add_to_dictionary(dictionary, 'restrictTo', self.restrict_to)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFiltersClientSession, self).from_dictionary(dictionary)
        if 'exclude' in dictionary:
            if not isinstance(dictionary['exclude'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['exclude']))
            value = PaymentProductFilter()
            self.exclude = value.from_dictionary(dictionary['exclude'])
        if 'restrictTo' in dictionary:
            if not isinstance(dictionary['restrictTo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['restrictTo']))
            value = PaymentProductFilter()
            self.restrict_to = value.from_dictionary(dictionary['restrictTo'])
        return self
