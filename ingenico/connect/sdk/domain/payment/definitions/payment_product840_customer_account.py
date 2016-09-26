#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct840CustomerAccount(DataObject):
    """
    Class PaymentProduct840CustomerAccount
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProduct840CustomerAccount
    
    Attributes:
        account_id:               str
        billing_agreement_id:     str
        company_name:             str
        country_code:             str
        customer_account_status:  str
        customer_address_status:  str
        first_name:               str
        payer_id:                 str
        surname:                  str
     """

    account_id = None
    billing_agreement_id = None
    company_name = None
    country_code = None
    customer_account_status = None
    customer_address_status = None
    first_name = None
    payer_id = None
    surname = None

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
