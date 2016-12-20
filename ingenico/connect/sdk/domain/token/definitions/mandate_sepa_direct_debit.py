#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.token.definitions.creditor import Creditor
from ingenico.connect.sdk.domain.token.definitions.mandate_sepa_direct_debit_with_mandate_id import MandateSepaDirectDebitWithMandateId


class MandateSepaDirectDebit(MandateSepaDirectDebitWithMandateId):
    """
    Class MandateSepaDirectDebit
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MandateSepaDirectDebit
    """

    __creditor = None

    @property
    def creditor(self):
        """
        :class:`Creditor`
        """
        return self.__creditor

    @creditor.setter
    def creditor(self, value):
        self.__creditor = value

    def to_dictionary(self):
        dictionary = super(MandateSepaDirectDebit, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'creditor', self.creditor)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateSepaDirectDebit, self).from_dictionary(dictionary)
        if 'creditor' in dictionary:
            if not isinstance(dictionary['creditor'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['creditor']))
            value = Creditor()
            self.creditor = value.from_dictionary(dictionary['creditor'])
        return self
