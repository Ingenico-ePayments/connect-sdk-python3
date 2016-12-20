#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from ingenico.connect.sdk.domain.payment.definitions.external_cardholder_authentication_data import ExternalCardholderAuthenticationData


class CardPaymentMethodSpecificInput(CardPaymentMethodSpecificInputBase):
    """
    Class CardPaymentMethodSpecificInput
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CardPaymentMethodSpecificInput
    """

    __card = None
    __external_cardholder_authentication_data = None
    __is_recurring = None
    __return_url = None

    @property
    def card(self):
        """
        :class:`Card`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def external_cardholder_authentication_data(self):
        """
        :class:`ExternalCardholderAuthenticationData`
        """
        return self.__external_cardholder_authentication_data

    @external_cardholder_authentication_data.setter
    def external_cardholder_authentication_data(self, value):
        self.__external_cardholder_authentication_data = value

    @property
    def is_recurring(self):
        """
        bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def return_url(self):
        """
        str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'card', self.card)
        self._add_to_dictionary(dictionary, 'externalCardholderAuthenticationData', self.external_cardholder_authentication_data)
        self._add_to_dictionary(dictionary, 'isRecurring', self.is_recurring)
        self._add_to_dictionary(dictionary, 'returnUrl', self.return_url)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'externalCardholderAuthenticationData' in dictionary:
            if not isinstance(dictionary['externalCardholderAuthenticationData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['externalCardholderAuthenticationData']))
            value = ExternalCardholderAuthenticationData()
            self.external_cardholder_authentication_data = value.from_dictionary(dictionary['externalCardholderAuthenticationData'])
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        return self
