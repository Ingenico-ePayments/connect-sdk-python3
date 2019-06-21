# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectionData(DataObject):
    """
    | Object containing browser specific redirection related data
    """

    __return_url = None
    __variant = None

    @property
    def return_url(self):
        """
        | The URL that the customer is redirect to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        | Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of *protocol*://. This protocol must be registered on the device first.
        | URLs without a protocol will be rejected.
        
        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        self.__return_url = value

    @property
    def variant(self):
        """
        | Using the Configuration Center it is possible to create multiple variations of your MyCheckout payment pages. The redirection flow for 3-D Secure uses the MyCheckout payment pages to display the following types of pages:
        
        * Redirection page - All redirection using a POST method will load a page in the browser of the customer that performs the actual redirection. This page contains a message to the customer explaining what is happening.
        * MethodURL page - Certain Issuers will use a specific flow in case of 3-D Secure version 2 to directly collect information from the customer browser. This page contains a spinner indicating that this process is going on in.
        
        | By specifying a specific variant you can force the use of another variant than the default. This allows you to test out the effect of certain changes to your MyCheckout payment pages in a controlled manner. Please note that you need to specify the ID instead of the name of the variant.
        
        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value):
        self.__variant = value

    def to_dictionary(self):
        dictionary = super(RedirectionData, self).to_dictionary()
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectionData, self).from_dictionary(dictionary)
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self
