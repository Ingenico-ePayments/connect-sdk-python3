# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.payment.definitions.personal_name import PersonalName


class AddressPersonal(Address):

    __name = None

    @property
    def name(self):
        """
        | Object that holds the name elements
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.personal_name.PersonalName`
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(AddressPersonal, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(AddressPersonal, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        return self
