# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class HostedMandateManagementSpecificInput(DataObject):

    __locale = None
    __return_url = None
    __show_result_page = None
    __variant = None

    @property
    def locale(self):
        """
        | Locale to use to present the hosted mandate pages to the customer. Please make sure that a language pack is configured for the locale you are submitting. If you submit a locale that is not setup on your account we will use the default language pack for your account. You can easily upload additional language packs and set the default language pack in the Configuration Center.
        
        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def return_url(self):
        """
        | The URL that the customer is redirect to after the mandate flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        | Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of *protocol*://. This protocol must be registered on the device first.
        | URLs without a protocol will be rejected.
        
        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    @property
    def show_result_page(self):
        """
        * true - MyMandate will show a result page to the customer when applicable. Default.
        * false - MyMandate will redirect the customer back to the provided returnUrl when this is possible.
        
        | The default value for this property is true.
        
        Type: bool
        """
        return self.__show_result_page

    @show_result_page.setter
    def show_result_page(self, value):
        self.__show_result_page = value

    @property
    def variant(self):
        """
        | The ID of the variant used to create the Hosted Mandate Management Session in which the payment was made.
        
        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value):
        self.__variant = value

    def to_dictionary(self):
        dictionary = super(HostedMandateManagementSpecificInput, self).to_dictionary()
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.show_result_page is not None:
            dictionary['showResultPage'] = self.show_result_page
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary):
        super(HostedMandateManagementSpecificInput, self).from_dictionary(dictionary)
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'showResultPage' in dictionary:
            self.show_result_page = dictionary['showResultPage']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self
