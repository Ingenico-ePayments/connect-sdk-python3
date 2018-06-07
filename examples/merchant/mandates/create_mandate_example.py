#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban
from ingenico.connect.sdk.domain.mandates.create_mandate_request import CreateMandateRequest
from ingenico.connect.sdk.domain.mandates.definitions.mandate_address import MandateAddress
from ingenico.connect.sdk.domain.mandates.definitions.mandate_contact_details import MandateContactDetails
from ingenico.connect.sdk.domain.mandates.definitions.mandate_customer import MandateCustomer
from ingenico.connect.sdk.domain.mandates.definitions.mandate_personal_information import MandatePersonalInformation
from ingenico.connect.sdk.domain.mandates.definitions.mandate_personal_name import MandatePersonalName


class CreateMandateExample(object):

    def example(self):
        with self.__get_client() as client:
            bank_account_iban = BankAccountIban()
            bank_account_iban.iban = "DE46940594210000012345"

            contact_details = MandateContactDetails()
            contact_details.email_address = "wile.e.coyote@acmelabs.com"

            mandate_address = MandateAddress()
            mandate_address.city = "Monumentenvallei"
            mandate_address.country_code = "NL"
            mandate_address.street = "Woestijnweg"
            mandate_address.zip = "1337XD"

            name = MandatePersonalName()
            name.first_name = "Wile"
            name.surname = "Coyote"

            personal_information = MandatePersonalInformation()
            personal_information.name = name
            personal_information.title = "Miss"

            customer = MandateCustomer()
            customer.bank_account_iban = bank_account_iban
            customer.company_name = "Acme labs"
            customer.contact_details = contact_details
            customer.mandate_address = mandate_address
            customer.personal_information = personal_information

            body = CreateMandateRequest()
            body.customer = customer
            body.customer_reference = "idonthaveareference"
            body.language = "nl"
            body.recurrence_type = "UNIQUE"
            body.signature_type = "UNSIGNED"

            response = client.merchant("merchantId").mandates().create(body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
