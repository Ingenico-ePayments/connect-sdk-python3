#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentCreationReferences(DataObject):
    """
    Class PaymentCreationReferences
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentCreationReferences
    """

    __additional_reference = None
    __external_reference = None

    @property
    def additional_reference(self):
        """
        str
        """
        return self.__additional_reference

    @additional_reference.setter
    def additional_reference(self, value):
        self.__additional_reference = value

    @property
    def external_reference(self):
        """
        str
        """
        return self.__external_reference

    @external_reference.setter
    def external_reference(self, value):
        self.__external_reference = value

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
