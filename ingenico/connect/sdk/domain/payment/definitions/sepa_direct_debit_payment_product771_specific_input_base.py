# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.mandates.definitions.create_mandate_base import CreateMandateBase
from ingenico.connect.sdk.domain.payment.definitions.abstract_sepa_direct_debit_payment_product771_specific_input import AbstractSepaDirectDebitPaymentProduct771SpecificInput


class SepaDirectDebitPaymentProduct771SpecificInputBase(AbstractSepaDirectDebitPaymentProduct771SpecificInput):
    """
    | Object containing information specific to SEPA Direct Debit for Hosted Checkouts.
    """

    __existing_unique_mandate_reference = None
    __mandate = None

    @property
    def existing_unique_mandate_reference(self):
        """
        | The unique reference of the existing mandate to use in this payment.
        
        Type: str
        """
        return self.__existing_unique_mandate_reference

    @existing_unique_mandate_reference.setter
    def existing_unique_mandate_reference(self, value):
        self.__existing_unique_mandate_reference = value

    @property
    def mandate(self):
        """
        | Object containing information to create a SEPA Direct Debit mandate.
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.create_mandate_base.CreateMandateBase`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentProduct771SpecificInputBase, self).to_dictionary()
        if self.existing_unique_mandate_reference is not None:
            dictionary['existingUniqueMandateReference'] = self.existing_unique_mandate_reference
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentProduct771SpecificInputBase, self).from_dictionary(dictionary)
        if 'existingUniqueMandateReference' in dictionary:
            self.existing_unique_mandate_reference = dictionary['existingUniqueMandateReference']
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = CreateMandateBase()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
