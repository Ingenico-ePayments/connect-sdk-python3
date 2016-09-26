#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
import os

from ingenico.connect.sdk.api_exception import ApiException
from ingenico.connect.sdk.declined_refund_exception import DeclinedRefundException
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal
from ingenico.connect.sdk.domain.payment.definitions.personal_name import PersonalName
from ingenico.connect.sdk.domain.refund.refund_request import RefundRequest
from ingenico.connect.sdk.domain.refund.definitions.bank_refund_method_specific_input import BankRefundMethodSpecificInput
from ingenico.connect.sdk.domain.refund.definitions.refund_customer import RefundCustomer
from ingenico.connect.sdk.domain.refund.definitions.refund_references import RefundReferences


class RefundPaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 1
            amount_of_money.currency_code = "EUR"

            bank_account_iban = BankAccountIban()
            bank_account_iban.iban = "NL53INGB0000000036"

            bank_refund_method_specific_input = BankRefundMethodSpecificInput()
            bank_refund_method_specific_input.bank_account_iban = bank_account_iban

            name = PersonalName()
            name.surname = "Coyote"

            address = AddressPersonal()
            address.country_code = "US"
            address.name = name

            contact_details = ContactDetailsBase()
            contact_details.email_address = "wile.e.coyote@acmelabs.com"
            contact_details.email_message_type = "html"

            customer = RefundCustomer()
            customer.address = address
            customer.contact_details = contact_details

            refund_references = RefundReferences()
            refund_references.merchant_reference = "AcmeOrder0001"

            body = RefundRequest()
            body.amount_of_money = amount_of_money
            body.bank_refund_method_specific_input = bank_refund_method_specific_input
            body.customer = customer
            body.refund_date = "20140306"
            body.refund_references = refund_references

            try:
                response = client.merchant("merchantId").payments().refund("paymentId", body)
            except DeclinedRefundException as e:
                self.handle_declined_refund(e.refund_result)
            except ApiException as e:
                self.handle_api_errors(e.errors)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)

    def handle_declined_refund(self, refund_result):
        # handle the result here
        pass

    def  handle_api_errors(self, errors):
        # handle the errors here
        pass
