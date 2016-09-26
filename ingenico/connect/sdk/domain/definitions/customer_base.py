#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation


class CustomerBase(DataObject):
    """
    Class CustomerBase
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CustomerBase
    
    Attributes:
        company_information:   :class:`CompanyInformation`
        merchant_customer_id:  str
        vat_number:            str
     """

    company_information = None
    merchant_customer_id = None
    vat_number = None

    def to_dictionary(self):
        dictionary = super(CustomerBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'companyInformation', self.company_information)
        self._add_to_dictionary(dictionary, 'merchantCustomerId', self.merchant_customer_id)
        self._add_to_dictionary(dictionary, 'vatNumber', self.vat_number)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerBase, self).from_dictionary(dictionary)
        if 'companyInformation' in dictionary:
            if not isinstance(dictionary['companyInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['companyInformation']))
            value = CompanyInformation()
            self.company_information = value.from_dictionary(dictionary['companyInformation'])
        if 'merchantCustomerId' in dictionary:
            self.merchant_customer_id = dictionary['merchantCustomerId']
        if 'vatNumber' in dictionary:
            self.vat_number = dictionary['vatNumber']
        return self
