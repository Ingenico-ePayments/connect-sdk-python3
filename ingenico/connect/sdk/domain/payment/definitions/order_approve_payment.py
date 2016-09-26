#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.additional_order_input_airline_data import AdditionalOrderInputAirlineData
from ingenico.connect.sdk.domain.payment.definitions.order_references_approve_payment import OrderReferencesApprovePayment


class OrderApprovePayment(DataObject):
    """
    Class OrderApprovePayment
    See also https://developer.globalcollect.com/documentation/api/server/#schema_OrderApprovePayment
    
    Attributes:
        additional_input:  :class:`AdditionalOrderInputAirlineData`
        references:        :class:`OrderReferencesApprovePayment`
     """

    additional_input = None
    references = None

    def to_dictionary(self):
        dictionary = super(OrderApprovePayment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalInput', self.additional_input)
        self._add_to_dictionary(dictionary, 'references', self.references)
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderApprovePayment, self).from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInputAirlineData()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = OrderReferencesApprovePayment()
            self.references = value.from_dictionary(dictionary['references'])
        return self
