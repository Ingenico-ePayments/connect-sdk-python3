#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase


class ContactDetailsToken(ContactDetailsBase):
    """
    Class ContactDetailsToken
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ContactDetailsToken
    """

    def to_dictionary(self):
        dictionary = super(ContactDetailsToken, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetailsToken, self).from_dictionary(dictionary)
        return self
