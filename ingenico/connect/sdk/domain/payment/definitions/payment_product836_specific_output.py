#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct836SpecificOutput(DataObject):
    """
    Class PaymentProduct836SpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProduct836SpecificOutput
    """

    __security_indicator = None

    @property
    def security_indicator(self):
        """
        str
        """
        return self.__security_indicator

    @security_indicator.setter
    def security_indicator(self, value):
        self.__security_indicator = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct836SpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'securityIndicator', self.security_indicator)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct836SpecificOutput, self).from_dictionary(dictionary)
        if 'securityIndicator' in dictionary:
            self.security_indicator = dictionary['securityIndicator']
        return self
