# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_redirect_payment_method_specific_input import AbstractRedirectPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product809_specific_input import RedirectPaymentProduct809SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product816_specific_input import RedirectPaymentProduct816SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product840_specific_input import RedirectPaymentProduct840SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product861_specific_input import RedirectPaymentProduct861SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product863_specific_input import RedirectPaymentProduct863SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product882_specific_input import RedirectPaymentProduct882SpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirection_data import RedirectionData


class RedirectPaymentMethodSpecificInput(AbstractRedirectPaymentMethodSpecificInput):

    __is_recurring = None
    __payment_product809_specific_input = None
    __payment_product816_specific_input = None
    __payment_product840_specific_input = None
    __payment_product861_specific_input = None
    __payment_product863_specific_input = None
    __payment_product882_specific_input = None
    __redirection_data = None
    __return_url = None

    @property
    def is_recurring(self):
        """
        * true
        * false
        
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def payment_product809_specific_input(self):
        """
        | Object containing specific input required for Dutch iDeal payments (Payment product ID 809)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product809_specific_input.RedirectPaymentProduct809SpecificInput`
        """
        return self.__payment_product809_specific_input

    @payment_product809_specific_input.setter
    def payment_product809_specific_input(self, value):
        self.__payment_product809_specific_input = value

    @property
    def payment_product816_specific_input(self):
        """
        | Object containing specific input required for German giropay payments (Payment product ID 816)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product816_specific_input.RedirectPaymentProduct816SpecificInput`
        """
        return self.__payment_product816_specific_input

    @payment_product816_specific_input.setter
    def payment_product816_specific_input(self, value):
        self.__payment_product816_specific_input = value

    @property
    def payment_product840_specific_input(self):
        """
        | Object containing specific input required for PayPal payments (Payment product ID 840)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product840_specific_input.RedirectPaymentProduct840SpecificInput`
        """
        return self.__payment_product840_specific_input

    @payment_product840_specific_input.setter
    def payment_product840_specific_input(self, value):
        self.__payment_product840_specific_input = value

    @property
    def payment_product861_specific_input(self):
        """
        | Object containing specific input required for AliPay payments (Payment product ID 861)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product861_specific_input.RedirectPaymentProduct861SpecificInput`
        """
        return self.__payment_product861_specific_input

    @payment_product861_specific_input.setter
    def payment_product861_specific_input(self, value):
        self.__payment_product861_specific_input = value

    @property
    def payment_product863_specific_input(self):
        """
        | Object containing specific input required for We Chat Pay payments (Payment product ID 863)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product863_specific_input.RedirectPaymentProduct863SpecificInput`
        """
        return self.__payment_product863_specific_input

    @payment_product863_specific_input.setter
    def payment_product863_specific_input(self, value):
        self.__payment_product863_specific_input = value

    @property
    def payment_product882_specific_input(self):
        """
        | Object containing specific input required for Indian Net Banking payments (Payment product ID 882)
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product882_specific_input.RedirectPaymentProduct882SpecificInput`
        """
        return self.__payment_product882_specific_input

    @payment_product882_specific_input.setter
    def payment_product882_specific_input(self, value):
        self.__payment_product882_specific_input = value

    @property
    def redirection_data(self):
        """
        | Object containing browser specific redirection related data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirection_data.RedirectionData`
        """
        return self.__redirection_data

    @redirection_data.setter
    def redirection_data(self, value):
        self.__redirection_data = value

    @property
    def return_url(self):
        """
        | The URL that the customer is redirect to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        | Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of *protocol*://. This protocol must be registered on the device first.
        | URLs without a protocol will be rejected.
        
        Type: str
        
        Deprecated; Use redirectionData.returnUrl instead
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificInput, self).to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.payment_product809_specific_input is not None:
            dictionary['paymentProduct809SpecificInput'] = self.payment_product809_specific_input.to_dictionary()
        if self.payment_product816_specific_input is not None:
            dictionary['paymentProduct816SpecificInput'] = self.payment_product816_specific_input.to_dictionary()
        if self.payment_product840_specific_input is not None:
            dictionary['paymentProduct840SpecificInput'] = self.payment_product840_specific_input.to_dictionary()
        if self.payment_product861_specific_input is not None:
            dictionary['paymentProduct861SpecificInput'] = self.payment_product861_specific_input.to_dictionary()
        if self.payment_product863_specific_input is not None:
            dictionary['paymentProduct863SpecificInput'] = self.payment_product863_specific_input.to_dictionary()
        if self.payment_product882_specific_input is not None:
            dictionary['paymentProduct882SpecificInput'] = self.payment_product882_specific_input.to_dictionary()
        if self.redirection_data is not None:
            dictionary['redirectionData'] = self.redirection_data.to_dictionary()
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'paymentProduct809SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct809SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct809SpecificInput']))
            value = RedirectPaymentProduct809SpecificInput()
            self.payment_product809_specific_input = value.from_dictionary(dictionary['paymentProduct809SpecificInput'])
        if 'paymentProduct816SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct816SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct816SpecificInput']))
            value = RedirectPaymentProduct816SpecificInput()
            self.payment_product816_specific_input = value.from_dictionary(dictionary['paymentProduct816SpecificInput'])
        if 'paymentProduct840SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct840SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840SpecificInput']))
            value = RedirectPaymentProduct840SpecificInput()
            self.payment_product840_specific_input = value.from_dictionary(dictionary['paymentProduct840SpecificInput'])
        if 'paymentProduct861SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct861SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct861SpecificInput']))
            value = RedirectPaymentProduct861SpecificInput()
            self.payment_product861_specific_input = value.from_dictionary(dictionary['paymentProduct861SpecificInput'])
        if 'paymentProduct863SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct863SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct863SpecificInput']))
            value = RedirectPaymentProduct863SpecificInput()
            self.payment_product863_specific_input = value.from_dictionary(dictionary['paymentProduct863SpecificInput'])
        if 'paymentProduct882SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct882SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct882SpecificInput']))
            value = RedirectPaymentProduct882SpecificInput()
            self.payment_product882_specific_input = value.from_dictionary(dictionary['paymentProduct882SpecificInput'])
        if 'redirectionData' in dictionary:
            if not isinstance(dictionary['redirectionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectionData']))
            value = RedirectionData()
            self.redirection_data = value.from_dictionary(dictionary['redirectionData'])
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        return self
