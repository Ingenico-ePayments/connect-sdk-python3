#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class MandateApproval(DataObject):
    """
    Class MandateApproval
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MandateApproval
    
    Attributes:
        mandate_signature_date:   str
        mandate_signature_place:  str
        mandate_signed:           bool
     """

    mandate_signature_date = None
    mandate_signature_place = None
    mandate_signed = None

    def to_dictionary(self):
        dictionary = super(MandateApproval, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'mandateSignatureDate', self.mandate_signature_date)
        self._add_to_dictionary(dictionary, 'mandateSignaturePlace', self.mandate_signature_place)
        self._add_to_dictionary(dictionary, 'mandateSigned', self.mandate_signed)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateApproval, self).from_dictionary(dictionary)
        if 'mandateSignatureDate' in dictionary:
            self.mandate_signature_date = dictionary['mandateSignatureDate']
        if 'mandateSignaturePlace' in dictionary:
            self.mandate_signature_place = dictionary['mandateSignaturePlace']
        if 'mandateSigned' in dictionary:
            self.mandate_signed = dictionary['mandateSigned']
        return self
