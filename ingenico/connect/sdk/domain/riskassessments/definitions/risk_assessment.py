#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.fraud_fields import FraudFields
from ingenico.connect.sdk.domain.riskassessments.definitions.order_risk_assessment import OrderRiskAssessment


class RiskAssessment(DataObject):
    """
    Class RiskAssessment
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RiskAssessment
    
    Attributes:
        fraud_fields:        :class:`FraudFields`
        order:               :class:`OrderRiskAssessment`
        payment_product_id:  int
     """

    fraud_fields = None
    order = None
    payment_product_id = None

    def to_dictionary(self):
        dictionary = super(RiskAssessment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'fraudFields', self.fraud_fields)
        self._add_to_dictionary(dictionary, 'order', self.order)
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RiskAssessment, self).from_dictionary(dictionary)
        if 'fraudFields' in dictionary:
            if not isinstance(dictionary['fraudFields'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudFields']))
            value = FraudFields()
            self.fraud_fields = value.from_dictionary(dictionary['fraudFields'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = OrderRiskAssessment()
            self.order = value.from_dictionary(dictionary['order'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
