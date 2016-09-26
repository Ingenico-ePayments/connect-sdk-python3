#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct836SpecificOutput(DataObject):
    """
    Class PaymentProduct836SpecificOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProduct836SpecificOutput
    
    Attributes:
        security_indicator:  str
     """

    security_indicator = None

    def to_dictionary(self):
        dictionary = super(PaymentProduct836SpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'securityIndicator', self.security_indicator)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct836SpecificOutput, self).from_dictionary(dictionary)
        if 'securityIndicator' in dictionary:
            self.security_indicator = dictionary['securityIndicator']
        return self
