#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ContactDetailsBase(DataObject):
    """
    Class ContactDetailsBase
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ContactDetailsBase
    """

    __email_address = None
    __email_message_type = None

    @property
    def email_address(self):
        """
        str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def email_message_type(self):
        """
        str
        """
        return self.__email_message_type

    @email_message_type.setter
    def email_message_type(self, value):
        self.__email_message_type = value

    def to_dictionary(self):
        dictionary = super(ContactDetailsBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'emailAddress', self.email_address)
        self._add_to_dictionary(dictionary, 'emailMessageType', self.email_message_type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetailsBase, self).from_dictionary(dictionary)
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'emailMessageType' in dictionary:
            self.email_message_type = dictionary['emailMessageType']
        return self
