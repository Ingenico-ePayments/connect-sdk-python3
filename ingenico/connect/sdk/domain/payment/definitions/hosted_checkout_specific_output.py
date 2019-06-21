# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class HostedCheckoutSpecificOutput(DataObject):

    __hosted_checkout_id = None
    __variant = None

    @property
    def hosted_checkout_id(self):
        """
        | The ID of the Hosted Checkout Session in which the payment was made.
        
        Type: str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value):
        self.__hosted_checkout_id = value

    @property
    def variant(self):
        """
        | Using the Configuration Center it is possible to create multiple variations of your MyCheckout payment pages. By specifying a specific variant you can force the use of another variant then the default. This allows you to test out the effect of certain changes to your hosted mandate pages in a controlled manner. Please note that you need to specify the ID of the variant.
        
        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value):
        self.__variant = value

    def to_dictionary(self):
        dictionary = super(HostedCheckoutSpecificOutput, self).to_dictionary()
        if self.hosted_checkout_id is not None:
            dictionary['hostedCheckoutId'] = self.hosted_checkout_id
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary):
        super(HostedCheckoutSpecificOutput, self).from_dictionary(dictionary)
        if 'hostedCheckoutId' in dictionary:
            self.hosted_checkout_id = dictionary['hostedCheckoutId']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self
