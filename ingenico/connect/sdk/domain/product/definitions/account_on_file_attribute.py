#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair


class AccountOnFileAttribute(KeyValuePair):
    """
    Class AccountOnFileAttribute
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AccountOnFileAttribute
    """

    __must_write_reason = None
    __status = None

    @property
    def must_write_reason(self):
        """
        str
        """
        return self.__must_write_reason

    @must_write_reason.setter
    def must_write_reason(self, value):
        self.__must_write_reason = value

    @property
    def status(self):
        """
        str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

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
