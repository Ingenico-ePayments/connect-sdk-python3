#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.api_exception import ApiException
from ingenico.connect.sdk.declined_refund_exception import DeclinedRefundException
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.refund.refund_request import RefundRequest
from ingenico.connect.sdk.domain.refund.definitions.refund_references import RefundReferences


class CreateRefundCaptureExample(object):

    def example(self):
        with self.__get_client() as client:
            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 500
            amount_of_money.currency_code = "EUR"

            refund_references = RefundReferences()
            refund_references.merchant_reference = "AcmeOrder0001"

            body = RefundRequest()
            body.amount_of_money = amount_of_money
            body.refund_references = refund_references

            try:
                response = client.merchant("merchantId").captures().refund("captureId", body)
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

    def handle_api_errors(self, errors):
        # handle the errors here
        pass
