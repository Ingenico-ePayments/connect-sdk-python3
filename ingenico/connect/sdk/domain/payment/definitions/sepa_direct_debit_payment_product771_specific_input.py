# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.mandates.definitions.create_mandate_base import CreateMandateBase


class SepaDirectDebitPaymentProduct771SpecificInput(DataObject):
    """
    | Object containing information specific to SEPA Direct Debit with Slimpay
    """

    __mandate = None
    __mandate_reference = None

    @property
    def mandate(self):
        """
        | Object containing informatin to create a Slimpay mandate. Required for creating HostedCheckouts
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.create_mandate_base.CreateMandateBase`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    @property
    def mandate_reference(self):
        """
        | A mandate ID to create a mandate under iff the information to create a mandate has been supplied. Otherwise refers to the Slimpay mandate to retrieve and use in the payment.
        
        Type: str
        """
        return self.__mandate_reference

    @mandate_reference.setter
    def mandate_reference(self, value):
        self.__mandate_reference = value

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentProduct771SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'mandate', self.mandate)
        self._add_to_dictionary(dictionary, 'mandateReference', self.mandate_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentProduct771SpecificInput, self).from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = CreateMandateBase()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        if 'mandateReference' in dictionary:
            self.mandate_reference = dictionary['mandateReference']
        return self
