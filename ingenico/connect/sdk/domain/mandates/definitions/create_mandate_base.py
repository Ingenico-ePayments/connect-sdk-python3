# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.mandates.definitions.mandate_customer import MandateCustomer


class CreateMandateBase(DataObject):

    __customer = None
    __customer_reference = None
    __language = None
    __recurrence_type = None
    __return_url = None
    __signature_type = None

    @property
    def customer(self):
        """
        | Customer object containing customer specific inputs
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.mandate_customer.MandateCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def customer_reference(self):
        """
        | The unique identifier of a customer
        
        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value):
        self.__customer_reference = value

    @property
    def language(self):
        """
        | The language of the customer.
        
        Type: str
        """
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    @property
    def recurrence_type(self):
        """
        | Specifies whether the mandate is for one-off or recurring payments.
        
        Type: str
        """
        return self.__recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, value):
        self.__recurrence_type = value

    @property
    def return_url(self):
        """
        | Return url to use if the mandate signing requires redirection.
        
        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    @property
    def signature_type(self):
        """
        | Specifies whether the mandate is 'Unsigned' or singed by 'SMS'.
        
        Type: str
        """
        return self.__signature_type

    @signature_type.setter
    def signature_type(self, value):
        self.__signature_type = value

    def to_dictionary(self):
        dictionary = super(CreateMandateBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'customerReference', self.customer_reference)
        self._add_to_dictionary(dictionary, 'language', self.language)
        self._add_to_dictionary(dictionary, 'recurrenceType', self.recurrence_type)
        self._add_to_dictionary(dictionary, 'returnUrl', self.return_url)
        self._add_to_dictionary(dictionary, 'signatureType', self.signature_type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateMandateBase, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = MandateCustomer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'language' in dictionary:
            self.language = dictionary['language']
        if 'recurrenceType' in dictionary:
            self.recurrence_type = dictionary['recurrenceType']
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'signatureType' in dictionary:
            self.signature_type = dictionary['signatureType']
        return self
