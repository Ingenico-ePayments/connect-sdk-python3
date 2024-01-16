#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.token.approve_token_request import ApproveTokenRequest


class ApproveSepaDirectDebitTokenExample(object):

    def example(self):
        with self.__get_client() as client:
            body = ApproveTokenRequest()
            body.mandate_signature_date = "20150201"
            body.mandate_signature_place = "Monument Valley"
            body.mandate_signed = True

            client.merchant("merchantId").tokens().approvesepadirectdebit("tokenId", body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
