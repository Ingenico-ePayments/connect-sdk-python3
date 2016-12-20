#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase
from ingenico.connect.sdk.domain.payment.definitions.personal_name import PersonalName


class PayoutCustomer(DataObject):
    """
    Class PayoutCustomer
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PayoutCustomer
    """

    __address = None
    __company_information = None
    __contact_details = None
    __merchant_customer_id = None
    __name = None

    @property
    def address(self):
        """
        :class:`Address`
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def company_information(self):
        """
        :class:`CompanyInformation`
        """
        return self.__company_information

    @company_information.setter
    def company_information(self, value):
        self.__company_information = value

    @property
    def contact_details(self):
        """
        :class:`ContactDetailsBase`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value):
        self.__contact_details = value

    @property
    def merchant_customer_id(self):
        """
        str
        """
        return self.__merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, value):
        self.__merchant_customer_id = value

    @property
    def name(self):
        """
        :class:`PersonalName`
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(PayoutCustomer, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'address', self.address)
        self._add_to_dictionary(dictionary, 'companyInformation', self.company_information)
        self._add_to_dictionary(dictionary, 'contactDetails', self.contact_details)
        self._add_to_dictionary(dictionary, 'merchantCustomerId', self.merchant_customer_id)
        self._add_to_dictionary(dictionary, 'name', self.name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutCustomer, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = Address()
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
        if 'merchantCustomerId' in dictionary:
            self.merchant_customer_id = dictionary['merchantCustomerId']
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        return self
