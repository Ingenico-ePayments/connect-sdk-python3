#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment_product836_specific_output import PaymentProduct836SpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.payment_product840_specific_output import PaymentProduct840SpecificOutput


class RedirectPaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):
    """
    Class RedirectPaymentMethodSpecificOutput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RedirectPaymentMethodSpecificOutput
    """

    __bank_account_iban = None
    __payment_product836_specific_output = None
    __payment_product840_specific_output = None

    @property
    def bank_account_iban(self):
        """
        :class:`BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value):
        self.__bank_account_iban = value

    @property
    def payment_product836_specific_output(self):
        """
        :class:`PaymentProduct836SpecificOutput`
        """
        return self.__payment_product836_specific_output

    @payment_product836_specific_output.setter
    def payment_product836_specific_output(self, value):
        self.__payment_product836_specific_output = value

    @property
    def payment_product840_specific_output(self):
        """
        :class:`PaymentProduct840SpecificOutput`
        """
        return self.__payment_product840_specific_output

    @payment_product840_specific_output.setter
    def payment_product840_specific_output(self, value):
        self.__payment_product840_specific_output = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        self._add_to_dictionary(dictionary, 'paymentProduct836SpecificOutput', self.payment_product836_specific_output)
        self._add_to_dictionary(dictionary, 'paymentProduct840SpecificOutput', self.payment_product840_specific_output)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'paymentProduct836SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct836SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct836SpecificOutput']))
            value = PaymentProduct836SpecificOutput()
            self.payment_product836_specific_output = value.from_dictionary(dictionary['paymentProduct836SpecificOutput'])
        if 'paymentProduct840SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct840SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840SpecificOutput']))
            value = PaymentProduct840SpecificOutput()
            self.payment_product840_specific_output = value.from_dictionary(dictionary['paymentProduct840SpecificOutput'])
        return self
