#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.api_exception import ApiException
from ingenico.connect.sdk.declined_payout_exception import DeclinedPayoutException
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation
from ingenico.connect.sdk.domain.definitions.contact_details_base import ContactDetailsBase
from ingenico.connect.sdk.domain.payment.definitions.personal_name import PersonalName
from ingenico.connect.sdk.domain.payout.create_payout_request import CreatePayoutRequest
from ingenico.connect.sdk.domain.payout.definitions.payout_customer import PayoutCustomer
from ingenico.connect.sdk.domain.payout.definitions.payout_references import PayoutReferences


class CreatePayoutExample(object):

    def example(self):
        with self.__get_client() as client:
            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 2345
            amount_of_money.currency_code = "EUR"

            bank_account_iban = BankAccountIban()
            bank_account_iban.account_holder_name = "Wile E. Coyote"
            bank_account_iban.iban = "IT60X0542811101000000123456"

            address = Address()
            address.city = "Burbank"
            address.country_code = "US"
            address.house_number = "411"
            address.state = "California"
            address.street = "N Hollywood Way"
            address.zip = "91505"

            company_information = CompanyInformation()
            company_information.name = "Acme Labs"

            contact_details = ContactDetailsBase()
            contact_details.email_address = "wile.e.coyote@acmelabs.com"

            name = PersonalName()
            name.first_name = "Wile"
            name.surname = "Coyote"
            name.surname_prefix = "E."
            name.title = "Mr."

            customer = PayoutCustomer()
            customer.address = address
            customer.company_information = company_information
            customer.contact_details = contact_details
            customer.name = name

            references = PayoutReferences()
            references.merchant_reference = "AcmeOrder001"

            body = CreatePayoutRequest()
            body.amount_of_money = amount_of_money
            body.bank_account_iban = bank_account_iban
            body.customer = customer
            body.payout_date = "20150102"
            body.payout_text = "Payout Acme"
            body.references = references
            body.swift_code = "swift"

            try:
                response = client.merchant("merchantId").payouts().create(body)
            except DeclinedPayoutException as e:
                self.handle_declined_payout(e.payout_result)
            except ApiException as e:
                self.handle_api_errors(e.errors)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)

    def handle_declined_payout(self, payout_result):
        # handle the result here
        pass

    def  handle_api_errors(self, errors):
        # handle the errors here
        pass
