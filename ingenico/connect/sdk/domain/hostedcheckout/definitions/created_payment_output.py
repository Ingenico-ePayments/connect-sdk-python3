#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.hostedcheckout.definitions.displayed_data import DisplayedData
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment
from ingenico.connect.sdk.domain.payment.definitions.payment_creation_references import PaymentCreationReferences


class CreatedPaymentOutput(DataObject):
    """
    Class CreatedPaymentOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreatedPaymentOutput
    
    Attributes:
        displayed_data:               :class:`DisplayedData`
        payment:                      :class:`Payment`
        payment_creation_references:  :class:`PaymentCreationReferences`
        payment_status_category:      str
        tokens:                       str
     """

    displayed_data = None
    payment = None
    payment_creation_references = None
    payment_status_category = None
    tokens = None

    def to_dictionary(self):
        dictionary = super(CreatedPaymentOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'displayedData', self.displayed_data)
        self._add_to_dictionary(dictionary, 'payment', self.payment)
        self._add_to_dictionary(dictionary, 'paymentCreationReferences', self.payment_creation_references)
        self._add_to_dictionary(dictionary, 'paymentStatusCategory', self.payment_status_category)
        self._add_to_dictionary(dictionary, 'tokens', self.tokens)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatedPaymentOutput, self).from_dictionary(dictionary)
        if 'displayedData' in dictionary:
            if not isinstance(dictionary['displayedData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayedData']))
            value = DisplayedData()
            self.displayed_data = value.from_dictionary(dictionary['displayedData'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentCreationReferences' in dictionary:
            if not isinstance(dictionary['paymentCreationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentCreationReferences']))
            value = PaymentCreationReferences()
            self.payment_creation_references = value.from_dictionary(dictionary['paymentCreationReferences'])
        if 'paymentStatusCategory' in dictionary:
            self.payment_status_category = dictionary['paymentStatusCategory']
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        return self
