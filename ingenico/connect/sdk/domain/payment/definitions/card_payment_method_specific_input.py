# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.payment.definitions.abstract_card_payment_method_specific_input import AbstractCardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.external_cardholder_authentication_data import ExternalCardholderAuthenticationData
from ingenico.connect.sdk.domain.payment.definitions.three_d_secure import ThreeDSecure


class CardPaymentMethodSpecificInput(AbstractCardPaymentMethodSpecificInput):

    __card = None
    __external_cardholder_authentication_data = None
    __is_recurring = None
    __return_url = None
    __three_d_secure = None

    @property
    def card(self):
        """
        | Object containing card details
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def external_cardholder_authentication_data(self):
        """
        | Object containing 3D secure details.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.external_cardholder_authentication_data.ExternalCardholderAuthenticationData`
        
        Deprecated; Use threeDSecure.externalCardholderAuthenticationData instead
        """
        return self.__external_cardholder_authentication_data

    @external_cardholder_authentication_data.setter
    def external_cardholder_authentication_data(self, value):
        self.__external_cardholder_authentication_data = value

    @property
    def is_recurring(self):
        """
        | Indicates if this transaction is of a one-off or a recurring type
        
        * true - This is recurring
        * false - This is one-off
        
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def return_url(self):
        """
        | The URL that the customer is redirect to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        | Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of *protocol*://. This protocol must be registered on the device first.
        | URLs without a protocol will be rejected.
        
        Type: str
        
        Deprecated; Use threeDSecure.redirectionData.returnUrl instead
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    @property
    def three_d_secure(self):
        """
        | Object containing specific data regarding 3-D Secure
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.three_d_secure.ThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value):
        self.__three_d_secure = value

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInput, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.external_cardholder_authentication_data is not None:
            dictionary['externalCardholderAuthenticationData'] = self.external_cardholder_authentication_data.to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
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
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = ThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
