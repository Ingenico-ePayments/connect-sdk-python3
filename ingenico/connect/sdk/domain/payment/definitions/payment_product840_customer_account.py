# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct840CustomerAccount(DataObject):
    """
    | PayPal account details as returned by PayPal
    """

    __account_id = None
    __billing_agreement_id = None
    __company_name = None
    __contact_phone = None
    __country_code = None
    __customer_account_status = None
    __customer_address_status = None
    __first_name = None
    __payer_id = None
    __surname = None

    @property
    def account_id(self):
        """
        | Username with which the PayPal account holder has registered at PayPal
        
        Type: str
        """
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = value

    @property
    def billing_agreement_id(self):
        """
        | Identification of the PayPal recurring billing agreement
        
        Type: str
        """
        return self.__billing_agreement_id

    @billing_agreement_id.setter
    def billing_agreement_id(self, value):
        self.__billing_agreement_id = value

    @property
    def company_name(self):
        """
        | Name of the company in case the PayPal account is owned by a business
        
        Type: str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        self.__company_name = value

    @property
    def contact_phone(self):
        """
        | The phone number of the PayPal account holder
        
        Type: str
        """
        return self.__contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self.__contact_phone = value

    @property
    def country_code(self):
        """
        | Country where the PayPal account is located
        
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def customer_account_status(self):
        """
        | Status of the PayPal account.
        | Possible values are:
        
        * verified - PayPal has verified the funding means for this account
        * unverified - PayPal has not verified the funding means for this account
        
        Type: str
        """
        return self.__customer_account_status

    @customer_account_status.setter
    def customer_account_status(self, value):
        self.__customer_account_status = value

    @property
    def customer_address_status(self):
        """
        | Status of the customer's shipping address as registered by PayPal
        | Possible values are:
        
        * none - Status is unknown at PayPal
        * confirmed - The address has been confirmed
        * unconfirmed - The address has not been confirmed
        
        Type: str
        """
        return self.__customer_address_status

    @customer_address_status.setter
    def customer_address_status(self, value):
        self.__customer_address_status = value

    @property
    def first_name(self):
        """
        | First name of the PayPal account holder
        
        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def payer_id(self):
        """
        | The unique identifier of a PayPal account and will never change in the life cycle of a PayPal account
        
        Type: str
        """
        return self.__payer_id

    @payer_id.setter
    def payer_id(self, value):
        self.__payer_id = value

    @property
    def surname(self):
        """
        | Surname of the PayPal account holder
        
        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct840CustomerAccount, self).to_dictionary()
        if self.account_id is not None:
            dictionary['accountId'] = self.account_id
        if self.billing_agreement_id is not None:
            dictionary['billingAgreementId'] = self.billing_agreement_id
        if self.company_name is not None:
            dictionary['companyName'] = self.company_name
        if self.contact_phone is not None:
            dictionary['contactPhone'] = self.contact_phone
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.customer_account_status is not None:
            dictionary['customerAccountStatus'] = self.customer_account_status
        if self.customer_address_status is not None:
            dictionary['customerAddressStatus'] = self.customer_address_status
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.payer_id is not None:
            dictionary['payerId'] = self.payer_id
        if self.surname is not None:
            dictionary['surname'] = self.surname
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct840CustomerAccount, self).from_dictionary(dictionary)
        if 'accountId' in dictionary:
            self.account_id = dictionary['accountId']
        if 'billingAgreementId' in dictionary:
            self.billing_agreement_id = dictionary['billingAgreementId']
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
        if 'contactPhone' in dictionary:
            self.contact_phone = dictionary['contactPhone']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'customerAccountStatus' in dictionary:
            self.customer_account_status = dictionary['customerAccountStatus']
        if 'customerAddressStatus' in dictionary:
            self.customer_address_status = dictionary['customerAddressStatus']
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'payerId' in dictionary:
            self.payer_id = dictionary['payerId']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        return self
