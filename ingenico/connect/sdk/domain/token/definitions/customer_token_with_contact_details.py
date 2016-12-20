#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.token.definitions.contact_details_token import ContactDetailsToken
from ingenico.connect.sdk.domain.token.definitions.customer_token import CustomerToken


class CustomerTokenWithContactDetails(CustomerToken):
    """
    Class CustomerTokenWithContactDetails
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CustomerTokenWithContactDetails
    """

    __contact_details = None

    @property
    def contact_details(self):
        """
        :class:`ContactDetailsToken`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value):
        self.__contact_details = value

    def to_dictionary(self):
        dictionary = super(CustomerTokenWithContactDetails, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'contactDetails', self.contact_details)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerTokenWithContactDetails, self).from_dictionary(dictionary)
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = ContactDetailsToken()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        return self
