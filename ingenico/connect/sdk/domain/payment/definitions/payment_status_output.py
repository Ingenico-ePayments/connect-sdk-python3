# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.order_status_output import OrderStatusOutput


class PaymentStatusOutput(OrderStatusOutput):

    __is_authorized = None
    __is_refundable = None
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
        if self.three_d_secure_status is not None:
            dictionary['threeDSecureStatus'] = self.three_d_secure_status
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentStatusOutput, self).from_dictionary(dictionary)
        if 'isAuthorized' in dictionary:
            self.is_authorized = dictionary['isAuthorized']
        if 'isRefundable' in dictionary:
            self.is_refundable = dictionary['isRefundable']
        if 'threeDSecureStatus' in dictionary:
            self.three_d_secure_status = dictionary['threeDSecureStatus']
        return self
