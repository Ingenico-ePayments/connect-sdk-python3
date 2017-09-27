# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal
from ingenico.connect.sdk.domain.riskassessments.definitions.contact_details_risk_assessment import ContactDetailsRiskAssessment
from ingenico.connect.sdk.domain.riskassessments.definitions.personal_information_risk_assessment import PersonalInformationRiskAssessment


class CustomerRiskAssessment(DataObject):

    __billing_address = None
    __contact_details = None
    __locale = None
    __personal_information = None
    __shipping_address = None

    @property
    def billing_address(self):
        """
        | Object containing billing address details
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value

    @property
    def contact_details(self):
        """
        | Object containing contact details like email address
        
        Type: :class:`ingenico.connect.sdk.domain.riskassessments.definitions.contact_details_risk_assessment.ContactDetailsRiskAssessment`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value):
        self.__contact_details = value

    @property
    def locale(self):
        """
        | The locale that the consumer should be addressed in (for 3rd parties). Note that some 3rd party providers only support the languageCode part of the locale, in those cases we will only use part of the locale provided.
        
        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def personal_information(self):
        """
        | Object containing personal information like name, date of birth and gender
        
        Type: :class:`ingenico.connect.sdk.domain.riskassessments.definitions.personal_information_risk_assessment.PersonalInformationRiskAssessment`
        """
        return self.__personal_information

    @personal_information.setter
    def personal_information(self, value):
        self.__personal_information = value

    @property
    def shipping_address(self):
        """
        | Object containing shipping address details
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.address_personal.AddressPersonal`
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value

    def to_dictionary(self):
        dictionary = super(CustomerRiskAssessment, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'billingAddress', self.billing_address)
        self._add_to_dictionary(dictionary, 'contactDetails', self.contact_details)
        self._add_to_dictionary(dictionary, 'locale', self.locale)
        self._add_to_dictionary(dictionary, 'personalInformation', self.personal_information)
        self._add_to_dictionary(dictionary, 'shippingAddress', self.shipping_address)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerRiskAssessment, self).from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = ContactDetailsRiskAssessment()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = PersonalInformationRiskAssessment()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        if 'shippingAddress' in dictionary:
            if not isinstance(dictionary['shippingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shippingAddress']))
            value = AddressPersonal()
            self.shipping_address = value.from_dictionary(dictionary['shippingAddress'])
        return self
