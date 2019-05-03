# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair


class GetCustomerDetailsRequest(DataObject):
    """
    | Input for the retrieval of a customer's details.
    """

    __country_code = None
    __values = None

    @property
    def country_code(self):
        """
        | The code of the country where the customer should reside.
        
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def values(self):
        """
        | A list of keys with a value used to retrieve the details of a customer. Depending on the country code, different keys are required. These can be determined with a getPaymentProduct call and using payment product properties with the property usedForLookup set to true.
        
        Type: list[:class:`ingenico.connect.sdk.domain.definitions.key_value_pair.KeyValuePair`]
        """
        return self.__values

    @values.setter
    def values(self, value):
        self.__values = value

    def to_dictionary(self):
        dictionary = super(GetCustomerDetailsRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        self._add_to_dictionary(dictionary, 'values', self.values)
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetCustomerDetailsRequest, self).from_dictionary(dictionary)
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'values' in dictionary:
            if not isinstance(dictionary['values'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['values']))
            self.values = []
            for values_element in dictionary['values']:
                values_value = KeyValuePair()
                self.values.append(values_value.from_dictionary(values_element))
        return self
