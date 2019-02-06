#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.dispute.create_dispute_request import CreateDisputeRequest


class CreatePaymentDisputeExample(object):

    def example(self):
        with self.__get_client() as client:
            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 1234
            amount_of_money.currency_code = "USD"

            body = CreateDisputeRequest()
            body.amount_of_money = amount_of_money
            body.contact_person = "Wile Coyote"
            body.email_address = "wile.e.coyote@acmelabs.com"
            body.reply_to = "r.runner@acmelabs.com"
            body.request_message = "This is the message from the merchant to GlobalCollect. It is a a freeform text field."

            response = client.merchant("merchantId").payments().dispute("paymentId", body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
