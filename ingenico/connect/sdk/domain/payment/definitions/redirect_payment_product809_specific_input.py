# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct809SpecificInput(DataObject):
    """
    | Please find below specific input fields for payment product 809 (iDeal)
    """

    __expiration_period = None
    __issuer_id = None

    @property
    def expiration_period(self):
        """
        | This sets the maximum amount of minutes a customer has to complete the payment at the bank. After this period has expired it is impossible for the customer to make a payment and in case no payment has been made the transaction will be marked as unsuccessful and expired by the bank. Setting the expirationPeriod is convenient if you want to maximise the time a customer has to complete the payment. Please note that it is normal for a customer to take up to 5 minutes to complete a payment. Setting this value below 10 minutes is not advised.
        | You can set this value in minutes with a maximum value of 60 minutes. If no input is provided the default value of 60 is used for the transaction.
        
        Type: str
        
        Deprecated; Use RedirectPaymentMethodSpecificInput.expirationPeriod instead
        """
        return self.__expiration_period

    @expiration_period.setter
    def expiration_period(self, value):
        self.__expiration_period = value

    @property
    def issuer_id(self):
        """
        | ID of the issuing bank of the customer. A list of available issuerIDs can be obtained by using the retrieve payment product directory API.
        
        Type: str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value):
        self.__issuer_id = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct809SpecificInput, self).to_dictionary()
        if self.expiration_period is not None:
            dictionary['expirationPeriod'] = self.expiration_period
        if self.issuer_id is not None:
            dictionary['issuerId'] = self.issuer_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct809SpecificInput, self).from_dictionary(dictionary)
        if 'expirationPeriod' in dictionary:
            self.expiration_period = dictionary['expirationPeriod']
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        return self
