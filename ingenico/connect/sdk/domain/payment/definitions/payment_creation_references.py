#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentCreationReferences(DataObject):
    """
    Class PaymentCreationReferences
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentCreationReferences
    
    Attributes:
        additional_reference:  str
        external_reference:    str
     """

    additional_reference = None
    external_reference = None

    def to_dictionary(self):
        dictionary = super(PaymentCreationReferences, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalReference', self.additional_reference)
        self._add_to_dictionary(dictionary, 'externalReference', self.external_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentCreationReferences, self).from_dictionary(dictionary)
        if 'additionalReference' in dictionary:
            self.additional_reference = dictionary['additionalReference']
        if 'externalReference' in dictionary:
            self.external_reference = dictionary['externalReference']
        return self
