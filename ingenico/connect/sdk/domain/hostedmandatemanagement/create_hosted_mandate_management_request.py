# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.hostedmandatemanagement.definitions.hosted_mandate_info import HostedMandateInfo
from ingenico.connect.sdk.domain.hostedmandatemanagement.definitions.hosted_mandate_management_specific_input import HostedMandateManagementSpecificInput


class CreateHostedMandateManagementRequest(DataObject):

    __create_mandate_info = None
    __hosted_mandate_management_specific_input = None

    @property
    def create_mandate_info(self):
        """
        | Object containing partial information needed for the creation of the mandate. The recurrencetype, signature type of the mandate and reference to the customer are mandatory. You can also supply any personal information you already know about the customer so they have to fill in less details.
        
        Type: :class:`ingenico.connect.sdk.domain.hostedmandatemanagement.definitions.hosted_mandate_info.HostedMandateInfo`
        """
        return self.__create_mandate_info

    @create_mandate_info.setter
    def create_mandate_info(self, value):
        self.__create_mandate_info = value

    @property
    def hosted_mandate_management_specific_input(self):
        """
        | Object containing hosted mandate management specific data
        
        Type: :class:`ingenico.connect.sdk.domain.hostedmandatemanagement.definitions.hosted_mandate_management_specific_input.HostedMandateManagementSpecificInput`
        """
        return self.__hosted_mandate_management_specific_input

    @hosted_mandate_management_specific_input.setter
    def hosted_mandate_management_specific_input(self, value):
        self.__hosted_mandate_management_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreateHostedMandateManagementRequest, self).to_dictionary()
        if self.create_mandate_info is not None:
            dictionary['createMandateInfo'] = self.create_mandate_info.to_dictionary()
        if self.hosted_mandate_management_specific_input is not None:
            dictionary['hostedMandateManagementSpecificInput'] = self.hosted_mandate_management_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedMandateManagementRequest, self).from_dictionary(dictionary)
        if 'createMandateInfo' in dictionary:
            if not isinstance(dictionary['createMandateInfo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['createMandateInfo']))
            value = HostedMandateInfo()
            self.create_mandate_info = value.from_dictionary(dictionary['createMandateInfo'])
        if 'hostedMandateManagementSpecificInput' in dictionary:
            if not isinstance(dictionary['hostedMandateManagementSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedMandateManagementSpecificInput']))
            value = HostedMandateManagementSpecificInput()
            self.hosted_mandate_management_specific_input = value.from_dictionary(dictionary['hostedMandateManagementSpecificInput'])
        return self
