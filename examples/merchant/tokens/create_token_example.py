#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation
from ingenico.connect.sdk.domain.token.create_token_request import CreateTokenRequest
from ingenico.connect.sdk.domain.token.definitions.customer_token import CustomerToken
from ingenico.connect.sdk.domain.token.definitions.mandate_non_sepa_direct_debit import MandateNonSepaDirectDebit
from ingenico.connect.sdk.domain.token.definitions.personal_information_token import PersonalInformationToken
from ingenico.connect.sdk.domain.token.definitions.personal_name_token import PersonalNameToken
from ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit import TokenNonSepaDirectDebit
from ingenico.connect.sdk.domain.token.definitions.token_non_sepa_direct_debit_payment_product705_specific_data import TokenNonSepaDirectDebitPaymentProduct705SpecificData


class CreateTokenExample(object):

    def example(self):
        with self.__get_client() as client:
            billing_address = Address()
            billing_address.additional_info = "Suite II"
            billing_address.city = "Monument Valley"
            billing_address.country_code = "US"
            billing_address.house_number = "1"
            billing_address.state = "Utah"
            billing_address.street = "Desertroad"
            billing_address.zip = "84536"

            company_information = CompanyInformation()
            company_information.name = "Acme Labs"

            name = PersonalNameToken()
            name.first_name = "Wile"
            name.surname = "Coyote"
            name.surname_prefix = "E."

            personal_information = PersonalInformationToken()
            personal_information.name = name

            customer = CustomerToken()
            customer.billing_address = billing_address
            customer.company_information = company_information
            customer.merchant_customer_id = "1234"
            customer.personal_information = personal_information

            bank_account_bban = BankAccountBban()
            bank_account_bban.account_number = "000000123456"
            bank_account_bban.bank_code = "05428"
            bank_account_bban.branch_code = "11101"
            bank_account_bban.check_digit = "X"
            bank_account_bban.country_code = "IT"

            payment_product705_specific_data = TokenNonSepaDirectDebitPaymentProduct705SpecificData()
            payment_product705_specific_data.authorisation_id = "123456"
            payment_product705_specific_data.bank_account_bban = bank_account_bban

            mandate = MandateNonSepaDirectDebit()
            mandate.payment_product705_specific_data = payment_product705_specific_data

            non_sepa_direct_debit = TokenNonSepaDirectDebit()
            non_sepa_direct_debit.customer = customer
            non_sepa_direct_debit.mandate = mandate

            body = CreateTokenRequest()
            body.non_sepa_direct_debit = non_sepa_direct_debit
            body.payment_product_id = 705

            response = client.merchant("merchantId").tokens().create(body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
