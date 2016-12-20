#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PublicKey(DataObject):
    """
    Class PublicKey
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PublicKey
    """

    __key_id = None
    __public_key = None

    @property
    def key_id(self):
        """
        str
        """
        return self.__key_id

    @key_id.setter
    def key_id(self, value):
        self.__key_id = value

    @property
    def public_key(self):
        """
        str
        """
        return self.__public_key

    @public_key.setter
    def public_key(self, value):
        self.__public_key = value

    def to_dictionary(self):
        dictionary = super(PublicKey, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'keyId', self.key_id)
        self._add_to_dictionary(dictionary, 'publicKey', self.public_key)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PublicKey, self).from_dictionary(dictionary)
        if 'keyId' in dictionary:
            self.key_id = dictionary['keyId']
        if 'publicKey' in dictionary:
            self.public_key = dictionary['publicKey']
        return self
