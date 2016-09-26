#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal


class RefundCustomer(DataObject):
    """
    Class RefundCustomer
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundCustomer
    
    Attributes:
        address:              :class:`AddressPersonal`
        company_information:  :class:`CompanyInformation`
        contact_details:      :class:`ContactDetailsBase`
     """

    address = None
    company_information = None
    contact_details = None

    def to_dictionary(self):
        dictionary = super(RefundCustomer, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'address', self.address)
        self._add_to_dictionary(dictionary, 'companyInformation', self.company_information)
        self._add_to_dictionary(dictionary, 'contactDetails', self.contact_details)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundCustomer, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = AddressPersonal()
            self.address = value.from_dictionary(dictionary['address'])
        if 'companyInformation' in dictionary:
            if not isinstance(dictionary['companyInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['companyInformation']))
            value = CompanyInformation()
            self.company_information = value.from_dictionary(dictionary['companyInformation'])
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = ContactDetailsBase()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        return self
