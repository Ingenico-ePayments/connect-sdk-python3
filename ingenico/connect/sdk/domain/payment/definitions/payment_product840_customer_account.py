#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct840CustomerAccount(DataObject):
    """
    Class PaymentProduct840CustomerAccount
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProduct840CustomerAccount
    """

    __account_id = None
    __billing_agreement_id = None
    __company_name = None
    __country_code = None
    __customer_account_status = None
    __customer_address_status = None
    __first_name = None
    __payer_id = None
    __surname = None

    @property
    def account_id(self):
        """
        str
        """
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = value

    @property
    def billing_agreement_id(self):
        """
        str
        """
        return self.__billing_agreement_id

    @billing_agreement_id.setter
    def billing_agreement_id(self, value):
        self.__billing_agreement_id = value

    @property
    def company_name(self):
        """
        str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        self.__company_name = value

    @property
    def country_code(self):
        """
        str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def customer_account_status(self):
        """
        str
        """
        return self.__customer_account_status

    @customer_account_status.setter
    def customer_account_status(self, value):
        self.__customer_account_status = value

    @property
    def customer_address_status(self):
        """
        str
        """
        return self.__customer_address_status

    @customer_address_status.setter
    def customer_address_status(self, value):
        self.__customer_address_status = value

    @property
    def first_name(self):
        """
        str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def payer_id(self):
        """
        str
        """
        return self.__payer_id

    @payer_id.setter
    def payer_id(self, value):
        self.__payer_id = value

    @property
    def surname(self):
        """
        str
        """
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct840CustomerAccount, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'accountId', self.account_id)
        self._add_to_dictionary(dictionary, 'billingAgreementId', self.billing_agreement_id)
        self._add_to_dictionary(dictionary, 'companyName', self.company_name)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        self._add_to_dictionary(dictionary, 'customerAccountStatus', self.customer_account_status)
        self._add_to_dictionary(dictionary, 'customerAddressStatus', self.customer_address_status)
        self._add_to_dictionary(dictionary, 'firstName', self.first_name)
        self._add_to_dictionary(dictionary, 'payerId', self.payer_id)
        self._add_to_dictionary(dictionary, 'surname', self.surname)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct840CustomerAccount, self).from_dictionary(dictionary)
        if 'accountId' in dictionary:
            self.account_id = dictionary['accountId']
        if 'billingAgreementId' in dictionary:
            self.billing_agreement_id = dictionary['billingAgreementId']
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
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
