#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase


class ContactDetails(ContactDetailsBase):
    """
    Class ContactDetails
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ContactDetails
    
    Attributes:
        fax_number:    str
        phone_number:  str
     """

    fax_number = None
    phone_number = None

    def to_dictionary(self):
        dictionary = super(ContactDetails, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'faxNumber', self.fax_number)
        self._add_to_dictionary(dictionary, 'phoneNumber', self.phone_number)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetails, self).from_dictionary(dictionary)
        if 'faxNumber' in dictionary:
            self.fax_number = dictionary['faxNumber']
        if 'phoneNumber' in dictionary:
            self.phone_number = dictionary['phoneNumber']
        return self
