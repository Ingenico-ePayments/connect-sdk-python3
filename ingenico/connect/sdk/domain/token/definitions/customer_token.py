#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.customer_base import CustomerBase
from ingenico.connect.sdk.domain.token.definitions.personal_information_token import PersonalInformationToken


class CustomerToken(CustomerBase):
    """
    Class CustomerToken
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CustomerToken
    
    Attributes:
        billing_address:       :class:`Address`
        personal_information:  :class:`PersonalInformationToken`
     """

    billing_address = None
    personal_information = None

    def to_dictionary(self):
        dictionary = super(CustomerToken, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'billingAddress', self.billing_address)
        self._add_to_dictionary(dictionary, 'personalInformation', self.personal_information)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerToken, self).from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = PersonalInformationToken()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        return self
