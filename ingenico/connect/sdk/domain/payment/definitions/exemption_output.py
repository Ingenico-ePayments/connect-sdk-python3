# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject


class ExemptionOutput(DataObject):
    """
    | Object containing exemption output
    """

    __exemption_raised = None
    __exemption_rejection_reason = None
    __exemption_request = None

    @property
    def exemption_raised(self):
        """
        | Type of strong customer authentication (SCA) exemption that was raised towards the acquirer for this transaction.
        
        Type: str
        """
        return self.__exemption_raised

    @exemption_raised.setter
    def exemption_raised(self, value):
        self.__exemption_raised = value

    @property
    def exemption_rejection_reason(self):
        """
        | The request exemption could not be granted. The reason why is returned in this property.
        
        Type: str
        """
        return self.__exemption_rejection_reason

    @exemption_rejection_reason.setter
    def exemption_rejection_reason(self, value):
        self.__exemption_rejection_reason = value

    @property
    def exemption_request(self):
        """
        | Type of strong customer authentication (SCA) exemption requested by you for this transaction.
        
        Type: str
        """
        return self.__exemption_request

    @exemption_request.setter
    def exemption_request(self, value):
        self.__exemption_request = value

    def to_dictionary(self):
        dictionary = super(ExemptionOutput, self).to_dictionary()
        if self.exemption_raised is not None:
            dictionary['exemptionRaised'] = self.exemption_raised
        if self.exemption_rejection_reason is not None:
            dictionary['exemptionRejectionReason'] = self.exemption_rejection_reason
        if self.exemption_request is not None:
            dictionary['exemptionRequest'] = self.exemption_request
        return dictionary

    def from_dictionary(self, dictionary):
        super(ExemptionOutput, self).from_dictionary(dictionary)
        if 'exemptionRaised' in dictionary:
            self.exemption_raised = dictionary['exemptionRaised']
        if 'exemptionRejectionReason' in dictionary:
            self.exemption_rejection_reason = dictionary['exemptionRejectionReason']
        if 'exemptionRequest' in dictionary:
            self.exemption_request = dictionary['exemptionRequest']
        return self
