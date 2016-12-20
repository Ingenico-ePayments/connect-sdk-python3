#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.refund_method_specific_output import RefundMethodSpecificOutput


class RefundMobileMethodSpecificOutput(RefundMethodSpecificOutput):
    """
    Class RefundMobileMethodSpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundMobileMethodSpecificOutput
    """

    __network = None

    @property
    def network(self):
        """
        str
        """
        return self.__network

    @network.setter
    def network(self, value):
        self.__network = value

    def to_dictionary(self):
        dictionary = super(RefundMobileMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'network', self.network)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundMobileMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'network' in dictionary:
            self.network = dictionary['network']
        return self
