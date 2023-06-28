# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair
from ingenico.connect.sdk.domain.definitions.order_status_output import OrderStatusOutput


class PaymentStatusOutput(OrderStatusOutput):

    __is_authorized = None
    __is_refundable = None
    __is_retriable = None
    __provider_raw_output = None
    __three_d_secure_status = None

    @property
    def is_authorized(self):
        """
        | Indicates if the transaction has been authorized
        
        * true
        * false
        
        Type: bool
        """
        return self.__is_authorized

    @is_authorized.setter
    def is_authorized(self, value):
        self.__is_authorized = value

    @property
    def is_refundable(self):
        """
        | Flag indicating if the payment can be refunded
        
        * true
        * false
        
        Type: bool
        """
        return self.__is_refundable

    @is_refundable.setter
    def is_refundable(self, value):
        self.__is_refundable = value

    @property
    def is_retriable(self):
        """
        | Flag indicating whether a rejected payment may be retried by the merchant without incurring a fee 
        
        * true
        * false
        
        Type: bool
        """
        return self.__is_retriable

    @is_retriable.setter
    def is_retriable(self, value):
        self.__is_retriable = value

    @property
    def provider_raw_output(self):
        """
        | This is the raw response returned by the acquirer. This property contains unprocessed data directly returned by the acquirer. It's recommended for data analysis only due to its dynamic nature, which may undergo future changes.
        
        Type: list[:class:`ingenico.connect.sdk.domain.definitions.key_value_pair.KeyValuePair`]
        """
        return self.__provider_raw_output

    @provider_raw_output.setter
    def provider_raw_output(self, value):
        self.__provider_raw_output = value

    @property
    def three_d_secure_status(self):
        """
        | The 3D Secure status, with the following possible values:
        
        * ENROLLED: the card is enrolled for 3D Secure authentication. The customer can be redirected to a 3D Secure access control server (ACS)
        * NOT_ENROLLED: the card is not enrolled for 3D Secure authentication
        * INVALID_PARES_OR_NOT_COMPLETED: the PARes is invalid, or the customer did not complete the 3D Secure authentication
        * AUTHENTICATED: the customer has passed the 3D Secure authentication
        * NOT_AUTHENTICATED: the customer failed the 3D Secure authentication
        * NOT_PARTICIPATING: the cardholder has not set up their card for 2-step 3D Secure.
        
        | Note that this status will only be set for payments that make use of 2-step 3D Secure.
        
        Type: str
        """
        return self.__three_d_secure_status

    @three_d_secure_status.setter
    def three_d_secure_status(self, value):
        self.__three_d_secure_status = value

    def to_dictionary(self):
        dictionary = super(PaymentStatusOutput, self).to_dictionary()
        if self.is_authorized is not None:
            dictionary['isAuthorized'] = self.is_authorized
        if self.is_refundable is not None:
            dictionary['isRefundable'] = self.is_refundable
        if self.is_retriable is not None:
            dictionary['isRetriable'] = self.is_retriable
        if self.provider_raw_output is not None:
            dictionary['providerRawOutput'] = []
            for element in self.provider_raw_output:
                if element is not None:
                    dictionary['providerRawOutput'].append(element.to_dictionary())
        if self.three_d_secure_status is not None:
            dictionary['threeDSecureStatus'] = self.three_d_secure_status
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentStatusOutput, self).from_dictionary(dictionary)
        if 'isAuthorized' in dictionary:
            self.is_authorized = dictionary['isAuthorized']
        if 'isRefundable' in dictionary:
            self.is_refundable = dictionary['isRefundable']
        if 'isRetriable' in dictionary:
            self.is_retriable = dictionary['isRetriable']
        if 'providerRawOutput' in dictionary:
            if not isinstance(dictionary['providerRawOutput'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['providerRawOutput']))
            self.provider_raw_output = []
            for element in dictionary['providerRawOutput']:
                value = KeyValuePair()
                self.provider_raw_output.append(value.from_dictionary(element))
        if 'threeDSecureStatus' in dictionary:
            self.three_d_secure_status = dictionary['threeDSecureStatus']
        return self
