#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.token.definitions.mandate_sepa_direct_debit_without_creditor import MandateSepaDirectDebitWithoutCreditor


class MandateSepaDirectDebitWithMandateId(MandateSepaDirectDebitWithoutCreditor):
    """
    Class MandateSepaDirectDebitWithMandateId
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MandateSepaDirectDebitWithMandateId
    
    Attributes:
        mandate_id:  str
     """

    mandate_id = None

    def to_dictionary(self):
        dictionary = super(MandateSepaDirectDebitWithMandateId, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'mandateId', self.mandate_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateSepaDirectDebitWithMandateId, self).from_dictionary(dictionary)
        if 'mandateId' in dictionary:
            self.mandate_id = dictionary['mandateId']
        return self
