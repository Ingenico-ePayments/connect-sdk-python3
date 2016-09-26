#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair


class AccountOnFileAttribute(KeyValuePair):
    """
    Class AccountOnFileAttribute
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AccountOnFileAttribute
    
    Attributes:
        must_write_reason:  str
        status:             str
     """

    must_write_reason = None
    status = None

    def to_dictionary(self):
        dictionary = super(AccountOnFileAttribute, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'mustWriteReason', self.must_write_reason)
        self._add_to_dictionary(dictionary, 'status', self.status)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFileAttribute, self).from_dictionary(dictionary)
        if 'mustWriteReason' in dictionary:
            self.must_write_reason = dictionary['mustWriteReason']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
